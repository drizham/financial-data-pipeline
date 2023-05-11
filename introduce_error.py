import os
import pandas as pd
from random import choice, random

def double_column_max(data_frame, column_name):
    # returns a data_frame after doubling the maximum value of column_name
    # in data_frame
    # find the maximum value in the column and double it
    double_value = data_frame.max(axis=0, skipna=True, numeric_only=True)[column_name] * 2
    # write double_value at the top of the data frame
    data_frame.at[0,column_name] = double_value # 0 = first row of data frame
    return data_frame

def halve_column_min(data_frame, column_name):
    # returns a data_frame after halving the minimum value of column_name
    # in data_frame
    # find the minimum value in the column and halve it
    halve_value = data_frame.min(axis=0, skipna=True, numeric_only=True)[column_name] / 2
    # write halve value at the top of the data frame
    data_frame.at[0, column_name] = halve_value # 0 = first row of data frame
    return data_frame

# TODO add more ERROR INTRODUCING FUNCTIONS
# add / delete rows
# add / delete columns

def introduce_error(input_path):
    # randomly introduces an error in a *.csv file and OVERWRITES the file
    # in a randomly choosen column from the list 'error_column'

    if not os.path.exists((input_path)):
        print(f'File: {input_path} does not exist')
        return
    try:
        df = pd.read_csv(input_path)
        error_introducers = [double_column_max, halve_column_min] # list of error introducing functions
        #error_column = ['Open', 'High', 'Low', 'Close'] # TODO use this for even more randomness
        #TODO
        error_column = ['Close']
        df_corrupt = choice(error_introducers)(df, choice(error_column)) # randomly select error introducing func.
        
        print(df_corrupt.head(2))
        df_corrupt.to_csv(input_path)
        print(f'corrupted file saved as: {input_path}')
        
    except Exception as e:
        print(f'Unable to introduce error for file {input_path}')
        print(e)

def randomly_introduce_errors(input_path, error_rate = 0.2):
    # input_path - input path of *.csv file to introduce the error into
    # rate - number between 0 and 1 rate at which errors should be introduced at
    # 0 is zero error 1 is a 100% error rate 
    # Defaults to 0.2 rate 
    if (random() < error_rate):
        print(f'Introducing error to {input_path}')
        introduce_error(input_path)
    else:
        print('Not introducing error')

# test
def main(input_path, rate):
    count = 0
    while count < 10:
        randomly_introduce_errors(input_path, rate)
        count += 1 
#main('lake1/CL=F/raw/we_2023-02-04.csv', 0.2)