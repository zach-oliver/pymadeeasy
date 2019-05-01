"""
Created on 04/27/19
@author: zach-oliver

The purpose of this file is to unit test all of pymadeeasy
"""

from test_operating_system_functions import test_operating_system_functions
from test_log import test_log
from test_api import test_api


def test_all():
    test_operating_system_functions()
    test_log()
    test_api()


test_all()
