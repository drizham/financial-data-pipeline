# Use this to check if the tokens, environment variables etc
# are loading correctly
from dotenv.main import load_dotenv
import os

load_dotenv()
print(os.environ['KSU_KENSU_INGESTION_TOKEN'])