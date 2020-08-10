from setuptools import setup
from setuptools import find_packages
from io import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='galsim_hub',
    description='Support for Tensorflow Hub modules in GalSim',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/McWilliamsCenter/galsim_hub',
    author='Francois Lanusse',
    author_email='francois.lanusse@cea.fr',
    classifiers=[
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Astronomy',
        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(),
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    install_requires=['galsim', 'tensorflow_hub']
)
