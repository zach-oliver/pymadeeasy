"""
Created on 04/28/19
@author: zach-oliver
"""


def print_blank_line():
    print('')


def print_standard_line():
    print('-----------------------------------------------------------')


def print_bold_line():
    print('***********************************************************')


def print_message_highlighted(str_message):
    print_standard_line()
    print_blank_line()
    print(str_message)
    print_blank_line()
    print_standard_line()


def print_variable_highlighted(variable, str_variable_name):
    print_standard_line()
    print_blank_line()
    print(str_variable_name + ' ' + str(type(variable)) + ' : ' + str(variable))
    print_blank_line()
    print_standard_line()


def print_variables_highlighted(dict_variables):
    print_bold_line()
    print_blank_line()
    for key, value in dict_variables.iteritems():
        print(key + ' ' + str(type(value))  + ' : ' + str(value))
    print_blank_line()
    print_bold_line()


def print_str(str_print):
    print(str_print)


def print_obj(unknown_object):
    print(unknown_object)


def print_obj_to_str(unknown_object):
    print(str(unknown_object))


def print_message_standard(str_message):
    print_standard_line()
    print(str_message)
    print_standard_line()


def print_variable_standard(variable, str_variable_name):
    print_standard_line()
    print(str_variable_name + ' ' + str(type(variable)) + ' : ' + str(variable))
    print_standard_line()
