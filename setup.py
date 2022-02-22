"""Install packages as defined in this file into the Python environment."""
from setuptools import setup, find_namespace_packages

setup(
    name="slowburn",
    author="Matthew Cotton",
    author_email="matthewcotton.cs@gmail.com",
    url="https://github.com/MattCCS/SlowBurn",
    description="Tools for caching long-running or intermittent process results",
    version="0.0.1",
    # package_dir={"": "slowburn"},
    # packages=find_namespace_packages(where="slowburn", exclude=["tests"]),
    packages=["slowburn"],
    include_package_data=True,
    # package_data={"slowburn": ["slowburn/*"]},
    install_requires=[
        "setuptools>=45.0",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.0",
        "Topic :: Utilities",
    ],
)
