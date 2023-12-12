from pathlib import Path
from setuptools import setup, Extension
import Cython.Build

# read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "readme.md").read_text()

version = '0.0.6'

ext = Extension(name="jsondb_in_memory", sources=["jsondb_in_memory.py"])

setup(
    name='jsondb_in_memory',
    version=version,
    description='Sychronized, streaming dictionary that uses shared memory as a backend',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ronny Rentner',
    author_email='',
    url='https://github.com/wanghaisheng/json-dict-in-memory',
    cmdclass={'build_ext': Cython.Build.build_ext},
    package_dir={'jsondb_in_memory': '.'},
    packages=['jsondb_in_memory'],
    zip_safe=False,
    ext_modules=Cython.Build.cythonize(ext, compiler_directives={'language_level' : "3"}),
    setup_requires=['cython>=0.24.1'],
    python_requires=">=3.8",
)
