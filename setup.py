from setuptools import setup
from setuptools import find_packages

setup(
    package_dir={"": "python/libraries"},
    packages=find_packages(
        where=["python/libraries"],
        include=["lxmimageproc"],
    ),
)
