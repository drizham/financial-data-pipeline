import time
import glob
import os
import utils_zero as uz
import download_zero as dz
import manage_lake
import summarise_zero as sz

def main():

    # remove all previously downloaded data
    manage_lake.delete_files('lake0/GC=F/raw/')
    manage_lake.delete_files('lake0/GC=F/description/')

    # get start and end dates to download data for
    start_dates, end_dates = uz.read_start_end_dates('start_end_dates.csv')

    print('Starting pipeline')
    time.sleep(1)

    # call first app in the pipeline - download financial data
    print('Downloading financial data files')
    dz.download_instrument_2_csv0('GC=F',start_dates, end_dates, 'lake0/')
    time.sleep(1)

    # call a 'summariser' that summarises each data *.csv file
    # use pandas in the summariser to calculate stats
    print('Running basic describe on data files')
    flist = glob.glob("lake0/GC=F/raw/*.csv") # get the list of downloaded data
    for file in flist:
        sz.describe_file(file, 'lake0/GC=F/description/')

    time.sleep(1)

    print('Pipeline run completed')

main()