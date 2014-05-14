#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

import {{ cookiecutter.project_name }}

PUBLISH_CMD = "python setup.py register sdist upload"
TEST_PUBLISH_CMD = 'python setup.py register -r test sdist upload -r test'
TEST_CMD = 'nosetests'

if 'publish' in sys.argv:
    status = subprocess.call(PUBLISH_CMD, shell=True)
    sys.exit(status)

if 'publish_test' in sys.argv:
    status = subprocess.call(TEST_PUBLISH_CMD, shell=True)
    sys.exit()

if 'run_tests' in sys.argv:
    try:
        __import__('nose')
    except ImportError:
        print('nose required. Run `pip install nose`.')
        sys.exit(1)
    status = subprocess.call(TEST_CMD, shell=True)
    sys.exit(status)

def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content

# remember __init__.py
VERSION = {{ cookiecutter.script_name }}.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.md').read()
#history = open('HISTORY.rst').read().replace('.. :changelog:', '')

with open('requirements.txt') as f:
    requires = [line for line in f.readlines()]


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='{{ cookiecutter.script_name }}',
    #version=VERSION,
    description='CSP utility package for developers.',
    long_description=readme,
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='{{ cookiecutter.repo_url }}',
    packages=[
        '{{ cookiecutter.project_name }}',
    ],
    package_dir={'{{ cookiecutter.project_name }}': '{{ cookiecutter.project_name }}'},
    include_package_data=True,
    install_requires=requires,
    cmdclass={'test': PyTest,},
    tests_require=['pytest', 'nose'],
    extras_require={
        'testing': ['pytest',],
    },
    license="BSD",
    zip_safe=False,
    keywords='{{ cookiecutter.project_name }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.script_name }} = {{ cookiecutter.project_name }}.main:main',
            '{{ cookiecutter.script_name }}2 = {{ cookiecutter.script_name }}.main2:main',
        ],
    }
)
