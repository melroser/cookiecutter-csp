#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""main2

Usage:
  csputil2 ship new <name>...
  csputil2 ship <name> move <x> <y> [--speed=<kn>]
  csputil2 ship shoot <x> <y>
  csputil2 mine (set|remove) <x> <y> [--moored|--drifting]
  csputil2 -h | --help
  csputil2 --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.
"""

from __future__ import unicode_literals, print_function
from docopt import docopt

import csputil

PROG_NAME = 'csputil'
VERSION = csputil.__version__
DESCRIPTION = 'CSP utility package for developers.'
AUTHOR = csputil.__author__
AUTHOR_MAIL = csputil.__email__

def main():
    """Main entry point for the main2 CLI."""
    args = docopt(__doc__, version=VERSION)
    print(args)

if __name__ == "__main__":
    main()
