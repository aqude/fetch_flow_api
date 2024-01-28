#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="fetch_flow_api",
    author_email='tovpeko03dev@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="FetchFlowApi is a Python package designed to simplify the process of extracting and handling data from various APIs. This tool is ideal for developers and data analysts who regularly interact with web APIs to gather data.",
    entry_points={
        'console_scripts': [
            'fetch_flow_api=fetch_flow_api.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='fetch_flow_api',
    name='fetch_flow_api',
    packages=find_packages(include=['fetch_flow_api', 'fetch_flow_api.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/aqude/fetch_flow_api',
    version='0.1.0',
    zip_safe=False,
)
