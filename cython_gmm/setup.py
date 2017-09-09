from distutils.core import setup, Extension
from Cython.Build import cythonize

ext = Extension("GMM_PY",
                sources=["GMM_PY.pyx", "gmm.cc"],
                language="c++")

setup(name="GMM_PY",
      ext_modules=cythonize(ext))
