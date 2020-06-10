"""
Created on 10/06/19
@author: zach-oliver
"""
import pandas
import print_functions as p
# See https://github.com/zach-oliver/pymadeeasy for details


# UNIT TESTED
def add_new_column_to_data_frame_from_series(data_frame, str_new_column, new_series):
    assert_is_data_frame(data_frame, called_by='add_new_column_to_data_frame_from_series')
    assert_is_series(new_series, called_by='add_new_column_to_data_frame_from_series')
    data_frame[str_new_column] = new_series


# UNIT TESTED
def assert_is_data_frame(data_frame, called_by=''):
    assert isinstance(data_frame,
                      pandas.DataFrame), "Variable type FAIL! You sent a non-DataFrame to a DataFrame function(%s)" % called_by

# UNIT TESTED
def assert_is_series(series, called_by=''):
    assert isinstance(series,
                      pandas.Series), "Variable type FAIL! You sent a non-Series to a Series function(%s)" % called_by


# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_numpy.html
def convert_data_frame_to_numpy_variables(data_frame):
    assert_is_data_frame(data_frame, called_by='convert_data_frame_to_numpy_variables')
    data_frame.to_numpy()


# UNIT TESTED
def create_blank_data_frame():
    return pandas.DataFrame()


# UNIT TESTED
def create_data_frame(data):
    return pandas.DataFrame(data)


def fill_data_frame_blanks(data_frame, str_column, fill_value=0, bool_in_place=True):
    assert_is_data_frame(data_frame, called_by='fill_data_frame_blanks')
    return data_frame[str_column].fillna(fill_value, inplace=bool_in_place)


# UNIT TESTED
# https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
def get_data_frame_cell(data_frame, str_index, str_column):
    assert_is_data_frame(data_frame, called_by='get_data_frame_cell')
    if str_index in data_frame.index:
        return data_frame.loc[str_index, str_column]
    else:
        return ''


# https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
def get_data_frame_column_with_index(data_frame, str_column):
    assert_is_data_frame(data_frame, called_by='get_data_frame_column_with_index')
    return data_frame[str_column]


# https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
def get_data_frame_row_as_series_from_index(data_frame, str_index):
    assert_is_data_frame(data_frame, called_by='get_data_frame_row_from_index')
    if is_value_in_data_frame_index(data_frame, str_index):
        return data_frame.loc[str_index]
    else:
        return pandas.Series()


# https://stackoverflow.com/questions/17071871/how-to-select-rows-from-a-dataframe-based-on-column-values
def get_data_frame_rows_where_column_equals_value(data_frame, str_column, value):
    assert_is_data_frame(data_frame, called_by='get_data_frame_rows_where_column_equals_value')
    return data_frame.loc[data_frame[str_column] == value]


# https://stackoverflow.com/questions/17071871/how-to-select-rows-from-a-dataframe-based-on-column-values
def get_data_frame_rows_where_column_equals_values(data_frame, str_column, values):
    assert_is_data_frame(data_frame, called_by='get_data_frame_rows_where_column_equals_values')
    return data_frame.loc[data_frame[str_column].isin(values)]


# UNIT TESTED
# https://stackoverflow.com/questions/14808945/check-if-variable-is-dataframe/14809026
def is_data_frame(data_frame):
    assert_is_data_frame(data_frame, called_by='is_data_frame')
    return isinstance(data_frame, pandas.DataFrame)


# UNIT TESTED
def is_empty_data_frame(data_frame):
    assert_is_data_frame(data_frame, called_by='is_data_frame_empty')
    return data_frame.empty


# UNIT TESTED
def is_value_in_data_frame_index(data_frame, value):
    assert_is_data_frame(data_frame, called_by='is_value_in_data_frame_index')
    return value in data_frame.index


# UNIT TESTED
def output_data_frame_as_string(data_frame):
    assert_is_data_frame(data_frame, called_by='output_data_frame')
    return data_frame.to_string()


# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html
def set_data_frame_index(data_frame, str_column, inplace=True):
    assert_is_data_frame(data_frame, called_by='set_data_frame_index')
    data_frame.set_index(str_column, inplace=inplace)


# https://stackoverflow.com/questions/13842088/set-value-for-particular-cell-in-pandas-dataframe-using-index
def set_data_frame_value(data_frame, index, str_column, value):
    assert_is_data_frame(data_frame, called_by='set_data_frame_value')
    data_frame.at[index, str_column] = value


# https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
def sort_data_frame_index(data_frame, axis=1, ascending=False, inplace=True):
    assert_is_data_frame(data_frame, called_by='sort_data_frame_index')
    data_frame.sort_index(axis=axis, ascending=ascending, inplace=inplace)


# https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
def sort_data_frame_by_values_in_column(data_frame, str_column, axis=0, ascending=True, inplace=True):
    assert_is_data_frame(data_frame, called_by='get_data_frame_row_from_index')
    data_frame.sort_values(by=str_column, axis=axis, ascending=ascending, inplace=inplace)


if __name__ == '__main__':
    p.print_message_standard('START data_frame_functions.py')
    temp_df = create_blank_data_frame()
    assert_is_data_frame(temp_df, called_by='data_frame_functions.py')
    p.print_str('temp_df blank DataFrame created')
    assert is_data_frame(temp_df), "is_data_frame() FAIL! temp_df is not a DataFrame!"
    p.print_str('temp_df is_data_frame()')
    assert is_empty_data_frame(temp_df), "is_data_frame_empty() FAIL! temp_df should be empty!"
    p.print_str('temp_df is_empty_data_frame()')
    p.print_str('temp_df output should be empty:')
    p.print_str(output_data_frame_as_string(temp_df))
    p.print_standard_line()
    # example inspired by https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
    p.print_str('DataFrame objects are a collection of Series objects with a common key known as an "index"')
    p.print_str('Dictionaries are a "key: value" pair data structure')
    p.print_standard_line()
    p.print_str('The first dictionary (type integer) with a common key')
    temp_list_key = ['key_a', 'key_b', 'key_c', 'key_d']
    temp_list_int = range(len(temp_list_key))
    # https://www.geeksforgeeks.org/python-convert-two-lists-into-a-dictionary/
    temp_dict_int = {temp_list_key[i]: temp_list_int[i] for i in range(len(temp_list_key))}
    p.print_obj(temp_dict_int)
    p.print_standard_line()
    p.print_str('The second dictionary (type timestamp) with a common key')
    temp_list_time = [pandas.Timestamp('20200607'),
                      pandas.Timestamp('20200606'),
                      pandas.Timestamp('20200608'),
                      pandas.Timestamp('20200605')]
    temp_dict_time = {temp_list_key[i]: temp_list_time[i] for i in range(len(temp_list_key))}
    p.print_obj(temp_dict_time)
    p.print_standard_line()
    p.print_str('Dictionaries must be converted to a Series object, where keys are now called indexes')
    temp_series_int = pandas.Series(temp_dict_int)
    assert_is_series(temp_series_int, called_by='data_frame_functions.py')
    p.print_obj(temp_series_int)
    p.print_standard_line()
    temp_series_time = pandas.Series(temp_dict_time)
    assert_is_series(temp_series_time, called_by='data_frame_functions.py')
    p.print_obj(temp_series_time)
    p.print_str('Indexes across Series objects are usually common as you can see above!')
    p.print_standard_line()
    p.print_str('DataFrame data is imported as a dictionary of Series objects,')
    p.print_str('where the keys of this data dictionary are the column names.')
    temp_dict_data = {
        'col_A': temp_series_int,
        'col_B': temp_series_time,
        'col_C': pandas.Series(1, index=temp_list_key, dtype='float32'),
        'col_D': pandas.Series(1, index=temp_list_key, dtype='int32'),
        'col_E': pandas.Categorical(["test", "train", "train", "test"]),
        'col_F': 'foo'
    }
    temp_df = pandas.DataFrame(data=temp_dict_data)
    p.print_str("Once imported with column names, here's the resulting DataFrame")
    p.print_standard_line()
    p.print_str(output_data_frame_as_string(temp_df))
    assert is_value_in_data_frame_index(temp_df, temp_list_key[
        1]), "is_value_in_data_frame_index() FAIL! Original dictionary key did not persist to DataFrame index!"
    p.print_standard_line()
    p.print_str("Each column has the following DataFrame data type")
    p.print_obj_to_str(temp_df.dtypes)
    temp_str_col = 'col_G'
    add_new_column_to_data_frame_from_series(temp_df, temp_str_col, temp_series_int)
    p.print_standard_line()
    p.print_str("Now adding a new G column with the data from A")
    p.print_str(output_data_frame_as_string(temp_df))
    temp_A = get_data_frame_cell(temp_df, temp_list_key[1], 'col_A')
    assert temp_A == 1, "get_data_frame_cell() FAIL! col_A was not gathered!"
    temp_G = get_data_frame_cell(temp_df, temp_list_key[1], 'col_G')
    assert temp_G == 1, "get_data_frame_cell() FAIL! col_G was not gathered!"
    assert temp_A == temp_G, "add_new_column_to_data_frame_from_series FAIL! col_G was not copied from col_A properly!"
    p.print_standard_line()
    p.print_str("G column added correctly! All tests have passed!")
    p.print_message_standard('FINISH data_frame_functions.py')

