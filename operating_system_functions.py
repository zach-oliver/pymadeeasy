"""
Created on 04/12/19
@author: zach-oliver
"""

import os
import errno
import datetime
import time
import re


def create_folders_along_path(str_path):
    """Creates any folders locally along str_path

    NOT UNIT TESTED

    Retrieves the current date and time one of two ways:
    - As a string object
    - As a datetime object

    Args:
        str_path: A string that has the path you would like to create folders along
        this_log: a Log from Log class defined in pymadeeasy

    Returns:
        None, folders are created along the path provided otherwise error

    Raises:
        OSError: An error occurred accessing the bigtable.Table object.
    """
    # https://stackoverflow.com/questions/12517451/automatically-creating-directories-with-file-output
    # creates the directory and any parent directories if it doesn't exist
    if not os.path.exists(os.path.dirname(str_path)):
        try:
            os.makedirs(os.path.dirname(str_path))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


def get_current_date_time(as_string=False, now_format=''):
    """Gets the current date and time

    UNIT TESTED

    Retrieves the current date and time one of two ways:
    - As a string object
    - As a datetime object

    Args:
        as_string: if False, function returns a datetime object.
            now_format:
                if 'log' then the string returned will be shortened to reduce Log line length.
                if 'file' then the string returned will be a file-compliant version of the date time.

    Returns:
        An example string: 2019-04-27 12:03:21.037656
            log:  10/07/19 Mon 08:33:41PM
            file: 10.07.19.Mon.08.30.25.PM
        or the datetime object

    Raises:
        None
    """
    # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    if as_string:
        if now_format == 'log':
            return str(datetime.datetime.now().strftime('%m/%d/%y %a %I:%M:%S%p'))
        elif now_format == 'file':
            return str(datetime.datetime.now().strftime('%m.%d.%y.%a.%I.%M.%S.%p.'))
        else:
            return str(datetime.datetime.now())
    else:
        return datetime.datetime.now()


def get_current_time():
    """Gets the current date and time

    NOT UNIT TESTED

    Retrieves the current time

    Returns:
        An example time object: 1556510572.392354

    Raises:
        None
    """
    return time.time()


def run_command(str_command, bool_output=False, bool_return_output=False, str_cmd_out_prefix='cmdout',
                str_cmd_out_suffix='.out',):
    """Runs a terminal command in the current working directory

    UNIT TESTED

    Runs the terminal command in the current working directory. If output_bool is True
        it will create a text file with the output from the command

    Args:
        str_command: the string equivalent of the command you
            want to run on the command line / terminal
        bool_output: if True, the command line output will be sent to 'cmdout<timestamp>.txt'
            in the current working directory
        bool_return_output: if True, the output of the command will be returned as a string
        str_cmd_out_prefix: the string prefix on the command output filename
        str_cmd_out_suffix: the string suffix on the command output filename
    Returns:
        the filename of the output file

    Raises:
        None
    """
    if bool_output:
        # https://linuxhandbook.com/execute-shell-command-python/
        out_filename_str = str_cmd_out_prefix + convert_string_to_url(get_current_date_time(as_string=True)) + str_cmd_out_suffix
        out_command_str = ' > ' + out_filename_str
        str_command = str_command + out_command_str
    os.system(str_command)
    if bool_output:
        if bool_return_output:
            return read_file(out_filename_str, bool_no_lines=True)
        else:
            return out_filename_str
    return


def convert_string_to_url(str_original):
    """Converts a string to a URL compliant version and returns that string back

    UNIT TESTED

    Using a regular expression, remove all non-URL compliant characters and return that string

    Args:
        str_original: the string you want to convert

    Returns:
        None

    Raises:
        None
    """
    # https://stackoverflow.com/questions/1007481/how-do-i-replace-whitespaces-with-underscore-and-vice-versa
    # Remove all non-word characters (everything except numbers and letters)
    str_new = re.sub(r"[^\w\s]", '', str_original)

    # Replace all runs of whitespace with a single dash
    str_new = re.sub(r"\s+", '-', str_new)
    return str_new


def find_url_in_string(str_original):
    """ Find a URL in a string

    UNIT TESTED

    Using a regular expression, find a URL in a string and return that URL back as a string

    Args:
        str_original: the string you want to find the URL in

    Returns:
        None or the string with the URL

    Raises:
        None
    """
    # https://stackoverflow.com/questions/839994/extracting-a-url-in-python
    temp_re = re.search("(?P<url>https?://[^\s]+)", str_original)
    if temp_re is not None:
        output_str = temp_re.group("url")
        return output_str
    else:
        return None


def read_file(str_file_path, mode='rt', bool_no_lines=False):
    """ Read the contents of a file

    NOT UNIT TESTED

    Read the contents of the file passed on the string path from the current directory

    Args:
        str_file_path: the string of the file's path you want to read
        mode: Per https://www.w3schools.com/python/ref_func_open.asp, reads text from str_filepath
        bool_no_lines: removes the new lines from the file
    Returns:
        A string with the contents of the file
    Raises:
        None
    """
    # https://stackoverflow.com/questions/8369219/how-to-read-a-text-file-into-a-string-variable-and-strip-newlines
    print(str_file_path)
    with open(str_file_path, mode) as my_file:
        if bool_no_lines:
            data = my_file.read().replace('\n', '')
        else:
            data = my_file.readlines()
    return data


def get_current_date_time_url_str():
    """Converts the current date and time to a URL compliant version and returns that string back

    NOT UNIT TESTED

    Using a regular expression, remove all non-URL compliant characters from the date time string
        and return that string

    Args:
        None

    Returns:
        String

    Raises:
        None
    """
    return convert_string_to_url(get_current_date_time(as_string=True))


def wait(int_seconds):
    """Wait for a given number of seconds before proceeding

    NOT UNIT TESTED

    Use the time sleep function to wait for a given number of seconds

    Args:
        int_seconds: the number of seconds to wait in integer form

    Returns:
        None

    Raises:
        None
    """
    time.sleep(int_seconds)


def get_current_working_directory():
    """Gets the current working directory of the operating system

    UNIT TESTED

    Uses the os library to grab the current working directory and
        then converts it to a string and returns

    Returns:
        A string of the current working directory

    Raises:
        None
    """
    return str(os.getcwd())


def check_variable_type(check_variable, check_type):
    """Check if the first variable is of specific type

    UNIT TESTED

    Returns True if the variable being checked is of any of the
        tuple types passed

    Returns:
        True or False if the variable is of the types passed

    Raises:
        None
    """
    return type(check_variable) == check_type

