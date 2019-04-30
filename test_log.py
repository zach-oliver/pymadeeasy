"""
Created on 04/27/19
@author: zach-oliver

The purpose of this file is to unit test the Log.py file
"""

from Log import Log
from print_functions import print_message_highlighted


def test_log():
    print_message_highlighted('TESTING LOG.PY')
    dict_log_config = dict(str_filename='test_log.py', bool_debug=True, str_log_directory='log/',
                           str_function='test_log', str_separator='|:|')

    print(dict_log_config)

    this_log = Log(**dict_log_config)

    this_log.append('START')

    this_log.change_debug(False)
    this_log.append('DEBUG=False SHOULD NOT SEE THIS IN CONSOLE')
    this_log.change_debug(True)
    this_log.append('DEBUG=True OUTPUT BACK TO CONSOLE')

    this_log.change_function('testing_test_log')
    this_log.append('<==testing_test_log')
    this_log.change_function('test_log')
    this_log.append('<==test_log')

    this_log.change_filename('testing_filename_test_log.py')
    this_log.append('FILENAME CHANGE')
    this_log.change_filename('test_log.py')

    this_log.append('FINISH')
