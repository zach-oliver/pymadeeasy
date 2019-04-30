"""
Created on 04/12/19
@author: zach-oliver
"""

import os
import errno
import datetime
import time


def create_folders_along_path(str_path):
    """Creates any folders locally along str_path

    NOT UNIT TESTED

    Retrieves the current date and time one of two ways:
    - As a string object
    - As a datetime object

    Args:
        as_string: if False, function returns a datetime object.

    Returns:
        An example string: 2019-04-27 12:03:21.037656
        or the datetime object

    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
    """
    # https://stackoverflow.com/questions/12517451/automatically-creating-directories-with-file-output
    # creates the directory and any parent directories if it doesn't exist
    if not os.path.exists(os.path.dirname(str_path)):
        try:
            os.makedirs(os.path.dirname(str_path))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


def get_current_date_time(as_string=False):
    """Gets the current date and time

    UNIT TESTED

    Retrieves the current date and time one of two ways:
    - As a string object
    - As a datetime object

    Args:
        as_string: if False, function returns a datetime object.

    Returns:
        An example string: 2019-04-27 12:03:21.037656
        or the datetime object

    Raises:
        None
    """
    if as_string:
        return str(datetime.datetime.now())
    else:
        return datetime.datetime.now()


def get_current_time():
    """Gets the current date and time

    NOT UNIT TESTED

    Retrieves the current time

    Args:
        None

    Returns:
        An example time object: 1556510572.392354

    Raises:
        None
    """
    return time.time()
