"""
Created on 04/28/19
@author: zach-oliver
"""


def print_message_highlighted(str_message):
    print('***********************************************************')
    print('                                                           ')
    print(str_message)
    print('                                                           ')
    print('***********************************************************')


def print_variable_highlighted(variable, str_variable_name):
    print('***********************************************************')
    print('                                                           ')
    print(str_variable_name + ' ' + str(type(variable)) + ' : ' + str(variable))
    print('                                                           ')
    print('***********************************************************')


def print_variables_highlighted(dict_variables):
    print('***********************************************************')
    print('                                                           ')
    for key, value in dict_variables.iteritems():
        print(key + ' ' + str(type(value))  + ' : ' + str(value))
    print('                                                           ')
    print('***********************************************************')