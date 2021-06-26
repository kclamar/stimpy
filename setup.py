import codecs
import os.path

from setuptools import find_packages, setup


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="stimpy",
    version=get_version("stimpy/__init__.py"),
    packages=find_packages(),
    url="https://github.com/kclamar/stimpy",
    author="Ka Chung Lam",
    author_email="kclamar@connect.ust.hk",
    description="A PsychoPy wrapper to create moving visual stimuli without "
    "loops.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Intended Audience :: Science/Research",
    ],
    install_requires=[
        "numpy",
        "psychopy",
    ],
    extras_require={
        "dev": [
            "black",
            "isort",
            "flake8",
            "mypy",
            "pydata-sphinx-theme",
            "sphinx",
            "sphinx-autodoc-typehints",
        ]
    },
    python_requires=">=3.8",
)
