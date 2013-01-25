# -*- coding: utf-8 -*-
"""
    Copyright (C) 2013 Kouhei Maeda <mkouhei@palmtb.net>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import sys
from setuptools import setup, find_packages

sys.path.insert(0, 'src')
import meibo

classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: System Administrators",
    "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    "Programming Language :: Python",
    "Topic :: System :: Systems Administration",
    "Topic :: Internet :: WWW/HTTP",
]

long_description = \
        open(os.path.join("docs","README.rst")).read() + \
        open(os.path.join("docs","HISTORY.rst")).read() + \
        open(os.path.join("docs","TODO.rst")).read()

requires = ['setuptools', 'httplib2', 'pyquery']

setup(name='meibo',
      version=meibo.__version__,
      description='Retrieve userlist of Mailman',
      long_description=long_description,
      author='Kouhei Maeda',
      author_email='mkouhei@palmtb.net',
      url='https://github.com/mkouhei/meibo',
      classifiers=classifiers,
      packages=find_packages('src'),
      package_dir={'': 'src'},
      data_files = [('share/meibo/examples',
                     ['examples/meibo.conf'])],
      install_requires=requires,
      include_package_data = True,
      extras_require=dict(
        test=['pytest', 'pep8', 'unittest'],
        ),
      test_suite='tests.runtest',
      tests_require=['pytest','pep8','unittest'],
      entry_points= {
        "console_scripts": [
            "tazuna = meibo.runapp:main",
            ]
        },
)
