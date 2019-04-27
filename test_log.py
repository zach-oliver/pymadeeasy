"""
Created on 04/27/19
@author: zach-oliver

The purpose of this file is to unit test the Log.py file
"""

from Log import Log
from operating_system_functions import get_current_date_time


def test_log():

    dict_log_config = dict(str_filename='test_log.py', bool_debug=True, str_log_directory='log/',
                           str_function='test_log', str_separator='|:|')

    print(dict_log_config)

    this_log = Log(**dict_log_config)

    this_log.append(get_current_date_time(as_string=True))




test_log()
