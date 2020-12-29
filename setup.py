from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='yamljinja',
    version='2020.12.1',
    author='tahini-dev',
    author_email='tahini.dev@gmail.com',
    description='Python package for yaml and jinja together',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/tahini-dev/yamljinja',
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'pyyaml',
        'jinja2'
    ],
    python_requires='>=3.7',
    include_package_data=True,
)
