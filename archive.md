# pymadeeasy

[Home](https://github.com/zach-oliver/pymadeeasy/blob/master/README.md)

## Archive of Release Notes
### 0.0.5
- Created two new functions in _operating_system_functions_:
    - _get_current_date_time_url_str_ converts the current date and time to a URL compliant version and returns that string back.
    - _wait_ for a given number of seconds before proceeding.

### 0.0.4
- Created _lambda_with_api_trigger_ to provide example files to deploy a Chalice-based Lambda function triggered by an API request.
    - Provided example for basic _GET_ on root and additional paths.
- Added several functions to _operating_system_functions.py_:
    - _run_command_ now has the ability to store or return the output from the terminal when that code was run.
    - _convert_string_to_url_ added to provide a url-compliant version of the string you pass to it. Good for file names as well.
    - _find_url_in_string_ added to identify a url within a string of text.
    - _read_file_ added to provide an easy way to read files and provide text with or without new lines.
- Added redirect history to _api_ function and class.
- Added _post_data_, _post_json_, and _post_file_ functions to _APIResponse_ class.

### 0.0.3.1
- Added _run_command_ to run a string on the command line in python
    - Needed to run Chalice

### 0.0.3
- Initial _api_ for easy requesting and handing of responses over HTTP including:
    - _get_api_response_ - make a basic request and return a response
    - _dict_http_status_codes_ - a dictionary of primary status codes
    - _APIResponse_ class providing more easy to use attributes to deal with the request

### 0.0.2
- _Log_ class for error and debug logging
- Initial _operating_system_functions_ including:
    - _get_current_date_time_ - return the current date & time
    - _create_folders_along_path_ - from where this script is running, create folders along a path
    - _get_current_time_ - return the current time

### 0.0.1
- Includes the scope of this project and overall format via the README.md

### 0.0.0
 - Initial commit when creating the repository including the .gitignore and README.md

#### Tools Deprecated
- [Anaconda](https://www.anaconda.com/distribution/) is what I'm most familiar with to date and what I used to build [ref](https://github.com/zach-oliver/ref)
- [Sublime](https://www.sublimetext.com/) was used as a general text editor until I found pycharm
