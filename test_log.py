"""
Created on 04/27/19
@author: zach-oliver

The purpose of this file is to unit test the Log.py file
"""

import Log
import print_functions as p


def test_log():
    p.print_message_highlighted('TESTING LOG.PY')
    dict_log_config = dict(str_filename='test_log.py', bool_debug=True, str_log_directory='log/',
                           str_function='test_log')

    p.print_str(str(dict_log_config))

    this_log = Log.Log(**dict_log_config)

    this_log.start()

    this_log.change_debug(False)
    this_log.append('DEBUG=False SHOULD NOT SEE THIS IN CONSOLE')
    this_log.change_debug(True)
    this_log.append('DEBUG=True OUTPUT BACK TO CONSOLE')
    assert this_log.debug, "PYMADEEASY LOG FAIL! The Log debug did not change to True!"

    temp_function_change_str = 'testing_test_log'
    this_log.change_function(temp_function_change_str)
    this_log.append('<==testing_test_log')
    assert this_log.function == temp_function_change_str, "PYMADEEASY LOG FAIL! The Log function name was not changed!"

    temp_function_change_str = 'test_log'
    this_log.change_function(temp_function_change_str)
    this_log.append('<==test_log')
    assert this_log.function == temp_function_change_str, "PYMADEEASY LOG FAIL! The Log function was not changed!"

    this_log.change_filename('testing_filename_test_log.py')
    this_log.append('FILENAME CHANGE')
    temp_file_name_change_str = 'test_log.py'
    this_log.change_filename(temp_file_name_change_str)
    assert this_log.filename == temp_file_name_change_str, "PYMADEEASY LOG FAIL! The Log filename was not changed!"
    this_log.finish()


test_log()
