
from setuptools import setup

setup(
    name='book_list',
    description='Simple book list app with REST API',
    version='0.1.0',
    author='Timothy McPhillips',
    author_email='tmcphillips@absoluteflow.org',
    url='https://github.com/tmcphillips/flask-demos',
    license='MIT',
    packages=['book_list'],
    package_dir={'': 'src'},
    data_files = [("", ["LICENSE.txt"])],
    install_requires=['Flask >= 1.0.2']
)