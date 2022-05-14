# encoding:utf-8
from setuptools import find_packages, setup

from pkg import init

setup(
    name="Mksci",
    version=init.__version__,
    description="Project Managing Tools",
    author="SongshGeo",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    platforms="any",
    install_requires=["requests", "docopt>=0.6.2"],
    entry_points={"console_scripts": ["mksci = pkg.mksci:cli"]},
)
