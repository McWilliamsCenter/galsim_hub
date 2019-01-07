# GalSim Hub

GalSim Hub provides a collection of TensorFlow modules for GalSim.

## Installation

To install:
```sh
 $ pip install --user galsim-hub
```

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

model = galsim_hub.GenerativeGalaxyModel('hub:cosmos_size_mag')

# Defines the input conditions, for this model flux_radius and mag_auto
cat = Table([[5., 10. ,20.], [24., 24., 24.] ],
             names=['flux_radius', 'mag_auto'])

# Sample light profiles for these parameters
ims = model.sample(cat)
```
