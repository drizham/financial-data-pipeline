import time
import glob
import os
import utils_zero as uz
import download_zero as dz
import manage_lake
import summarise_zero as sz
import summarise_ob as so
import sys
from utils_zero import create_directory
from dotenv.main import load_dotenv
from kensu.utils.kensu_provider import KensuProvider
import urllib3

def main():
    urllib3.disable_warnings() # disables warnings being sent back from kensu

    # init the library using the conf file
    try:
        load_dotenv() # load environment variables from .env
        os.environ["KSU_CONF_FILE"] = "conf.ini" # project configuration
        # over rides some settings from conf.ini e.g. process_name = 'PipeLineX'
        KensuProvider().initKensu(kensu_ingestion_url = os.environ['KSU_KENSU_INTEGRATION_URL'],
                                  kensu_ingestion_token = os.environ["KSU_KENSU_INGESTION_TOKEN"],
                                  process_name = 'PipeLineX') # this is automatically importing the env vars
    except TypeError:   
        msg = "Unable to initialize kensu, ensure tokens and ingestion url are correct"
        print(msg)
    else:

        ticker = 'CL=F' # ticker of instrument to download
        lake = 'lake1/' # folder data to be written to
        # get start and end dates to download data for
        start_dates, end_dates = uz.read_start_end_dates('start_end_dates.csv')

        # remove all previously downloaded data
        manage_lake.delete_files(f'{lake}{ticker}/raw/')
        manage_lake.delete_files(f'{lake}{ticker}/description/')

        time.sleep(1)
        print('Starting pipeline')
    
        # call first app in the pipeline - download financial data
        print('Downloading financial data files')
        dz.download_instrument_2_csv0('GC=F',start_dates, end_dates, 'lake0/')
    
        # TODO put the run/ job settings in a file and use them
        run_settings = [ticker, start_dates, end_dates, lake]
        runner0(dz.download_instrument_2_csv0, run_settings)

        time.sleep(1)

        # call a 'summariser' that summarises each data *.csv file
        # use pandas in the summariser to calculate stats
        print('Running basic describe on data files')
        flist = glob.glob(f'{lake}{ticker}/raw/*.csv') # get the list of downloaded data
        for file in flist:
            so.describe_file(file, f'{lake}{ticker}/description/')
            
        time.sleep(1)

        print('Pipeline run completed')

def runner0(process_to_run, run_settings):
    try:
        return process_to_run(*run_settings)
    except:
        sys.exit(f'Issue running process {str(process_to_run)}')

main()