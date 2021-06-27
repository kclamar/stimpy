from setuptools import setup

packages = ["stimpy", "stimpy.animate"]

package_data = {"": ["*"]}

install_requires = ["PsychoPy>=2021.2.0,<2022.0.0", "numpy>=1.21.0,<2.0.0"]

extras_require = {
    "dev": [
        "black",
        "isort",
        "flake8",
        "mypy",
        "pydata-sphinx-theme",
        "sphinx",
        "sphinx-autodoc-typehints",
    ]
}

with open("README.md", "r") as fh:
    long_description = fh.read()

setup_kwargs = {
    "name": "stimpy",
    "version": "0.1.0",
    "description": "A PsychoPy wrapper to create moving visual stimuli without"
    " loops.",
    "long_description": long_description,
    "author": "Ka Chung Lam",
    "author_email": "kclamar@connect.ust.hk",
    "maintainer": None,
    "maintainer_email": None,
    "url": "https://github.com/kclamar/stimpy",
    "packages": packages,
    "package_data": package_data,
    "install_requires": install_requires,
    "extras_require": extras_require,
    "python_requires": ">=3.8,<4.0",
}


setup(**setup_kwargs)
