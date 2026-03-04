import schedule,os,logging,time
from datetime import date, datetime

PROCESSED_FOLDER = "./processed"
# create our custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler("logs.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)  

def job():
    logger.info("Monitoring job started")
    #get all csv files in the processed folder
    csv_files = [file for file in os.listdir(PROCESSED_FOLDER) if file.endswith(".csv")]
    # if no csv file found log an error and return
    if len(csv_files) == 0:
        logger.error("ERROR: File not delivered by Company A")
        return
    # check if any of the csv files in the processed folder were modified today, if so log a success message, if not log an error message
    today = date.today()
    success = False
    for file in csv_files:

        file_path = os.path.join(PROCESSED_FOLDER, file)

        modified_date = datetime.fromtimestamp(
            os.path.getmtime(file_path)
        ).date()

        if modified_date == today:
            logger.info(f"SUCCESS: File processed today with the filename {file}")
            success = True
            break
        
    if not success:
        logger.error("ERROR: No CSV file processed today")

    logger.info("Monitoring job finished")

schedule.every().day.at("20:16").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)