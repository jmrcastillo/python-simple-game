

from setuptools import setup


with open('README.md') as file:
    readme = file.read()

setup(
    name="jibreel",
    version="0.3",
    packages=["jibreel"],
    url="https://testpypi.python.org/legacy/",
    description="My fantasy game",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="jmrcas",
    author_email="jm.cass20@gmail.com"
)
