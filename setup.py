"""Config for setup package client Python."""

import os

from setuptools import setup, find_packages

__version__ = '5.3.5'

TYPE_STUBS = ['*.pyi']


def read_file(fname):
    """Read the given file.

    :param fname: Name of the file to be read
    :return:      Output of the given file
    """
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name='reportportal-client',
    packages=find_packages(exclude=('tests', 'tests.*')),
    package_data={
        'reportportal_client': TYPE_STUBS,
        'reportportal_client.steps': TYPE_STUBS
    },
    version=__version__,
    description='Python client for Report Portal v5.',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    author='Report Portal Team',
    author_email='support@reportportal.io',
    url='https://github.com/reportportal/client-Python',
    download_url=('https://github.com/reportportal/client-Python/'
                  'tarball/%s' % __version__),
    license='Apache 2.0.',
    keywords=['testing', 'reporting', 'reportportal', 'client'],
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires=read_file('requirements.txt').splitlines(),
)
