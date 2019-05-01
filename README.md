# pymadeeasy
## Introduction
Everyone has their own journey when learning a new language. pymadeeasy is intended to demonstrate my own journey through Python 3.x and identify ways to abstract problems into reusable pieces that can be used by any project.

***Constructive*** feedback is welcome at any time to help me along my Python journey.

## Current Version
0.0.3 will include common ways to make HTTP requests and receive responses.

## Next Version
0.0.4 will include common ways to create an HTTP endpoint.

## References
- [ref](https://github.com/zach-oliver/ref) is my first pass at this project starting with Python 2.x. At some point I needed to move on to 3.x so that journey starts now.
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) is a Python style guide from Google that points to a few common tools as well as formatting standards. As I learn more about these, I will strive to adhere to these so others can better understand my code.
- [Semantic Versioning](https://semver.org/) is a commonly known versioning scheme that I will do my best to adhere to over the course of this project.

## Versions
### 0.0.3
- Initial _api_ for easy requesting and handing of responses over HTTP including:
    - _get_api_response_ - make a basic request and return a response
    - _dict_http_status_codes_ - a dictionary of primary status codes
    - _API_ class providing more easy to use attributes to deal with the request

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


## Future Considerations
- pylint
- [pytorch](https://pytorch.org/get-started/locally/)
- [unittest](https://docs.python.org/3/library/unittest.html)

## Additional References
- [Markdown Guide](https://www.markdownguide.org/basic-syntax) is the guide I used for this README.md
- [pipenv](https://pipenv.readthedocs.io/en/latest/) is a tool used setup and manage your development environment

## Tools Used
- [PyCharm](https://www.jetbrains.com/pycharm/promo/anaconda/) I'm currently this trying out
- [Anaconda](https://www.anaconda.com/distribution/) is what I'm most familiar with to date and what I used to build [ref](https://github.com/zach-oliver/ref)
- [Sublime](https://www.sublimetext.com/) I use as a general text editor until I find the best IDE and dev environment management solution
- [Homebrew](https://brew.sh/) is a package manager for OS X. I used this to install pipenv
