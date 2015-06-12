#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
utils
------------------------------
Tools for python Resel scripts

"""

__docformat__ = 'restructuredtext en'

def read_file(filename):
    """ read a file.
    """
    with open(filename, 'rb') as my_file:
        return my_file.readlines()
 
# vim:set et sts=4 ts=4 tw=80:
