"""
Created on 04/14/19
@author: zach-oliver

The purpose of this file is to unit test the operating_system_functions.py file
"""

from operating_system_functions import get_current_date_time, get_current_time
from print_functions import print_message_highlighted


def test_operating_system_functions():
    print_message_highlighted('TESTING OPERATING_SYSTEM_FUNCTIONS.PY')
    print("This should be the exact time now as a string: %s" % get_current_date_time(as_string=True))
