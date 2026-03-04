import os,csv,sqlite3,logging,shutil,schedule,time
from logger import logger

INCOMING_FOLDER = "./incoming"
PROCESSED_FOLDER = "./processed"
EXECUTION_TIME = "23:25"
logger = logger()


# reads and processes the data from a file into a database, then moves the file to the processed directory when finished
def process_file():
    csv_files = [file for file in os.listdir(INCOMING_FOLDER) if file.endswith(".csv")]

    if len(csv_files) == 0:
        logger.info("No CSV file found in incoming folder")
        return
    elif len(csv_files) == 1:
        filename = csv_files[0]
        source_path = os.path.join(INCOMING_FOLDER, filename)
        try:
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
                CustomerName TEXT,
                Product TEXT,
                Quantity INTEGER,
                Price REAL,
                Date TEXT
            )
            """)

            with open(source_path, "r") as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    cursor.execute(
                        "INSERT INTO transactions (CustomerName, Product, Quantity, Price, Date) VALUES (?, ?, ?, ?, ?)",
                        (row[0], row[1], row[2], row[3], row[4])
                    )

            conn.commit()
            conn.close()

            logger.info("CSV data inserted into database")

            destination_path = os.path.join(PROCESSED_FOLDER, filename)
            shutil.move(source_path, destination_path)

            logger.info("File moved to processed folder")

        except Exception as e:
            logger.error(f"Processing failed: {e}")
    else:
        logger.info("more than one csv file in the incoming folder which is not allowed")

schedule.every().day.at(EXECUTION_TIME).do(process_file)

while True:
    schedule.run_pending()
    time.sleep(1)