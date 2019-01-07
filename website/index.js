import * as tf from '@tensorflow/tfjs';
import * as ta from 'time-ago';

const data = require('./web_model/weights_manifest.json');

const fakeCanvas = document.getElementById('fake-canvas');
const testModel = document.getElementById('test');

/**
 * Generate a set of examples using the generator model of the ACGAN.
 *
 * @param {tf.Model} generator The generator part of the ACGAN.
 */
async function generateAndVisualizeImages(generator) {

  const combinedFakes = tf.tidy(() => {

    const t0 = tf.util.now();
    const generatedImages = generator.predict(tf.randomNormal([10, 64]));
    generatedImages.dataSync();  // For accurate timing benchmark.
    const elapsed = tf.util.now() - t0;
    // Concatenate the images horizontally into a single image.
    return tf.clipByValue(tf.concat(tf.unstack(generatedImages.mul(20)), 1), 0,1);
  });

  await tf.toPixels(combinedFakes, fakeCanvas);
  tf.dispose(combinedFakes);
}


async function init() {

  const LOCAL_WEIGHTS_PATH = 'https://raw.githubusercontent.com/EiffL/GalSim-Hub/tensorflowjs/web_model/weights_manifest.json';
  const LOCAL_MODEL_PATH = 'https://raw.githubusercontent.com/EiffL/GalSim-Hub/tensorflowjs/web_model/tensorflowjs_model.pb';

  // Attempt to load locally-saved model. If it fails, activate the
  // "Load hosted model" button.
  let model;
  try {
    model = await tf.loadFrozenModel(LOCAL_MODEL_PATH, LOCAL_WEIGHTS_PATH);
  } catch (err) {
    console.error(err);
  }

  testModel.addEventListener('click', async () => {
    await generateAndVisualizeImages(model);
  });

}

init();
