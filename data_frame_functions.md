# pymadeeasy

[Home](https://github.com/zach-oliver/pymadeeasy/blob/master/README.md)

## DataFrame functions
A DataFrame is a common 2-dimensional data structure that is helpful in gathering, processing, and extracting data in Python. Think of it like an Excel Spreadsheet or CSV with rows and columns. 

[Pandas][pandas] is a commonly used Python library that makes processing data easy. This library uses a Series, a dictionary-like object, with a key and value pair to represent a single column of the DataFrame. The use of **key** _(for dictionaries)_, **row** _(for CSVs)_, and **index** _(for DataFrames)_ are used interchangeably for the sake of explanation simplicity below.

|    | series_1   | series_2   |
|---:|:-----------|:-----------|
|  key_0 | elk        | dog        |
|  key_1 | pig        | quetzal    |

When combining multiple Series into a DataFrame, they will often times place common keys across Series on the same row _(see `key_0`, `key_1` above)_ but each value will be where the key is the index of the DataFrame and the value is placed where the index and column name match.

[data_frame_functions.py](https://github.com/zach-oliver/pymadeeasy/blob/master/data_frame_functions.py) provides descriptive alternatives to streamline the use of DataFrames within your code.

**Note**: When using the phrase _"passed"_ in descriptions below, the object being "passed" is in the form of an argument to a [Python function](https://www.w3schools.com/python/python_functions.asp).

## Last Updated Version
2.0.0 **data_frame_functions** launched

### Previous Updated Version
1.1.4 **data_frame_functions** created in beta

### References
- [Pandas][pandas] a commonly used Python library making data processing easy.

## Versions
### 2.0.0
- **data_frame_functions** added:
    - **add_new_column_to_data_frame_from_series** will add a new column to the DataFrame 
    - **assert_is_data_frame** will stop the script and throw an error if object is not a DataFrame
    - **assert_is_series** will stop the script and throw an error if object is not a Series
    - **convert_data_frame_to_numpy_variables** will change all values within the passed DataFrame to [NumPy](https://numpy.org/learn/) variables
    - **create_blank_data_frame** will return a blank DataFrame
    - **create_data_frame** will return a DataFrame with passed data
    - **get_data_frame_cell** will return a specific cell value within the passed DataFrame
    - **get_data_frame_column_with_index** will return a column of the DataFrame and its indexes if found
    - **get_data_frame_row_as_series_from_index** will return a Series representing the row of a DataFrame if found
    - **get_data_frame_rows_where_column_equals_value** will return all rows within the passed DataFrame where a column matches a value 
    - **get_data_frame_rows_where_column_equals_values** will return all rows within the passed DataFrame where a column matches a set of values 
    - **is_data_frame** will return True if passed object is DataFrame
    - **is_empty_data_frame** will return True is passed DataFrame is empty
    - **is_value_in_data_frame_index** will return True if passed value is found in DataFrame index
    - **output_data_frame_as_string** will return the passed DataFrame as a string
    - **set_data_frame_index** will change the index of the DataFrame to the column passed
    - **set_data_frame_value** will set the value at the passed index and column of the DataFrame
    - **sort_data_frame_index** will sort the passed DataFrame by its index
    - **sort_data_frame_by_values_in_column** will sort the passed DataFrame by the values within one of its columns

### 1.1.4
- **data_frame_functions** created:
    - **fill_data_frame_blanks** will fill all null values in a column with 0

## Functions
### add_new_column_to_data_frame_from_series
- will add a new column to the DataFrame when passed a Series
- will name the new column in the DataFrame the passed string
### assert_is_data_frame
- will stop the script and throw an error to the console if the function argument is not a [Pandas][pandas] DataFrame
- **called_by** argument allows you to add a description (as a string) of the function which invoked this function for improved error communication
### convert_data_frame_to_numpy_variables
- will change all values within the passed DataFrame to [NumPy](https://numpy.org/learn/) variables for easy calculations
### create_blank_data_frame
- returns a blank DataFrame from [Pandas][pandas]
### create_data_frame
- returns a DataFrame with passed data imported
### fill_data_frame_blanks
- will fill all null values in a column with a default of 0
### get_data_frame_cell
- returns a value from the cell within the passed DataFrame if it exists
- will return the value from the passed index and column or a blank string
### get_data_frame_column_with_index
- returns an entire column of the DataFrame passed with indexes included if the column name is found
### get_data_frame_row_as_series_from_index
- returns a Series representing the entire row of a DataFrame if found
### get_data_frame_rows_where_column_equals_value
- returns all rows within the passed DataFrame where a column matches a value
### get_data_frame_rows_where_column_equals_values
- returns all rows within the passed DataFrame where a column matches a set of values
### is_data_frame
- returns True if the function argument passed is a [Pandas][pandas] DataFrame else False
### is_empty_data_frame
- returns True if function argument passed DataFrame is empty else False
### is_value_in_data_frame_index
- returns True if function argument passed variable is within the DataFrame index else False
### output_data_frame_as_string
- returns the passed DataFrame as a string for easier output to console or file
### set_data_frame_index
- changes the index of the passed DataFrame to the column string passed
### set_data_frame_value
- changes the value at the passed index and column of the passed DataFrame
### sort_data_frame_index
- changes the index order of the passed DataFrame in ascending order by default
### sort_data_frame_by_values_in_column
- changes the index order of the passed DataFrame by the values within one of its columns in ascending order by default

[pandas]: https://pandas.pydata.org/pandas-docs/stable/getting_started/overview.html