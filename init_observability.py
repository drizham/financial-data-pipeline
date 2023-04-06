# functions to initialise Kensu and observability
import urllib3
from dotenv.main import load_dotenv
import os
from kensu.utils.kensu_provider import KensuProvider


def init_kensu(process_name):
    """process_name is the application name to be made 'observable' """
    # init the library using the conf file
    urllib3.disable_warnings() # disables warnings being sent back from kensu
    try:
        print(f'Initiallising Kensu for: {process_name}')
        load_dotenv() # load environment variables from .env
        os.environ["KSU_CONF_FILE"] = "conf.ini" # project configuration
        # over rides some settings from conf.ini e.g. process_name = process_name
        return KensuProvider().initKensu(kensu_ingestion_url = os.environ['KSU_KENSU_INTEGRATION_URL'],
                                  kensu_ingestion_token = os.environ["KSU_KENSU_INGESTION_TOKEN"],
                                  process_name = process_name,
                                  code_version = '1.0.0',
                                  allow_reinit = True) # this is automatically importing the env vars
    except Exception as e:   
        msg = f'Unable to initialize kensu for {process_name} ensure tokens and ingestion url are correct'
        print(msg)
        print(e)