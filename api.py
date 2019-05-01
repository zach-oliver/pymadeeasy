"""
Created on 04/29/19
@author: zach-oliver
"""

# https://2.python-requests.org//en/master/#
import requests


def get_api_response(str_uri='', str_username='', str_password=''):
    response = requests.get(str_uri, auth=(str_username, str_password))
    return response


dict_http_status_codes = {
    # https://www.restapitutorial.com/httpstatuscodes.html
    100: 'Continue',
    101: 'Switching Protocols',
    102: 'Processing',
    103: 'Early Hints',
    200: 'OK',
    201: 'Created',
    202: 'Accepted',
    203: 'Non-Authoritative Information',
    204: 'No Content',
    205: 'Reset Content',
    206: 'Partial Content',
    207: 'Multi-Status',
    208: 'Already Reported',
    300: 'Multiple Choices',
    301: 'Moved Permanently',
    304: 'Not Modified',
    400: 'Bad Request',
    401: 'Unauthorized',
    402: 'Payment Required',
    403: 'Forbidden',
    404: 'Not Found',
    409: 'Conflict',
    500: 'Internal Server Error'
}


class API:

    def __init__(self, str_url='https://httpbin.org/ip', str_username='', str_password=''):
        """Initialize the API class object

        UNIT TESTED

        This class is a wrapper around the requests package for Python. It creates an object out
        of the response back from the request so you can specify attributes coming back from that
        response after they are processed. This means that useful information is simply an
        attribute away...in theory.

        Args:
            str_url: A string used as the URL you are making a request to
            str_username: A string used to optionally set the username for the request
            str_password: A string used to optionally set the password for the request

        Returns:
            An API class object with the below attributes available

        Raises:
            None

        Attributes:
            self.response: The original response object from the requests package
            self.status_str: A string containing the description of the HTTP status code
            self.header_dict: A dictionary including the header details
            self.header_dict_is_dict_bool: A boolean used to represent if the header was actually converted into a
                dictionary. If false, the header has an un-recognized format and you must parse yourself
            self.response_str: The string version of the response from the the request
            self.response_str_is_str_bool: A boolean used to represent if the request was actually converted into a
                string. If false, the response has an un-recognized format and you must parse yourself
            self.response_dict: The dictionary version of the response from the the request
            self.response_dict_is_dict_bool: A boolean used to represent if the request was actually converted into a
                dictionary. If false, the response has an un-recognized format and you must parse yourself

        """
        self.response = requests.get(str_url, auth=(str_username, str_password))
        self.status_str = dict_http_status_codes[self.response.status_code]
        # Converting a request.structures.CaseInsensitiveDict to a regular dict
        # https://stackoverflow.com/questions/24533018/get-a-header-with-python-and-convert-in-json-requests-urllib2-json
        self.header_dict = self.response.headers.__dict__
        # https://codeyarns.com/2010/01/28/python-checking-type-of-variable/
        self.header_dict_is_dict_bool = isinstance(self.header_dict, dict)
        self.response_str = str(self.response.text)
        self.response_str_is_str_bool = isinstance(self.response_str, str)
        self.response_dict = dict(self.response.json())
        self.response_dict_is_dict_bool = isinstance(self.response_dict, dict)

        if self.header_dict_is_dict_bool:
            pass
        else:
            print('Warning: API header is not loaded into dictionary')

        if self.response_str_is_str_bool:
            pass
        else:
            print('Warning: API response is not a string')

        if self.response_dict_is_dict_bool:
            pass
        else:
            print('ERROR: UNRECOGNIZED API RESPONSE TYPE')
            print(f'RESPONSE: {self.status_str}')
            print(self.response_dict)

    def __str__(self):
        # https://realpython.com/python-f-strings/
        # https://medium.com/@NirantK/best-of-python3-6-f-strings-41f9154983e
        field_width_int = 15
        type_width_int = 6

        fstr_output = f"""
{'API CLASS OBJECT DETAILS':>30}
{'Field':>{field_width_int}}|{'Type':^{type_width_int}}|Details
-------------------------------
{'Status Code':>{field_width_int}}|{'int':^{type_width_int}}|{self.response.status_code} is {self.status_str}
-------------------------------
{'Header':>{field_width_int}}|{'dict':^{type_width_int}}|{self.header_dict}
-------------------------------
{'Response':>{field_width_int}}|{'str':^{type_width_int}}|{self.response_str}
-------------------------------
{'Response':>{field_width_int}}|{'dict':^{type_width_int}}|{self.response_dict}"""
        return fstr_output
