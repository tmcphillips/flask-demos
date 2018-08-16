
from setuptools import setup

setup(
    name='hello_world_rest_api',
    description='Mimimal hello world app with REST API',
    version='0.1.2',
    author='Timothy McPhillips',
    author_email='tmcphillips@absoluteflow.org',
    url='https://github.com/tmcphillips/flask-demos',
    license='MIT',
    packages=['hello_world_rest_api'],
    package_dir={'': 'src'},
    data_files = [("", ["LICENSE.txt"])],
    install_requires=['Flask >= 1.0.2']
)