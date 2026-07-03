
# This file shows how to use the timestamp_logger module.
# Run this file with: python example.py
#
# Each time you run it, new lines will be added to today's
# log file inside the "action_data" folder.
# you only add log(message) in your programme 


from timestamp_logger import log

log("Program started")
log("Opening database")
log("Database connected")
log("Backup completed")
log("Program finished")


