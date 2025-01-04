from setuptools import setup
from setuptools import find_packages

setup(
    package_dir={"": "libraries"},
    packages=find_packages(
        where=["libraries"],
        include=["lxmimageproc"],
    ),
)
