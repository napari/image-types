#!/usr/bin/env python
"""
napari mage types
=================
"""

MIN_PY_VER = '3.6'
DISTNAME = 'image-types'
DESCRIPTION = 'Types to annotate image processing functions'
LONG_DESCRIPTION = __doc__
LICENSE = 'BSD 3-Clause'
DOWNLOAD_URL = 'https://github.com/napari/image-types'

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: C',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Visualization',
    'Topic :: Scientific/Engineering :: Information Analysis',
    'Topic :: Scientific/Engineering :: Bio-Informatics',
    'Topic :: Utilities',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Operating System :: MacOS'
]

import imtypes
import sys
from setuptools import setup


if sys.version_info < (3, 6):
    sys.stderr.write('You are using Python '
                     f'{".".join(str(v) for v in sys.version_info[:3])}.\n\n'
                     'image-types only supports Python 3.6 and above. ')
    sys.exit(1)


with open('requirements.txt') as f:
    requirements = [line.strip() for line in f
                    if line and not line.startswith('#')]


INSTALL_REQUIRES = []

if __name__ == '__main__':
    setup(
        name=DISTNAME,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        license=LICENSE,
        download_url=DOWNLOAD_URL,
        version=imtypes.__version__,
        classifiers=CLASSIFIERS,
        install_requires=INSTALL_REQUIRES,
        requires=requirements,
        python_requires=f'>={MIN_PY_VER}',
        packages=['imtypes'],
        include_package_data=True,
        zip_safe=False  # the package can run out of an .egg file
    )
