from setuptools import setup
from io import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='galsim_hub',
    version='0.0.1rc2',
    description='Support for Tensorflow Hub modules in GalSim',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/McWilliamsCenter/galsim_hub',
    author='Francois Lanusse',
    classifiers=[
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Astronomy',
        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    packages=['galsim_hub'],
    install_requires=['galsim', 'tensorflow', 'tensorflow_hub']
)
