
from setuptools import setup, find_packages

setup(
    name='hello_world_rest_api',
    packages=find_packages(where='src'),
    package_dir={'': 'src'}
)