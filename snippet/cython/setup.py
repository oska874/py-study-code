# -*- coding:utf8 -*-
from distutils.core import setup,Extension
from Cython.Build import cythonize

#ext
ext = Extension(name="wrap_p22",sources=["p22.c","wrap_p22.pyx"])

#cythonize：编译源代码为C或C++，返回一个distutils Extension对象列表
setup(ext_modules=cythonize(ext))
