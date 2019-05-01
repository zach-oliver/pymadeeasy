"""
Created on 04/29/19
@author: zach-oliver
"""

from api import get_api_response, API
from print_functions import print_message_highlighted
from Log import Log


def test_api():
    print_message_highlighted('TESTING API.PY')
    dict_log_config = dict(str_filename='test_api.py', bool_debug=True, str_log_directory='log/',
                           str_function='test_api', str_separator='|:|')
    this_log = Log(**dict_log_config)
    this_log.append('START')
    str_uri = 'https://httpbin.org/ip'
    this_log.append(str_uri)

    this_log.append('Testing get_api_response function')
    response = get_api_response(str_uri)

    if response.status_code == 200:
        this_log.append('response.status_code:' + str(type(response.status_code)))
        this_log.append('response.headers:' + str(type(response.headers)))
        this_log.append('response.encoding:' + str(response.encoding))
        this_log.append('response.text:' + str(type(response.text)))
        this_log.append('response.json:' + str(type(response.json())))
    else:
        this_log.append('get_api_response function FAILED')

    this_log.append('Testing API class')
    response_class = API()
    this_log.append(f'{response_class}')
    if response_class.status_str == 'OK':
        this_log.append('FINISH')
        return
    else:
        print('API ERROR: Check logs!')


test_api()
