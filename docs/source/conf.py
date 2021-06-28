# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import importlib.metadata
import os
import sys
from typing import List

project_path = os.path.abspath("../../stimpy")

sys.path.insert(0, project_path)

# -- Project information -----------------------------------------------------

project = "stimpy"
copyright = "2021, Ka Chung Lam"
author = "Ka Chung Lam"

# The full version, including alpha/beta/rc tags
release = importlib.metadata.version(project)


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx_autodoc_typehints",
    "sphinx_panels",
]

panels_add_bootstrap_css = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns: List[str] = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = [
    "css/custom.css",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "psychopy": ("https://www.psychopy.org/", None),
}

html_context = {
    "github_url": "https://github.com",
    "github_user": "kclamar",
    "github_repo": "stimpy",
    "github_version": "master",
    "doc_path": "docs/source",
}

html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/kclamar/stimpy",
            "icon": "fab fa-github-square",
        },
    ],
    "external_links": [
        {"name": "PsychoPy", "url": "https://www.psychopy.org/"},
    ],
    "use_edit_page_button": True,
}

autodoc_mock_imports = ["wx"]
