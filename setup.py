from setuptools import setup

setup(
    name='stalker',
    version='0.1.0',
    packages=['stalker'],
    entry_points={
        'console_scripts': [
            'stalker = stalker.__main__:main'
        ]
    })
