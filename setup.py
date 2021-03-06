# coding=utf-8

from setuptools import setup, find_packages


def parse_requirements(filename='requirements.txt'):
    """ load requirements from a pip requirements file. (replacing from pip.req import parse_requirements)"""
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


setup(
    name='pocounit',
    version='1.0.40',
    keywords="PocoUnit unittest",
    description='Unittest framework for poco and airtest',
    packages=find_packages(),
    include_package_data=True,
    install_requires=parse_requirements(),
    license='Apache License 2.0',
)
