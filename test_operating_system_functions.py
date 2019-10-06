"""
Created on 04/14/19
@author: zach-oliver

The purpose of this file is to unit test the operating_system_functions.py file
"""

import operating_system_functions as os
import print_functions as p


def test_operating_system_functions():
    p.print_message_highlighted('TESTING OPERATING_SYSTEM_FUNCTIONS.PY')
    p.print_str("This should be the exact time now as a string: %s" % os.get_current_date_time(as_string=True))
    os.run_command('ls -la')
    p.print_str("Above should be the list of files in the current directory: run_command test")
    p.print_str(os.convert_string_to_url("I can't get no satisfaction!"))
    p.print_str("Above should be: I-cant-get-no-satisfaction: convert_string_to_url test")
    test_string = "This is my tweet http://example.com/blah check it out"
    p.print_str(test_string)
    p.print_str(os.find_url_in_string(test_string))
    p.print_str("Above should be the URL in the statement above it")
    p.print_str("The current working directory is %s" % os.get_current_working_directory())
    p.print_str("It correctly returned a string: %s"
                % str(os.check_variable_type(os.get_current_working_directory(), str)))


test_operating_system_functions()
