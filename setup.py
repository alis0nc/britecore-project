from setuptools import setup

setup(
    name='britecoreproject',
    packages=['britecoreproject'],
    include_package_data=True,
    install_requires=[
        'flask',
        'sqlobject',
    ],
)
