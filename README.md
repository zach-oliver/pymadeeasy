# pymadeeasy
## Introduction
Everyone has their own journey when learning a new language. pymadeeasy is intended to demonstrate [my](https://zacharyoliver.com) journey through Python 3.x. Goals include the following:
- Identify common problems and abstract them into reusable pieces
- Provide descriptive alternatives to streamline your next project
- Build community through learning

**Constructive** feedback is welcome at any time to help me along my Python journey.

## Current Version
2.1.1 [__**DataFrame functions**__][df] updated

### References
- [ref](https://github.com/zach-oliver/ref) is my first pass at this project starting with Python 2.x. At some point I needed to move on to 3.x so that journey starts now.
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) is a Python style guide from Google that points to a few common tools as well as formatting standards. As I learn more about these, I will strive to adhere to these so others can better understand my code.
- [Semantic Versioning](https://semver.org/) is a commonly known versioning scheme that I will do my best to adhere to over the course of this project.
- [Chalice](https://github.com/aws/chalice) is a Python Serverless Microframework using AWS. It allows you to create Lambda-based cloud functions and invoke them via API.
- [Pandas][pandas] a commonly used Python library making data processing easy.

## Versions
### 2.1.1
- Minor update for core python dependency

### 2.1.0
- [__**DataFrame functions**__][df] updated
    - updated names to align with common English semantics
    - added ability to copy from existing DataFrame column and check if value is in column names

### 2.0.0
- [__**DataFrame functions**__][df] launched
    - Common uses for the [Pandas][pandas] package including a tutorial of basic Series and DataFrame structures
- [__**Print functions**__][pf] changes:
    - differentiated line printing options based on intent with _print_blank_line_, _print_standard_line_, _print_bold_line_
    - added _print_message_standard_ and _print_variable_standard_
- [__**Log class**__][l] changes:
    - added the ability to turn logging to file and logging to console off and on independently

### 1.1.4
- [__**DataFrame functions**__][df] created:
    - _data_frame_fill_blanks_ will fill all null values in a column with 0

### 1.1.3
- [__**Log class**__][l] changes:
    - added assertions in _append_ and _append_new_line_ to make sure string was passed
    - added _append_object_as_string_ and _append_object_as_string_new_line_ for unknown object handling
- [__**Print functions**__][pf] change:
    - added _print_obj_ and _print_obj_to_str_ to be more explicit with variable types
- [__**Operating System functions**__][os] change:
    - removed reference to related pymadeeasy libraries to avoid race conditions

### 1.1.2
- Adjusted _current_date_time_ formatting and its use on [__**Log class**__][l]
    - [__**Log class**__][l] calls new _current_date_time_ formats in output file and line logging

### 1.1.1
- Added styling and invoking adjustments below
    - [__**Log class**__][l] calls [__**Operating System functions**__][os] correctly
    - [__**Operating System functions**__][os] calls [__**Print functions**__][pf] correctly
    - _test_api_ calls _api_, _print_functions_, _Log_, and [__**Operating System functions**__][os] correctly

### 1.1.0
- Added one function to [__**Print functions**__][pf]
    - _print_str_ added as a standard print function for strings
- Adjusted formatting of .gitignore

### 1.0.0
- Created _lambda_with_timer_trigger_ to provide example files to deploy a Chalice-based Lambda function triggered by a time interval.
    - Provided example for basic 5 minute trigger.
- Created two new functions in [__**Operating System functions**__][os]:
    - _get_current_working_directory_ returns the current working directory as a string.
    - _check_variable_type_ to return True if the variable passed is the type passed.

Find older release notes in the [Archive](https://github.com/zach-oliver/pymadeeasy/blob/master/archive.md)

## Developer Setup
- [Install Python 3 via Homebrew](https://wsvincent.com/install-python3-mac/)
- [Download PyCharm](https://www.jetbrains.com/pycharm/promo/anaconda/)
- [Configure pipenv in PyCharm](https://www.jetbrains.com/help/pycharm/pipenv.html)
- [Setup default AWS CLI credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#aws-config-file)

## Tools Used
- [PyCharm](https://www.jetbrains.com/pycharm/promo/anaconda/) I'm currently this trying out
- [Homebrew](https://brew.sh/) is a package manager for OS X. I used this to install Python 3.X

## Future Considerations
- pylint
- [pytorch](https://pytorch.org/get-started/locally/)
- [unittest](https://docs.python.org/3/library/unittest.html)

## Additional References
- [Markdown Guide](https://www.markdownguide.org/basic-syntax) is the guide I used for this README.md
- [pipenv](https://pipenv.readthedocs.io/en/latest/) is a tool used setup and manage your development environment

[pandas]: https://pandas.pydata.org/pandas-docs/stable/getting_started/overview.html
[df]: https://github.com/zach-oliver/pymadeeasy/blob/master/data_frame_functions.md
[pf]: https://github.com/zach-oliver/pymadeeasy/blob/master/print_functions.py
[l]: https://github.com/zach-oliver/pymadeeasy/blob/master/Log.py
[os]: https://github.com/zach-oliver/pymadeeasy/blob/master/operating_system_functions.py
