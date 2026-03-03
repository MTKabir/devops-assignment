import schedule
import schedule,os
from datetime import time,datetime

INCOMING_FOLDER = "./incoming"
PROCESSED_FOLDER = "./processed"
# first i will go inside the incoming folder and get all the csv files(though according to the requirement i expect only one file just incase there are more than one file) 
# and then i will read the csv file and then move the file to the processed folder

def job():
    csv_files = [file for file in os.listdir(INCOMING_FOLDER) if file.endswith(".csv")]
    
    if len(csv_files) == 0:
        print("no csv file in the incoming folder")
    elif len(csv_files) == 1:
        filename = csv_files[0]
        source_path = os.path.join(INCOMING_FOLDER, filename)
        destination_path = os.path.join(PROCESSED_FOLDER, filename)
        os.rename(source_path, destination_path)
        print("csv file moved to the processed folder")
    else:
        print("more than one csv file in the incoming folder which is not allowed")

schedule.every().seconds.do(job)

while True:
    schedule.run_pending()