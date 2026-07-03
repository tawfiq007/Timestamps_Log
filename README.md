# Timestamp Logger

A simple, beginner-friendly Python tool that automatically saves
messages with a timestamp into a daily log file.

## What This Project Does

Sometimes when you write a program, you want to keep a record of
what happened and when. This project lets you do that with a single
function call:

```python
log("Program started")
```

Every time you call `log()`, your message is saved into a text file,
along with the current time. A new file is automatically created for
each new day, so your logs stay organized.

## Features

- Automatically creates a folder called `action_data` to store logs
- Automatically creates a new log file for each day
- Adds a timestamp (current time) to every message
- Adds new messages to the end of the file, without deleting old ones
- Uses UTF-8 encoding, so any kind of text can be saved safely
- Written using simple, beginner-friendly Python (no classes, no
  advanced tricks)

## Folder Structure

```
timestamp_logger/
│
├── timestamp_logger.py   # the main module - contains the log() function
├── example.py             # an example showing how to use the module
├── README.md               # this file
└── action_data/            # log files are saved here (created automatically)
```

## Installation

You don't need to install anything extra. This project only uses
Python's built-in `os` and `datetime` modules, which come with Python
by default.

1. Download or copy the `timestamp_logger.py` file into your project
   folder.
2. Make sure your project's main file is in the same folder as
   `timestamp_logger.py` (or that Python can find it).

## How to Import It

In any Python file, add this line at the top:

```python
from timestamp_logger import log
```

Then you can call `log()` anywhere in your code.

## Example Usage

```python
from timestamp_logger import log

log("Program started")
log("User logged in")
log("Backup completed")
```

Running this code will create a folder named `action_data`, and
inside it, a file named after today's date, like `02-04-2026.txt`.

## Example Output

If you run the example above, the file `action_data/02-04-2026.txt`
will contain something like this:

```
[09:15:24] Program started
[09:15:30] User logged in
[09:15:42] Backup completed
```

Each time you run your program again on the same day, new lines will
be added to the bottom of this same file. If you run it again
tomorrow, a brand new file will be created automatically, named with
tomorrow's date.

## Python Concepts You Can Learn From This Project

This project was built using only simple, beginner-friendly ideas:

- **Functions** - small, reusable pieces of code (like `log()`)
- **Variables** - storing values like the folder name or a timestamp
- **If statements** - checking whether a folder already exists
- **The `os` module** - checking for and creating folders
- **The `datetime` module** - getting the current date and time
- **File handling** - opening, writing to, and closing files
- **String formatting** - building text like `"[09:15:24] message"`
- **Append mode (`"a"`)** - adding new lines to a file instead of
  overwriting it

This makes it a great small project to study if you're learning how
real Python tools and modules are built.

This is a simple Alternative for Logging module...
