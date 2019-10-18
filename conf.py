# -*- coding: utf-8 -*-
#
# PPMS-PDFD documentation build configuration file, created by
# sphinx-quickstart on Tue Dec 12 14:22:39 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import datetime

sys.path.insert(0, os.path.abspath('.'))

from convert import write_open_api_json

API_PATH = os.path.join(os.path.dirname(__file__), '_static/api')

api_definitions = {
    'analytics_tracking_api.json': 'analytics/index.yaml',
    'audience_manager_public_api.json': 'audience_manager/public_api/index.yaml',
    'platform_access_control_authorized_api.json': 'platform/authorized_api/access_control/public_v2.yaml',
    'platform_apps_authorized_api.json': 'platform/authorized_api/apps/public_v2.yaml',
    'platform_meta_sites_authorized_api.json': 'platform/authorized_api/meta_sites/public_v1.yaml',
    'platform_users_authorized_api.json': 'platform/authorized_api/users/public_v2.yaml',
    'platform_user_groups_authorized_api.json': 'platform/authorized_api/user_groups/v1.yaml',
    'audience_manager_authorized_api.json': 'audience_manager/authorized_api/index.yaml',
    'custom_reports_http_api.json': 'custom_reports/http_api/index.yaml'
}


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'
autosectionlabel_prefix_document = True
# General information about the project.
project = u'Piwik PRO Marketing Suite'
copyright = u'{year}, Piwik.pro - Enterprise Analytics and Tag Management Platform'.format(year=datetime.date.today().year)
author = u'Piwik PRO'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'9.0'
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.md']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'PPMS-PDFDdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'PPMS-PDFD.tex', u'Piwik PRO Marketing Suite Documentation',
     u'Piwik PRO', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'Piwik PRO', u'Piwik PRO Marketing Suite Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Piwik PRO Marketing Suite', u'Piwik PRO Marketing Suite Documentation',
     author, 'Piwik PRO', 'One line description of project.',
     'Miscellaneous'),
]



# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']

html_theme = "sphinx_rtd_theme"


html_theme_options = {
    'includehidden': False
}

def setup(app):
    app.add_css_file('css/custom.css')
    app.add_js_file('js/custom.js')
    app.add_js_file('js/redoc.2.0.0-rc.14.min.js')

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}


# OpenAPI (YAML to JSON migration)
for output, input in api_definitions.items():
    with open(os.path.join(API_PATH, output), 'w') as file_handler:
        write_open_api_json(path=input, file_handler=file_handler, version=version)
