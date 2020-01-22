"""
Created on 10/06/19
@author: zach-oliver
"""


# issue: if there are any comments in the sql file this will not read
def data_frame_fill_blanks(data_frame, str_column, bool_in_place=True):
    return data_frame[str_column].fillna(0, inplace=bool_in_place)

