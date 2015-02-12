import cybox

project = u'python-cybox'
copyright = u'2015, The MITRE Corporation'
version = cybox.__version__
release = version

extensions = [
    'sphinx.ext.autodoc',
    'cybox.utils.autoentity',
    'sphinx.ext.doctest',
    'sphinx.ext.ifconfig',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinxcontrib.napoleon',
]

intersphinx_mapping = {'http://docs.python.org/': None}

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

rst_prolog = """
.. warning::

    This documentation is still a work in progress. If you have any issues or
    questions, please ask on the cybox-discussion mailing list or file a bug
    in our `issue tracker`_.

.. _issue tracker: https://github.com/CybOXProject/python-cybox/issues
"""

exclude_patterns = ['_build']
pygments_style = 'sphinx'

html_theme = 'default'
html_style = '/default.css'
html_static_path = ['_static']
htmlhelp_basename = 'python-cyboxdoc'

html_theme_options = {
    'codebgcolor': '#EEE',
    'footerbgcolor': '#FFF',
    'footertextcolor': '#36C',
    'headbgcolor': '#DEF',
    'headtextcolor': '#36C',
    'headlinkcolor': '#69F',
    'linkcolor': '#69F',
    'relbarbgcolor': '#36C',
    'relbartextcolor': '#69F',
    'sidebarbgcolor': '#EEE',
    'sidebarlinkcolor': '#36C',
    'sidebartextcolor': '#000',
    'visitedlinkcolor': '#69F',
}
html_sidebars = {"**": ['localtoc.html', 'relations.html', 'sourcelink.html',
'searchbox.html', 'links.html']}

latex_elements = {}
latex_documents = [
  ('index', 'python-cybox.tex', u'python-cybox Documentation',
   u'The MITRE Corporation', 'manual'),
]
