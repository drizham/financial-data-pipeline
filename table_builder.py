from os.path import exists
import glob
import kensu.pandas as pd
#import pandas as pd
def build0(lake, ticker,input, output):
    """
    builds the basic data file of instrument to date
    i.e. runs everytime there is a new *.csv file available
    lake - is the path to where the *.csv files are loaded e.g. 'lake1/'
    ticker - is the ticker of the instrument to process e.g 'CL=F'
    input - is input file to process 
    output - is the name of the table to be updated e.g. 'table0.csv'
    """
    #input_path = f'{lake}{ticker}/{input}' TODO fix path confusion
    input_path = input
    output_path = f'{lake}{ticker}/{output}'

    if not exists((input_path)):
        print(f'File: {input_path} does not exist... ')
        return # returns as no input file to process

    df0 = pd.DataFrame() # TODO is this needed?

    try:
        # check if data table to write to already exists
        if exists(output_path):
            print(f'Appending to pre-existing table on {output}')
            # exists read it, append data to it and overwrite it
            df0 = pd.read_csv(output_path)
            df_temp = pd.read_csv(input_path) # TODO FIX
            df0 = pd.concat([df0, df_temp])
            df0.to_csv(output_path, index=False)
        else:
            print(f'Creating table and saving to: {output}')
            df0 = pd.read_csv(input_path) # TODO FIX 
            df0.to_csv(output_path, index=False)

    except Exception as e:
        msg = f'Unable to build basic data file and save as {output}'
        print(msg)
        print(e)
    else:
        print(f'{ticker} table saved to {output_path}')