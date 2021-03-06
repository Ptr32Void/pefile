#!/usr/bin/python

import os
import sys

try:
    from setuptools import setup
except ImportError, excp:
    from distutils.core import setup

import pefile


os.environ['COPY_EXTENDED_ATTRIBUTES_DISABLE'] = 'true'
os.environ['COPYFILE_DISABLE'] = 'true'

# build_msi does not support the 1.2.10-139 versioning schema
# (or 1.2.10.139), hence the revision number is stripped.
pefile_version = pefile.__version__
if 'bdist_msi' in sys.argv:
    pefile_version, _, _ = pefile_version.partition('-')

setup(name = 'pefile',
    version = pefile_version,
    description = 'Python PE parsing module',
    author = pefile.__author__,
    author_email = pefile.__contact__,
    url = 'https://github.com/erocarrera/pefile',
    download_url = 'https://github.com/erocarrera/pefile/archive/pefile-%s.tar.gz' % pefile.__version__,
    platforms = ['any'],
    classifiers = ['Development Status :: 5 - Production/Stable',
    	'Intended Audience :: Developers',
    	'Intended Audience :: Science/Research',
    	'Natural Language :: English',
    	'Operating System :: OS Independent',
    	'Programming Language :: Python',
    	'Topic :: Software Development :: Libraries :: Python Modules'],
    long_description = "\n".join(pefile.__doc__.split('\n')),
    py_modules = ['pefile', 'peutils'],
    packages = ['ordlookup'] )
