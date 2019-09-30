"""
Created on 04/14/19
@author: zach-oliver

The purpose of this file is to unit test the operating_system_functions.py file
"""

from operating_system_functions import get_current_date_time, run_command, convert_string_to_url, find_url_in_string
from print_functions import print_message_highlighted


def test_operating_system_functions():
    print_message_highlighted('TESTING OPERATING_SYSTEM_FUNCTIONS.PY')
    print("This should be the exact time now as a string: %s" % get_current_date_time(as_string=True))
    run_command('ls -la')
    print("Above should be the list of files in the current directory: run_command test")
    print(convert_string_to_url("I can't get no satisfaction!"))
    print("Above should be: I-cant-get-no-satisfaction: convert_string_to_url test")
    test_string = "This is my tweet http://example.com/blah check it out"
    print(test_string)
    print(find_url_in_string(test_string))
    print("Above should be the URL in the statement above it")


test_operating_system_functions()
