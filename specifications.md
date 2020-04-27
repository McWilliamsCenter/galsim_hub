# Specifications for GalSim Hub Modules

GalSim Hub modules are based on [TensorFlow Hub](https://www.tensorflow.org/hub) models
with a set of specific inputs and attributes.

GalSim Hub expects the models to produce as an output an **unconvolved** light profile
as a postage stamp of a given size. This postage stamp will then be wrapped as an
InterpolatedImage object to be used within GalSim.

Inputs are optional, if some named inputs are declared in the module they are interpreted as input parameters for the GalSim light profile.

More presicely:
 - **Inputs**: Optional tensors of size at most 1d, designated by a keyword.
The following keywords are reserved:
    - `random_normal`: tensor. To ensure full reproducibility, we recommend extracting
    all random number generation out of the TensorFlow Hub module. GalSim Hub will
    automatically recognize the keyword `random_normal` and will use GalSim to
    generate an appropriate random number.

 - **Outputs**: A single default output is expected, in the form of a ([None, stamp_size, stamp_size]) float32 tensor.

 - **Attributes**: The following module attributes are expected
  - `stamp_size`: Size of the light profile postage stamp in pixels
  - `pixel_size`: Pixel resolution of the model
