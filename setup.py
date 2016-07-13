#!/usr/bin/env python

import sys
from distutils.core import setup

# force the statlib in this directory (for version detection)
sys.path.insert(0, '.')
import statlib

if sys.version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None

setup( 
    name='statlib',
    version=statlib.version,
    description='A collection of statistical modules (stats.py, pstats.py, matfunc.py)',
    author='Gary Strangman, Raymond Hettinger',
    author_email='strang@nmr.mgh.harvard.edu,python@rcn.com',
    maintainer='Istvan Albert',
    maintainer_email='istvan.albert@gmail.com',
    url='http://python-statlib.googlecode.com/',
    download_url="http://python-statlib.googlecode.com/files/statlib-%s.tar.gz" % statlib.version,
    packages = [ "statlib" ],
    classifiers=[
       'Development Status :: 5 - Production/Stable',
       'License :: OSI Approved :: MIT License',
       'Programming Language :: Python',
       'Operating System :: OS Independent',
       'Intended Audience :: Developers',
     ],
)