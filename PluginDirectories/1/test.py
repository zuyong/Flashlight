#!/usr/bin/env python
# coding: utf-8

"""
Test preview return from bundle
Usage: ./test.py jira "jira 12345"
"""

import os
import argparse
from importlib import import_module
import sys


os.chdir(os.path.dirname(os.path.realpath(__file__)))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='test',
        description='Test preview return from bundle'
    )
    parser.add_argument('dir', help='direction without .bundle')
    parser.add_argument('command', help='query in spotlight')
    para = parser.parse_args()
    bundle = para.dir + ".bundle"
    bundle_path = os.getcwd() + "/" + bundle
    sys.path.insert(0, bundle_path)

    os.chdir(bundle_path)

    mod = import_module("plugin")
    results = getattr(mod, "results")
    res = results({u'~query': u'34'}, {})
    print(res)
