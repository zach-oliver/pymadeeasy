"""
Created on 04/14/19
@author: zach-oliver

The purpose of this file is to unit test the operating_system_functions.py file
"""

import operating_system_functions as os
import print_functions as p


def test_operating_system_functions():
    p.print_message_highlighted('TESTING OPERATING_SYSTEM_FUNCTIONS.PY')
    print("This should be the exact time now as a string: %s" % os.get_current_date_time(as_string=True))
    os.run_command('ls -la')
    print("Above should be the list of files in the current directory: run_command test")
    print(os.convert_string_to_url("I can't get no satisfaction!"))
    print("Above should be: I-cant-get-no-satisfaction: convert_string_to_url test")
    test_string = "This is my tweet http://example.com/blah check it out"
    print(test_string)
    print(os.find_url_in_string(test_string))
    print("Above should be the URL in the statement above it")
    print("The current working directory is %s" % os.get_current_working_directory())
    print("It correctly returned a string: %s" % str(os.check_variable_type(os.get_current_working_directory(), str)))


test_operating_system_functions()
