import os

from setuptools import find_namespace_packages, setup

description = "A collection of general purpose utilities"

try:
    this_path = os.path.dirname(os.path.abspath(__file__))
    fn_readme = os.path.join(this_path, "README.md")
    with open(fn_readme) as fh:
        long_description = fh.read()
except OSError:
    long_description = description

setup(
    name="microlibs",
    version="0.0.0",
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    author="Hardik Ojha",
    author_email="hardikojha@outlook.com",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
)
