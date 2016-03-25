#!/usr/bin/env python3
# Copyright (C) 2016 Sebastian Wiesner and Flycheck contributors

# This file is not part of GNU Emacs.

# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.

# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.

import re
from pathlib import Path

# Require Sphinx 1.0
needs_sphinx = '1.0'
extensions = ['sphinx.ext.extlinks']

# Project metadata
project = 'Flycheck'
copyright = '2014-2016, Sebastian Wiesner and Flycheck contributors'
author = 'Sebastian Wiesner'


def read_version():
    """Extract version number from ``flycheck.el`` and return it as string."""
    version_pattern = re.compile(r'Version:\s+(\d.+)$')
    flycheck_el = Path(__file__).parent.parent.joinpath('flycheck.el')
    for line in flycheck_el.open(encoding='utf-8'):
        match = version_pattern.search(line)
        if match:
            return match.group(1)

release = read_version()
version = '.'.join(release.split('.')[:2])

# Source settings
source_suffix = '.rst'
master_doc = 'index'

# Build settings
exclude_patterns = ['_build']
# TODO: Choose a default role
#default_role = None

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# HTML settings
html_theme = 'alabaster'
html_theme_options = {
    'logo': 'logo.png',
    'logo_name': False,
    'description': 'Syntax checking for GNU Emacs',
    'github_user': 'flycheck',
    'github_repo': 'flycheck',
    'github_banner': True,
}
html_sidebars = {
    'index': [
        'about.html',
        'localtoc.html',
        'relations.html',
        'searchbox.html',
    ],
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
    ]
}
html_static_path = ['_static']
html_favicon = '_static/favicon.png'

# Ignore localhost when checking links
linkcheck_ignore = [r'http://localhost:\d+/']

extlinks = {
    'gh': ('https://github.com/%s', ''),
    'flyc': ('https://github.com/flycheck/%s', '')
}
