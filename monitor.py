import schedule,os,logging
from datetime import time,datetime

logging.basicConfig(filename="logs.log",filemode="w", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
INCOMING_FOLDER = "./incoming"
PROCESSED_FOLDER = "./processed"
# first i will go inside the incoming folder and get all the csv files(though according to the requirement i expect only one file just incase there are more than one file) 
# and then i will read the csv file and then move the file to the processed folder

def job():
    csv_files = [file for file in os.listdir(INCOMING_FOLDER) if file.endswith(".csv")]
    
    if len(csv_files) == 0:
        logging.info("no csv file in the incoming folder")
    elif len(csv_files) == 1:
        filename = csv_files[0]
        source_path = os.path.join(INCOMING_FOLDER, filename)
        destination_path = os.path.join(PROCESSED_FOLDER, filename)
        os.rename(source_path, destination_path)
        logging.info("csv file moved to the processed folder")
    else:
        logging.info("more than one csv file in the incoming folder which is not allowed")
        
def write_log(message):
    with open("log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: {message}\n")

schedule.every().seconds.do(job)

while True:
    schedule.run_pending()