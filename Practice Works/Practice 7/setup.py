from distutils.core import setup, Extension

module1 = Extension('meanmod', sources=['source.cpp'])

setup(name='MeanModule',
      version='1.0',
      description='Calculation of arithmetic mean',
      ext_modules=[module1])