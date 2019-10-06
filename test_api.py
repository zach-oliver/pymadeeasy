"""
Created on 04/29/19
@author: zach-oliver
"""

import api
import print_functions as p
import Log
import operating_system_functions as os


def test_get_api(str_uri = 'https://httpbin.org/get'):
    p.print_message_highlighted('TESTING API.PY')
    dict_log_config = dict(str_filename='test_api.py', bool_debug=True, str_log_directory='log/',
                           str_function='test_api', str_separator='|:|')
    this_log = Log.Log(**dict_log_config)
    this_log.append('START')
    this_log.append(str_uri)

    this_log.append('Testing get_api_response function')
    response = api.get_api_response(str_uri)

    field_width_int = 15
    type_width_int = 6

    if response.status_code != 200:
        fstr_output = f"""
----------------------------------------------
{'API FUNCTION RESPONSE DETAILS':>30}
{'FIELD':>{field_width_int}}|{'TYPE':^{type_width_int}}|DETAILS
----------------------------------------------
{'Status Code':>{field_width_int}}|{'int':^{type_width_int}}|{response.status_code}
----------------------------------------------
{'Header':>{field_width_int}}|{'dict':^{type_width_int}}|{response.headers}
----------------------------------------------
{'History':>{field_width_int}}|{'str':^{type_width_int}}|{response.history}
----------------------------------------------
{'Response':>{field_width_int}}|{'str':^{type_width_int}}|{response.text}
----------------------------------------------
{'Response':>{field_width_int}}|{'dict':^{type_width_int}}|{str('')}"""
    else:
        fstr_output = f"""
----------------------------------------------
{'API FUNCTION RESPONSE DETAILS':>30}
{'FIELD':>{field_width_int}}|{'TYPE':^{type_width_int}}|DETAILS
-----------------------------------------------
{'Status Code':>{field_width_int}}|{'int':^{type_width_int}}|{response.status_code}
----------------------------------------------
{'Header':>{field_width_int}}|{'dict':^{type_width_int}}|{response.headers}
----------------------------------------------
{'History':>{field_width_int}}|{'str':^{type_width_int}}|{response.history}
----------------------------------------------
{'Response':>{field_width_int}}|{'str':^{type_width_int}}|{response.text}
----------------------------------------------
{'Response':>{field_width_int}}|{'dict':^{type_width_int}}|{str(response.json())}"""
    this_log.append(fstr_output)

    if response.status_code == 200:
        pass
    else:
        this_log.append('get_api_response function FAILED')

    this_log.append('Testing API class')
    response_class = api.APIResponse(str_url=str_uri)
    response_class.get()
    this_log.append(f'{response_class}')
    if response_class.status_str == 'OK':
        this_log.append('FINISH')
        return
    else:
        p.print_str('API ERROR: Check logs!')
        print


# https://www.howtogeek.com/269509/how-to-run-two-or-more-terminal-commands-at-once-in-linux/
def test_create_lambda_with_api_trigger():
    output_str = os.run_command('cd lambda_with_api_trigger; rm -rf vendor/pymadeeasy; git clone https://github.com/zach-oliver/pymadeeasy.git vendor/pymadeeasy/; chalice deploy', bool_output=True)
    output_str = 'lambda_with_api_trigger/' + output_str
    output_str = os.read_file(output_str, bool_no_lines=True)
    output_str = os.find_url_in_string(output_str)
    return output_str


def test_delete_lambda_with_api_trigger():
    os.run_command('cd lambda_with_api_trigger; chalice delete --stage dev', bool_output=True)


def test_create_lambda_with_timer_trigger():
    output_str = os.run_command('cd lambda_with_timer_trigger; rm -rf vendor/pymadeeasy; git clone https://github.com/zach-oliver/pymadeeasy.git vendor/pymadeeasy/; chalice deploy', bool_output=True)
    output_str = 'lambda_with_timer_trigger/' + output_str
    output_str = os.read_file(output_str, bool_no_lines=True)
    output_str = os.find_url_in_string(output_str)
    return output_str


def test_delete_lambda_with_timer_trigger():
    os.run_command('cd lambda_with_timer_trigger; chalice delete --stage dev', bool_output=True)


def test_api():
    test_get_api()
    test_get_api(str_uri='https://httpbin.org/status/404')


    test_api_str = test_create_lambda_with_api_trigger()
    os.wait(10)
    # Optional test at root
    # test_get_api(str_uri=test_api_str)
    test_api_str2 = test_api_str + 'hello/alana'
    test_get_api(str_uri=test_api_str2)
    test_delete_lambda_with_api_trigger()

    test_create_lambda_with_timer_trigger()
    os.wait(10)
    test_delete_lambda_with_timer_trigger()
