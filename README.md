## CSV file processing and monitoring the process

Background information
Every day at 07.00 AM, Company A will upload a file (Filename: CompanyFile.csv) to an incoming directory.
An automated process starting at 08.00 AM reads and processes the data from this file into a database, then moves the file to the processed directory when finished. Company B is using the processed data for reporting purposes.

User story
For our monitoring, we need a script to check if the file was delivered and processed correctly. We assume that when the file is in the processed directory, the data is processed correctly. 

## Project Structure

- incoming/  Folder where Company A uploads CSV files. In our case, any csv file will be processed though in the assignment description , It is stated that CompanyFile.csv.I was a bit confused whether I should only process with the name **CompanyFile.csv** file or any csv file. But ultimately I have decided to go with any csv file and max one csv file is allowed in that folder at a time.
- processed/  Folder where processed files are moved.

- data_process.py  Processes CSV files and inserts data into database in our case sql lite db. 
- monitor.py  Checks if the data was processed successfully.

- data.db  SQLite database
- logs.log  Log file containing processing and monitoring results
- README.md projecct description


## Database

We are using  **SQLite database** called `data.db`.


## Automation

We did automation with **schedule library**. It is possible to do your automation process in any time you would like to . So, If you go to **data_process.py** and there you will get a variable **EXECUTION_TIME** . Here you can chnage the time. Same goes for **monitor.py** script.


## Create a virtual environment 
Create virtual environment `python -m venv venv`

## Activate venv 
`venv\Scripts\activate`

## Install dependencies
To install dependencies please run `pip install -r requirements.txt`

## Run the script to see the results in the logs.log file
use this command `python script_name.py`