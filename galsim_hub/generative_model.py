# Copyright (c) 2012-2018 by the GalSim developers team on GitHub
# https://github.com/GalSim-developers
#
# This file is part of GalSim: The modular galaxy image simulation toolkit.
# https://github.com/GalSim-developers/GalSim
#
# GalSim is free software: redistribution and use in source and binary forms,
# with or without modification, are permitted provided that the following
# conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions, and the disclaimer given in the accompanying LICENSE
#    file.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions, and the disclaimer given in the documentation
#    and/or other materials provided with the distribution.
#
"""@file generative_model.py
Functions defining a light profile produced by a deep generative model

TODO: add more documentation
"""
import galsim
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

class GenerativeGalaxyModel(object):
    """
    Generator object
    """

    _req_params = {'file_name': str}
    _opt_params = {}
    _single_params = []

    def __init__(self, file_name=None):
        """
        Initialisation of the generator, by loading a tensorflow model

        Parameters
        ----------
        dir: string
            Path to the tensorflow model to load,
            or a the module name on galsim-hub using the format `hub:module_name`
        """
        if 'hub:' in file_name:
            file_name = "https://github.com/McWilliamsCenter/galsim_hub/blob/master/hub/%s/model.tar.gz?raw=true"%file_name.split(':')[1]

        self.file_name = file_name
        self.module = None

        self.quantities = []
        self.random_variables = []
        self.sample_req_params = {}
        self.sample_opt_params = {}
        self.sample_single_params = []

        module = hub.Module(self.file_name)
        self.stamp_size = module.get_attached_message("stamp_size", tf.train.Int64List).value[0]
        self.pixel_size = module.get_attached_message("pixel_size", tf.train.FloatList).value[0]
        for k in module.get_input_info_dict():
            # Check for random variables
            if 'random_normal' in k:
                self.random_variables.append(k)
                continue
            # Otherwise add the rest of the conditional variables to the input
            self.quantities.append(k)
            self.sample_req_params[k] = float

    def sample(self, cat, noise=None,  rng=None, x_interpolant=None, k_interpolant=None,
                pad_factor=4, noise_pad_size=0, gsparams=None, session_config=None):
        """
        Samples galaxy images from the model
        """
        # If we are sampling for the first time
        if self.module is None:
            self.module = hub.Module(self.file_name)

            self.sess = tf.Session(session_config)
            self.sess.run(tf.global_variables_initializer())

            self.inputs = {}
            for k in self.quantities+self.random_variables:
                tensor_info = self.module.get_input_info_dict()[k]
                self.inputs[k] = tf.placeholder(tensor_info.dtype, shape=tensor_info.get_shape(), name=k)

            self.generated_images = self.module(self.inputs)

        # Populate feed dictionary with input data
        feed_dict={self.inputs[k]: cat[k] for k in self.quantities}

        # If not provided, create a RNG
        if rng is None:
            rng = galsim.BaseDeviate(rng)
            orig_rng = rng.duplicate()

        # Look for requested random_variables
        if 'random_normal' in self.random_variables:
            # Draw a random normal from the galsim RNG
            noise_shape = self.module.get_input_info_dict()['random_normal'].get_shape()
            noise_shape = [len(cat)] + [noise_shape[i+1].value for i in range(len(noise_shape)-1)]
            noise_array = np.empty(np.prod(noise_shape), dtype=float)
            gd = galsim.random.GaussianDeviate(rng, sigma=1)
            gd.generate(noise_array)
            feed_dict[self.inputs['random_normal']] = noise_array.reshape(noise_shape).astype('float32')

        # Run the graph
        x = self.sess.run(self.generated_images, feed_dict=feed_dict)

        # Now, we build an InterpolatedImage for each of these
        ims = []
        for i in range(len(x)):
            im = galsim.Image(np.ascontiguousarray(x[i].reshape((self.stamp_size, self.stamp_size)).astype(np.float64)),
                              scale=self.pixel_size)

            ims.append(galsim.InterpolatedImage(im,
                                                x_interpolant=x_interpolant,
                                                k_interpolant=k_interpolant,
                                                pad_factor=pad_factor,
                                                noise_pad_size=noise_pad_size,
                                                noise_pad=noise,
                                                rng=rng,
                                                gsparams=gsparams))
        if len(ims) == 1:
            ims = ims[0]

        return ims
