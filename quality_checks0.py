# basic quality checks for a dataframe
# TODO - add error checking to functions!

import pandas as pd
import glob

def number_of_rows_check(n_rows_expected, tolerance, dataframe):
    """Prints statistic of the number of rows read and witin tolerance
    n_rows_expected is the number of rows expected for the data read in
    tolerance is the plus minus tolerance of number of rows in %
    dataframe is the dataframe being checked
    Usage:
    n_rows_expected = 9900
    tolerance = 5 # tolerance in percent
    number_of_rows_check(n_rows_expected, tolerance, dataframe)
    """
    # Prints statistics of the number of rows read & if within tolerance
    rows_read = dataframe.shape[0]
    minimum_num_rows = n_rows_expected * ( 1 - tolerance / 100)
    maximum_num_rows = n_rows_expected * ( 1 + tolerance / 100)
    res_str = ''
    if ((minimum_num_rows < rows_read) and (rows_read < maximum_num_rows)):
        res_str = 'within'
    else:
        res_str = 'not within'
        
    print(f'Number of rows read: {rows_read} is {res_str} {tolerance}% tolerance of number of rows expected of {n_rows_expected} ')

def null_check0(df):
    """
    Performs a very basic check for null values in a dataframes
    Logs the number of null values occuring in each column &
    the total number of nulls
    Usage:
    null_check0(dataframe)
    TODO could add some return statistics"""
    col_names = df.columns
    sum_nulls = 0
    for i in range(len(col_names)):
        if (df[col_names[i]].isnull().values.any()):
            nulls = df[col_names[i]].isnull().sum()
            sum_nulls = sum_nulls + nulls
            print(f'Column {col_names[i]} has {sum_nulls} nuls')
    if (sum_nulls == 0):
        print('Data has no null values in any column')
    else:
        print(f'{sum_nulls} nulls found in total')

def check_column_types(expected_types, df0):
    """
    Logs for each column if the expected data type is found or not"""
    # Warning:
    # will not work as expected if number of columns are not the same!
    # or if column order does not agree!
    # loop through expected types and what the types really was to get type agreement
    n_read_columns = len(df0.dtypes) # number of read columns in df
    read_column_names = df0.keys().values.tolist()
    for i in range (n_read_columns):
        if (expected_types[i] == df0.dtypes[i]):
            print(f'{read_column_names[i]} column is of expected type {expected_types[i]}')
        else:
            print((f'{read_column_names[i]} column is of type {df0.dtypes[i]} and  NOT of expected type {expected_types[i]}'))

def check_number_of_columns(expected_types,df0):
    """
    Checks if number of columns, if expected number of columns found proceeds with type check of each column
    else exits
    expected_types - a list of expected types e.g. expected_types = ['O', 'float64', 'float64', 'float64', ...]
    df0 - pandas dataframe to check
    """
    n_expected_columns = len(expected_types)
    n_read_columns = len(df0.dtypes)
    read_column_names = df0.keys().values.tolist()    

    # check if length of types are the same i.e. a number of expected column check
    if (n_expected_columns == n_read_columns):
        print('Found expected number of data columns')
        print('Running column wise type checks...')
        check_column_types(expected_types, df0)
    else:
        print(f'Number of expected columns: {n_expected_columns} number of columns read: {n_read_columns}')
        print('Skipping columnwise type checks')

def quality_check_folder(lake, ticker, expected_types):
    """
    Runs a basic quality check on the *.csv files in the folder
    lake is part of the folder path
    ticker is subfolder path
    expected_types is a list of types e.g.  expected_types = ['O', 'float64', 'float64', 'float64',
       'float64', 'int64', 'float64', 'float64'] """
    print(f'Quality checking data in: {lake}{ticker}/raw/')
    flist = glob.glob(f'{lake}{ticker}/raw/*.csv') # get the list of downloaded data
    
    for file in flist:
        df0 = pd.read_csv(file)
        print(f'Processing file:{file}')
        null_check0(df0)
        check_number_of_columns(expected_types,df0)