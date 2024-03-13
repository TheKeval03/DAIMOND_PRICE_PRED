import logging 
import os 
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

"""In summary, these lines of code generate a unique log file name based on the current date and time, 
create a "logs" directory within the current working directory if it doesn't exist, 
and then set logs_path to the complete path of the log file within the "logs" directory. 
This prepares the logging infrastructure for the subsequent configuration and recording of log messages."""

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s)] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
