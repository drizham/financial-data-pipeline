import glob
import pandas as pd

def market_direction0(lake, ticker):
    """
    prints the direction of trades based on where the fast moving average is
    relative to the slow moving average
    lake - is the path to where the *.csv files are loaded e.g. 'lake1/'
    ticker - is the ticker of the instrument to process e.g 'CL=F'
    """

    df0 = pd.DataFrame()
    # loop through all files in folder and append to df0 (pandas dataframe)
    print('Processing weekly data for trade signals')
    flist = glob.glob(f'{lake}{ticker}/raw/*.csv') # get the list of downloaded data
    
    for file in flist:
        df_temp = pd.read_csv(file)
        df0 = pd.concat([df0, df_temp])
        
        # calc moving averages & their difference
        df0['Close_MA5'] = df0['Close'].rolling(window=5).mean()
        df0['Close_MA15'] = df0['Close'].rolling(window=15).mean()
        df0['Diff_MA'] = df0['Close_MA5'] - df0['Close_MA15'] # if fast is larger (+ve) look for longs
        last_row = df0.iloc[-1:] # gets the last entry of the CSV file or last row on the 'db' at the moment
        # simple recommendation or direction based on MA diff
        if last_row['Diff_MA'].values[0] > 0: # if Diff_MA is > than 0
            time_stamp = last_row['Datetime'].values[0]
            print (f'{time_stamp} recommend only long trades for {ticker} ')
        else:
            time_stamp = last_row['Datetime'].values[0]
            print (f'{time_stamp} recommend only short trades for {ticker} ')