import logging
import os
from datetime import datetime

# Generate a log file name based on the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the project root directory
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the path where logs will be stored (each log gets its own folder inside 'logs')
logs_path = os.path.join(base_path, "logs", LOG_FILE)

# Create the specific log directory if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# Define the full path to the log file (inside its own folder)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging system
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
