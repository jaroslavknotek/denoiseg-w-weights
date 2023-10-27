#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='denoisegweight',
    version='0.1',
    description='DenoiSeg + weightmaps',
    author='Jaroslav Knotek',
    author_email='knotekjaroslav@email.cz',
    url='https://github.com/jaroslavknotek/refuel',
#    entry_points = {
#        'console_scripts': ['dswcli=dsw.command_line:cli'],
#    },
    packages=find_packages(),
    package_data={"":["*.h5","*.json","*.pt"]},
    python_requires='>=3.10',
    include_package_data=True,
    install_requires=[
        'numpy',
        'torch'
    ]
)
