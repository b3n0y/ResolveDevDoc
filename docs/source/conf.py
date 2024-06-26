# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'ResolveDevDoc'
copyright = '2024, b3n0y'
author = 'Benoit Breault'

release = '0.1'
version = '0.2.0'

# -- General configuration
master_doc = 'index'

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
pygments_style = 'sphinx'

# -- Options for EPUB output
epub_show_urls = 'footnote'
