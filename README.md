# pymadeeasy
## Introduction
Everyone has their own journey when learning a new language. pymadeeasy is intended to demonstrate my own journey through Python 3.x and identify ways to abstract problems into reusable pieces that can be used by any project.

***Constructive*** feedback is welcome at any time to help me along my Python journey.

## Current Version
0.0.5 added the ability to create a time based file name / url and the ability to wait before continuing the execution.

## Next Version
0.0.6 will include more methods to expose and call a public API endpoint.

## References
- [ref](https://github.com/zach-oliver/ref) is my first pass at this project starting with Python 2.x. At some point I needed to move on to 3.x so that journey starts now.
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) is a Python style guide from Google that points to a few common tools as well as formatting standards. As I learn more about these, I will strive to adhere to these so others can better understand my code.
- [Semantic Versioning](https://semver.org/) is a commonly known versioning scheme that I will do my best to adhere to over the course of this project.
- [Chalice](https://github.com/aws/chalice) is a Python Serverless Microframework using AWS. It allows you to create Lambda-based cloud functions and invoke them via API.

## Versions
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

## Developer Setup
- [Install Python 3 via Homebrew](https://wsvincent.com/install-python3-mac/)
- [Download PyCharm](https://www.jetbrains.com/pycharm/promo/anaconda/)
- [Configure pipenv in PyCharm](https://www.jetbrains.com/help/pycharm/pipenv.html)
- [Setup default AWS CLI credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#aws-config-file)

## Tools Used
- [PyCharm](https://www.jetbrains.com/pycharm/promo/anaconda/) I'm currently this trying out
- [Homebrew](https://brew.sh/) is a package manager for OS X. I used this to install Python 3.X

#### Tools Deprecated
- [Anaconda](https://www.anaconda.com/distribution/) is what I'm most familiar with to date and what I used to build [ref](https://github.com/zach-oliver/ref)
- [Sublime](https://www.sublimetext.com/) was used as a general text editor until I found pycharm

## Future Considerations
- pylint
- [pytorch](https://pytorch.org/get-started/locally/)
- [unittest](https://docs.python.org/3/library/unittest.html)

## Additional References
- [Markdown Guide](https://www.markdownguide.org/basic-syntax) is the guide I used for this README.md
- [pipenv](https://pipenv.readthedocs.io/en/latest/) is a tool used setup and manage your development environment

