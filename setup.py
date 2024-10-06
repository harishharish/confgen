# setup.py

from setuptools import setup

setup(
    name='cli',  # The name of your CLI tool
    version='0.1',
    py_modules=['cli'],
    install_requires=[
        'typer',  # Include any dependencies your project needs
    ],
    entry_points='''
        [console_scripts]
        cli=cli:main
    ''',
)