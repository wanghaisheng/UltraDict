from pathlib import Path
from setuptools import setup, Extension
import Cython.Build

# read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "readme.md").read_text()
print(long_description)
version = '0.0.9'

ext = Extension(name="i18n_json", sources=["i18n_json.py"])

setup(
    name='i18n_json',
    version=version,
    description='Sychronized, streaming dictionary that uses shared memory as a backend',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='wanghaisheng',
    author_email='admin@tiktokastudio.com',
    url='https://github.com/wanghaisheng/json-dict-in-memory',
    cmdclass={'build_ext': Cython.Build.build_ext},
    package_dir={'i18n_json': '.'},
    packages=['i18n_json'],
    zip_safe=False,
    ext_modules=Cython.Build.cythonize(ext, compiler_directives={'language_level' : "3"}),
    setup_requires=['cython>=0.24.1'],
    python_requires=">=3.8",
    include_package_data=True    
)
