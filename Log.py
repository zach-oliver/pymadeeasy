"""
Created on 04/12/19
@author: zach-oliver
"""

from operating_system_functions import create_folders_along_path, get_current_date_time, get_current_time


class Log:

    def __init__(self, str_filename='', bool_debug=False, str_log_directory='log/',
                 str_function='', str_separator='|:|'):
        """Initialize the log file and class object

        UNIT TESTED

        Creates a local Log file and Log class object used to write logging and error
        statements to a local file for debugging purposes.

        Args:
            str_filename: A string used to set filename attribute
            bool_debug: A boolean used to set debug attribute
            str_log_directory: A string used to designate where the log files written by this
                class should go
            str_function: A string used to set function attribute
            str_separator: A string used to set separator attribute

        Returns:
            An example string: 2019-04-27 12:03:21.037656
            or the datetime object

        Raises:
            None

        Attributes:
            self.start_time: A string used to capture when the logging started and calculate overall run time
            self.filename: A string used to as the name of the file you are logging with this
                class and is used for logging statements written to the log file this
                class creates
            self.location: A string used as the location where the log file should be written
            self.debug: A boolean used to print log statements out to the console
            self.function: A string used as the name of the function you are logging with this
                class and is used for logging statements written to the log file this
                class creates
            self.separator: A string used to separate the filename from the function from
                the log statement when writing to the file
        """
        self.start_time = get_current_time()
        self.filename = str_filename
        self.location = get_current_date_time(as_string=True) + self.filename + '.log'
        self.debug = bool_debug
        self.function = str_function
        self.separator = str_separator

        if self.debug:
            print('log.py' + self.separator + 'self.location (file name)' + self.separator + self.location)

        self.location = "%s%s" % (str_log_directory, self.location)

        if self.debug:
            print('log.py' + self.separator + 'self.location (full name)' + self.separator + self.location)

        self.append('LOG CREATED')

    # UNIT TESTED
    def append(self, str_log_line):
        """Append log line to log file

        UNIT TESTED

        Creates the folders along the path and the log file if it doesn't exist and adds the
        log line as the last line of the file

        Args:
            str_log_line: A string that you wish to send to add to the log file

        Returns:
            None

        Raises:
            None
        """
        create_folders_along_path(self.location)

        log_line = get_current_date_time(as_string=True) + self.separator
        # https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
        log_line = log_line + str(round(get_current_time() - self.start_time, 2)) + ' sec'
        log_line = log_line + self.separator + self.filename
        log_line = log_line + self.separator + self.function
        log_line = log_line + self.separator + str(str_log_line)

        if self.debug:
            print(log_line)
        with open(self.location, "a") as f:
            f.write(log_line)
            f.write("\n")

    def change_filename(self, str_filename):
        """Change the log object filename string attribute

        UNIT TESTED

        Changes the filename string. Used to reflect a change of logging under a new filename with
        the same Log object. Adds a line to the log file.

        Args:
            str_filename: A string used to set filename attribute

        Returns:
            None

        Raises:
            None
        """
        self.filename = str_filename
        self.append('MOVED TO %s' % str_filename)

    def change_function(self, str_function):
        """Change the log object function string attribute

        UNIT TESTED

        Changes the function string. Used to reflect a change of logging under a new function with
        the same Log object

        Args:
            str_function: A string used to set function attribute

        Returns:
            None

        Raises:
            None
        """
        self.function = str_function

    def change_debug(self, bool_debug):
        """Change the log object debug boolean attribute

        UNIT TESTED

        Changes the debug boolean. Used to reflect a change of logging if you want to suppress
        debug statements printed to console

        Args:
            bool_debug: A boolean used to set debug attribute

        Returns:
            None

        Raises:
            None
        """
        self.debug = bool_debug
