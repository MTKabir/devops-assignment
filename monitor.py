import schedule
import schedule,os
from datetime import time,datetime

INCOMING_FOLDER = "./incoming"
PROCESSED_FOLDER = "./processed"
# first i will go inside the incoming folder and get all the csv files(though according to the requirement i expect only one file just incase there are more than one file) 
# and then i will read the csv file and then move the file to the processed folder

def job():
    print("Process file from incoming folder and move it to the processed folder")
    csv_files = [file for file in os.listdir(INCOMING_FOLDER) if file.endswith(".csv")]
    for filename in csv_files:
        os.rename(os.path.join(INCOMING_FOLDER, filename), os.path.join(PROCESSED_FOLDER, filename))

schedule.every().seconds.do(job)