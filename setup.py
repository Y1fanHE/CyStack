from distutils.core import setup,Extension
from Cython.Build import cythonize

mod=Extension(
    "cstack",
    sources=["cstack.pyx"],
    language="c++"
)

setup(ext_modules = cythonize(mod))