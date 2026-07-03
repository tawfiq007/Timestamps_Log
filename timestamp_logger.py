import os
from datetime import datetime

# This is the name of the folder where all log files will be saved.
 

FOLDER_NAME = "action_data"


def make_folder_if_missing():
    """
    This function checks if the 'action_data' folder already exists.
    If it does not exist, it creates it...
    """
    if not os.path.exists(FOLDER_NAME):
        os.makedirs(FOLDER_NAME)


def get_today_filename():
    """
    This function builds daily log file inside FOLDER_NAME by date
    Example output: "02-04-2026.txt"
    """
    today = datetime.now()
    # strftime formats a date into a string.
    # %d = day, %m = month, %Y = full year
    date_text = today.strftime("%d-%m-%Y")
    filename = date_text + ".txt"
    return filename


def get_current_time():
    """
    This function returns the current time as a short text string,
    like "09:15:24".

    This is the timestamp that gets added in front of every log message.
    """
    now = datetime.now()
    # %H = hour (24-hour format), %M = minute, %S = second
    time_text = now.strftime("%H:%M:%S")
    return time_text


def log(message):
    """
    This is the main function that other programs will use.

    What it does, step by step:
    1. Make sure the 'action_data' folder exists.
    2. Figure out today's log file name.
    3. Get the current time.
    4. Build the full path to today's log file (folder + filename).
    5. Open the file in "append" mode and add a new line with the
       timestamp and the message.
    """
    # Step 1: make sure the folder exists
    make_folder_if_missing()

    # Step 2: get today's filename
    filename = get_today_filename()

    # Step 3: get the current time for the timestamp
    time_now = get_current_time()

    # Step 4: build the full file path (for example: action_data/02-04-2026.txt)
    file_path = os.path.join(FOLDER_NAME, filename)

    # Step 5: build the line of text we want to save
    log_line = "[" + time_now + "] " + message + "\n"

    # Open the file in append mode ("a") so we add to it instead of
    # replacing it. We use UTF-8 encoding so the file can safely store
    # any kind of text, including special characters.
    with open(file_path, "a", encoding="utf-8") as log_file:
        log_file.write(log_line)