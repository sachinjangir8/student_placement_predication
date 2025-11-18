import logging
import os
from datetime import datetime

# Create logs directory with timestamped log file
log_file=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
# Create logs directory if it doesn't exist
log_path=os.path.join("logs",log_file)
# making directory
os.makedirs(log_path,exist_ok=True)
# Complete log file path
log_file_path=os.path.join(log_path,log_file)

# Configure logging ,it will create a log file and store all the logs in that file
logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.INFO,
) 

# if __name__ == "__main__":
#     logging.info("Logger has been configured successfully.")