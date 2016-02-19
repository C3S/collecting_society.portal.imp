#!/usr/bin/env python
# For copyright and license terms, see COPYRIGHT.rst (top level of repository)
# Repository: https://github.com/C3S/collecting_society.portal.imp

import os
from setuptools import setup, find_packages

MODULE = 'collecting_society_portal_imp'
PREFIX = 'c3s'

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGELOG.rst')) as f:
    CHANGELOG = f.read()

requires = [
    '%s_collecting_society_portal' % (PREFIX),
    '%s_collecting_society_portal_creative' % (PREFIX),
    'requests',
]

setup(
    name='%s_%s' % (PREFIX, MODULE),
    version='0.1',
    description=(
        'Plugin for collecting_society.portal including: IMP web frontend, ',
        'Musician, Musicfan, Client API'
    ),
    long_description=README + '\n\n' + CHANGELOG,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Framework :: Pyramid',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Legal Industry',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Natural Language :: English',
        'Natural Language :: German',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Office/Business',
        'Topic :: Office/Business :: Financial :: Accounting',
        'Topic :: Artistic Software',
    ],
    license='AGPL-3',
    author='Alexander Blum',
    author_email='alexander.blum@c3s.cc',
    url='https://github.com/C3S/collecting_society.portal.imp',
    keywords='web pyramid pylons collecting society',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=requires,
    test_suite='%s' % (MODULE),
)
