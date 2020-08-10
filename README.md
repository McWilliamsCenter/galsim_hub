# GalSim Hub

[![PyPI](https://img.shields.io/pypi/v/galsim-hub)](https://pypi.org/project/galsim-hub/) [![PyPI - License](https://img.shields.io/pypi/l/galsim-hub)](https://github.com/McWilliamsCenter/galsim_hub/blob/master/LICENSE) 

GalSim Hub provides a collection of TensorFlow modules for GalSim.

## TL;DR

GalSim Hub makes it easy to incorporate galaxy light profiles modelled by deep neural networks directly with a GalSim script:

```py
import galsim
import galsim_hub
from astropy.table import Table

# Load a generative model from the online repository
model = galsim_hub.GenerativeGalaxyModel('hub:Lanusse2020')

# Defines the input conditions, for this model flux_radius, mag_auto, and redshift
catalog = Table([[5., 10. ,20.], [24., 24., 24.], [0.5, 0.5, 0.5] ],
             names=['flux_radius', 'mag_auto', 'zphot'])

# Sample light profiles for these parameters
profiles = model.sample(catalog)
...
```
You can read more, and try out a live demo here: [![colab link](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/McWilliamsCenter/galsim_hub/blob/master/notebooks/GalsimHubDemo.ipynb)

## Installation

To install:
```sh
 $ pip install --user galsim-hub
```
**Note**: GalSim-Hub currently assumes TensorFlow 1.15 to be installed, and will not try to install it as a dependency.


## Usage

This module can be used directly under the GalSim Yaml driver:
```sh
 $ galsim examples/demo14.yaml
```
or from Python:
```py
import galsim
import galsim_hub
from astropy.table import Table

# Load a generative model from the online repository
model = galsim_hub.GenerativeGalaxyModel('hub:Lanusse2020')

# Defines the input conditions, for this model flux_radius, mag_auto, and redshift
catalog = Table([[5., 10. ,20.], [24., 24., 24.], [0.5, 0.5, 0.5] ],
             names=['flux_radius', 'mag_auto', 'zphot'])

# Sample light profiles for these parameters
profiles = model.sample(catalog)
...
```

## Adding a model to the repository

This repository is intended to host a collection of deep generative models, any new contributions are welcome.
Submitting your model to the Hub means that it becomes trivially accessible to any GalSim user, increasing the chances that it will be used in practice :-)

To submit a model, please open a Pull Request adding a new folder under the `hub`directory. As the procedure is not currently completely documented, do not hesitate to reach out to the maintainers of the repository for guidance.


