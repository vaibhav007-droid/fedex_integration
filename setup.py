# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from pip._internal.req import parse_requirements
import re, ast

# get version from __version__ variable in fedex_integration/__init__.py
from fedex_integration import __version__ as version

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')


setup(
	name='fedex_integration',
	version=version,
	description='fedex_integration',
	author='fedex_integration',
	author_email='fedex_integration',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
