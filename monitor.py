import schedule
from datetime import time,datetime

def job():
    print("Process file from incoming folder and move it to the processed folder")

schedule.every().seconds.do(job)

while True:
    schedule.run_pending()
