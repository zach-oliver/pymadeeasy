"""
Created on 04/27/19
@author: zach-oliver

The purpose of this file is to unit test all of pymadeeasy
"""

import test_operating_system_functions as test_os
import test_log
import test_api


def test_all():
    test_os.test_operating_system_functions()
    test_log.test_log()
    test_api.test_api()


test_all()
