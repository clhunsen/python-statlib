#!/usr/bin/env python

from sys import version
from distutils.core import setup

if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None

setup( 
    name='statlib',
    version='1.0.1',
    description='A collection of statistical modules (stats.py, pstats.py, matfunc.py)',
    author='Raymond Hettinger, Gary Strangman',
    author_email='python@rcn.com, strang@nmr.mgh.harvard.edu',
    maintainer='Istvan Albert',
    maintainer_email='istvan.albert@gmail.com',
    url='http://python-statlib.googlecode.com/',
    download_url="http://python-statlib.googlecode.com/files/statlib-1.0.1.tar.gz",
    packages = [ "statlib" ],
    classifiers=[
       'Development Status :: 5 - Production/Stable',
       'License :: OSI Approved :: MIT License',
       'Programming Language :: Python',
       'Operating System :: OS Independent',
       'Intended Audience :: Developers',
     ],
)