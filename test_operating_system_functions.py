"""
Created on 04/14/19
@author: zach-oliver

The purpose of this file is to unit test the operating_system_functions.py file
"""

from operating_system_functions import get_current_date_time


def test_operating_system_functions():
    print("This should be the exact time now as a string: %s" % get_current_date_time(as_string=True))


test_operating_system_functions()