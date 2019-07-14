from distutils.core import setup

from Cython.Build import cythonize

from distutils.extension import Extension

import numpy

ext_modules = [

    Extension(
        "onp",
        ["orig_np_1.pyx"],

    )

]

setup(

    ext_modules=cythonize(ext_modules,language_level=3,annotate=True),

    include_dirs=[numpy.get_include()]

)
