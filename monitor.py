import schedule,os,logging,time
from datetime import datetime

INCOMING_FOLDER = "./incoming"
PROCESSED_FOLDER = "./processed"
# create our custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler("logs.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)  

def job():
    csv_files = [file for file in os.listdir(INCOMING_FOLDER) if file.endswith(".csv")]
    
    if len(csv_files) == 0:
        logger.info("No CSV file found in incoming folder")
    elif len(csv_files) == 1:
        filename = csv_files[0]
        source_path = os.path.join(INCOMING_FOLDER, filename)
        destination_path = os.path.join(PROCESSED_FOLDER, filename)
        os.rename(source_path, destination_path)
        logger.info("csv file moved to the processed folder")
    else:
        logger.info("more than one csv file in the incoming folder which is not allowed")
        
def write_log(message):
    with open("log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: {message}\n")

schedule.every().seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)