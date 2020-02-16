# -*- coding: utf-8 -*-
# Import needed function from setuptools
from setuptools import setup

# Create proper setup to be used by pip
setup(name='AutoClassifier',
      version='0.0.1',
      description='Automatically performs binary classification',
      author='Ashwin Rai',
      email='ashwin2rai@gmail.com',
      packages=['autoclassifier'],
	install_requires=['keras',
 'keras-applications',
 'keras-base',
 'keras-preprocessing',
 'matplotlib==3.1.1',
 'numpy==1.16.4',
 'numpy-base==1.16.4',
 'numpydoc=0.9.1',
 'pandas==0.25.1',
 'path.py',
 'pathlib2',
 'pep8',
 'pip',
 'scikit-learn==0.21.2',
 'scipy==1.3.1',
 'setuptools',
 'statsmodels==0.10.1',
 'tensorflow',
 'tensorflow-base',
 'tensorflow-estimator'])

