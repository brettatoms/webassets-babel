#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'webassets',
]

test_requirements = [
    'mock',
]

setup(
    name='webassets-babel',
    version='0.2.0',
    description="Babel filter for Webassets",
    long_description=readme + '\n\n' + history,
    author="Taras Lyapun",
    author_email='taraslyapun@gmail.com',
    url='https://github.com/lyapun/webassets-babel',
    packages=[
        'webassets_babel',
    ],
    package_dir={'webassets_babel':
                 'webassets_babel'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='webassets babel',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
