import schedule,os,logging,time
from datetime import datetime

PROCESSED_FOLDER = "./processed"
# create our custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler("logs.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)  

def job():
    csv_files = [file for file in os.listdir(PROCESSED_FOLDER) if file.endswith(".csv")]
    
    if len(csv_files) == 0:
        logger.error("ERROR: File not delivered by Company A")
    else:
        logger.info("SUCCESS: Data is delivered and processed correctly.")

schedule.every().seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)