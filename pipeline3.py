import manage_lake
import download_zero as dz
import numpy as np
import calendar_utils
import direction_suggester0
def main(ticker, year, lake):
    print(f'Downloading {ticker}, data for {year} to {lake}')

    # remove all previously downloaded data
    manage_lake.delete_files(f'{lake}{ticker}/raw/')
    # get list of start and end dates to download data
    # & save to a separate *.csv file
    week_start_dates = calendar_utils.week_start_dates(year)
    week_end_dates = calendar_utils.week_end_dates(year)
    dz.download_instrument_2_csv0(ticker, week_start_dates, week_end_dates, lake)

    # runs through all the *.csv files and outputs the recomended direction
    # of trade for the next week
    direction_suggester0.market_direction0(lake, ticker)

main('CL=F', 2022, 'lake1/')