# -*- coding: utf-8 -*-
#
# CVXPY documentation build configuration file, created by
# sphinx-quickstart on Mon Jan 27 20:47:07 2014.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# To import CVXPY:
sys.path.insert(0, os.path.abspath('../..'))
# To import sphinx extensions we've put in the repository:
sys.path.insert(0, os.path.abspath('../sphinxext'))

import cvxpy

__version__ = cvxpy.__version__

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinxcontrib.jquery',
    'sphinx.ext.autosectionlabel',
    'sphinx_inline_tabs',
    'sphinx_design',
    'sphinx_immaterial',
]

# To suppress autodoc/numpydoc warning.
# http://stackoverflow.com/questions/12206334/sphinx-autosummary-toctree-contains-reference-to-nonexisting-document-warnings
numpydoc_show_class_members = False


# Since readthedocs.org has trouble compiling `cvxopt`, autodoc fails
# whenever it tries to import a CVXPY module to document it.
# The following code replaces the relevant cvxopt modules with
# a dummy namespace, allowing autodoc to work.
class Mocked:
    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __getattr__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]
        else:
            return None

MOCK_MODULES = ['cvxopt', 'cvxopt.base', 'cvxopt.misc']
sys.modules.update((mod_name, Mocked()) for mod_name in MOCK_MODULES)

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'CVXPY'
copyright = u'The CVXPY authors'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '.'.join(__version__.split('.')[:2])
# The full version, including alpha/beta/rc tags.
release = __version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
import alabaster

table_styling_embed_css = False

html_theme_path = [alabaster.get_path(), "../themes"]
extensions += ['alabaster']
html_theme = 'sphinx_immaterial'
# Note: the version selector could be omitted for local builds.
# See https://github.com/cvxpy/cvxpy/pull/1624#discussion_r795207339 for a discussion on the topic
html_sidebars = {
   '**': [
       'about.html', 'navigation.html', 'searchbox.html', 'version_selector.html',
   ]
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "palette": {"scheme": "default"},

    "features": [
        "header.autohide",
        # "toc.integrate",  # enable/disable right sidebar
        "toc.follow",
        # "toc.sticky",
        "navigation.path",  # breadcrumbs, not yet available.
        # "navigation.sections",  # top-level sections are rendered as groups in the sidebar for viewports above 1220px; not compatible with tabs below.
        "navigation.instant",
        # clicks on all internal links will be intercepted and dispatched via XHR without fully reloading the page
        "navigation.top",
        # back-to-top button can be shown when the user, after scrolling down, starts to scroll up again. It's rendered centered and just below the header; not yet available.
        "navigation.tabs",
        # top-level sections are rendered in a menu layer below the header for viewports above 1220px, but remain as-is on mobile
        "navigation.tabs.sticky",
        # navigation tabs will lock below the header and always remain visible when scrolling down
        "navigation.tracking",  # the URL in the address bar is automatically updated with the active anchor
        "navigation.expand",
        # the left sidebar will expand all collapsible subsections by default, so the user doesn't have to open subsections manually
        "search.highlight",
        # a user clicks on a search result, Material for MkDocs will highlight all occurrences after following the link
        "search.share",
        # a  share button is rendered next to the reset button, which allows to deep link to the current search query and result
        "content.tabs.link",
        "announce.dismiss",
    ],

    "toc_title": "On this page",
    "site_url": "https://www.cvxpy.org/",
    "repo_url": "https://github.com/cvxpy/cvxpy/",
    "repo_name": "CVXPY",
    "icon": {
        "repo": "fontawesome/brands/github",
    },
    "analytics": {
        "provider": "google",
        "property": "UA-50248335-1",
    },

    # version_dropdown
    "version_dropdown": True,
    "version_info": [
        {
            "version": "https://www.cvxpy.org",
            "title": "latest",
            "aliases": [],
        },
        {
            "version": "https://www.cvxpy.org/version/1.7",
            "title": "1.7",
            "aliases": [],
        },
        {
            "version": "https://www.cvxpy.org/version/1.6",
            "title": "1.6",
            "aliases": [],
        },
        {
            "version": "https://www.cvxpy.org/version/1.5",
            "title": "1.5",
            "aliases": [],
        },
        {
            "version": "https://www.cvxpy.org/version/1.4",
            "title": "1.4",
            "aliases": [],
        },
    ],

    # social icons
    "social": [
        {
            "icon": "fontawesome/brands/github",
            "link": "https://github.com/cvxpy/cvxpy",
            "name": "Source on github.com",
        },
        {
            "icon": "fontawesome/brands/python",
            "link": "https://pypi.org/project/cvxpy/",
        },
    ],
}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = ['../themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = f'CVXPY {version} documentation'
html_title = ""  # we are using a logo.

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/cvxpy-wordmark-light.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = [
    'css/styling.css',
    'https://cdn.datatables.net/2.1.8/css/dataTables.dataTables.css',
]
html_js_files = [
    'https://cdn.datatables.net/2.1.8/js/dataTables.js',
]
# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'cvxpydoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'cvxpy.tex', u'CVXPY Documentation',
   u'Steven Diamond, Eric Chu, Stephen Boyd', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'cvxpy', u'CVXPY Documentation',
     [u'Steven Diamond, Eric Chu, Stephen Boyd'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'cvxpy', u'CVXPY Documentation',
   u'Steven Diamond, Eric Chu, Stephen Boyd', 'CVXPY', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}
