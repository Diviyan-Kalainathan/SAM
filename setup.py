# -*- coding: utf-8 -*-
# Copyright (C) 2016 Diviyan Kalainathan
# Licence: Apache 2.0

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def setup_package():
    """Install the package."""
    setup(name='cdt',
          version='0.1',
          description='Structural Agnostic Model',
          url='https://github.com/Diviyan-Kalainathan/CausalDiscoveryToolbox',
          author='Diviyan Kalainathan',
          author_email='diviyan.kalainathan@lri.fr',
          license='Apache 2.0',
          packages=['sam'])


if __name__ == '__main__':
    setup_package()
