import manage_lake
import download_zero as dz
import numpy as np
import calendar_utils
import direction_suggester0
import pandas as pd

def main(ticker, year, lake):
    print(f'Downloading {ticker}, data for {year} to {lake}')

    # remove all previously downloaded data from folder
    manage_lake.delete_files(f'{lake}{ticker}/raw/')
    # get list of start and end dates to download data
    # & save to a separate *.csv file
    week_start_dates = calendar_utils.week_start_dates(year)
    week_end_dates = calendar_utils.week_end_dates(year)

    # download ticker data for the year
    # save each weeks' data as a *.csv file
    dz.download_instrument_2_csv0(ticker, week_start_dates, week_end_dates, lake)

    # check data quality for each file before using data
    expected_types = ['O', 'float64', 'float64', 'float64',
       'float64', 'int64', 'float64', 'float64']
    
    # runs through all the *.csv files and outputs the recomended direction
    # of trade for the next week
    # .market_direction1 calls the basic quality checks directly
    direction_suggester0.market_direction1(lake, ticker, expected_types)

main('CL=F', 2022, 'lake1/')