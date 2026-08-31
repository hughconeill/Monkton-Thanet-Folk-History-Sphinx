# Configuration file for the Sphinx documentation builder.
# For a full list of options: https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = "The History of Monkton"
copyright = "2026, Monkton Local History Project"
author = "Monkton Local History Project"
release = "0.1"

# -- General configuration ----------------------------------------------------

extensions = [
    "myst_parser",           # Markdown support
    "sphinx_copybutton",     # Adds a "copy" button to code blocks
    "sphinx_design",         # Cards, tabs, grids, dropdowns, badges
]

# Let Sphinx build from both .rst and .md files
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# MyST Markdown extensions - these turn on extra Markdown syntax
myst_enable_extensions = [
    "colon_fence",      # ::: fenced directives (cleaner than ```{})
    "deflist",           # Definition lists
    "linkify",            # Auto-link bare URLs
    "substitution",      # {{ variable }} substitutions
    "tasklist",           # - [ ] checkboxes
    "attrs_inline",      # {.class} attributes on inline elements
    "attrs_block",       # {.class} attributes on the preceding block (e.g. tables)
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_css_files = ["custom.css"]

# -- Options for HTML output ---------------------------------------------------

html_theme = "furo"
html_static_path = ["_static"]
html_title = "The History of Monkton"

# Furo theme options
html_theme_options = {
    "sidebar_hide_name": False,
    "light_css_variables": {
        "color-brand-primary": "#7a2e3a",
        "color-brand-content": "#7a2e3a",
        "color-background-primary": "#faf7f3",
        "color-background-secondary": "#f0eae2",
        "color-background-border": "#e0d6c9",
        "color-sidebar-background": "#efe7dc",
        "color-table-row-alt": "#f0e9e0",
        "color-card-background": "#efe7dc",
        "color-card-border": "#b08a8f",
        "color-code-background": "#f2ede6",
    },
    "dark_css_variables": {
        "color-brand-primary": "#d68490",
        "color-brand-content": "#d68490",
        "color-background-primary": "#1b1714",
        "color-background-secondary": "#242019",
        "color-background-border": "#3a332a",
        "color-sidebar-background": "#1f1a16",
        "color-table-row-alt": "#262019",
        "color-card-background": "#1f1a16",
        "color-card-border": "#7a5258",
        "color-code-background": "#211c17",
    },
    # Uncomment and edit if you have a repo:
    # "source_repository": "https://github.com/yourname/yourrepo/",
    # "source_branch": "main",
    # "source_directory": "docs/source/",
}

# Optional: add your own logo/favicon by dropping files in _static/
html_logo = "_static/logo_trans_red.png"
html_favicon = "_static/monkton_coa.ico"
