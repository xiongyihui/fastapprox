from distutils.core import setup
from Cython.Build import cythonize

setup(name='fastapprox',
      ext_modules=cythonize("fastapprox.pyx"))