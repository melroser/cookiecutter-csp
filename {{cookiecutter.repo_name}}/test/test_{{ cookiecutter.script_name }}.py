#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_csputil
----------------------------------

Tests for `csputil` module.
"""
import pytest

from csputil import application as app

def test_csputil():
    assert app.app_opp()

if __name__ == '__main__':
    pytest.main(__file__)
