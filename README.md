# Python Logger Module

This repository contains a Python Logger Module for managing logs in Python applications. The module provides functionalities for:

- Inserting log messages into a file at a predefined location.
- Formatting log messages with timestamps, log levels, file names, function names, thread IDs, and actual log content.
- Automatically rotating log files to prevent excessive file size.

## Usage

To use the Python Logger Module in your project:

1. Clone this repository to your local machine.
2. Import the Logger class from the logger_module.py file into your Python script.
3. Initialize the logger with the desired log file name, maximum file size, and backup count.
4. Log messages at different levels (DEBUG, INFO, ERROR) using the logger instance.

## Approach

The Python Logger Module was implemented using the following approach:

- Utilized the built-in logging module in Python to handle logging functionalities.
- Implemented a custom Logger class that encapsulates the logging functionality and provides an easy-to-use interface for logging messages at different levels.
- Configured a RotatingFileHandler to handle log file rotation, ensuring that log files do not grow too large.
- Formatted log messages to include timestamps, log levels, file names, function names, thread IDs, and actual log content for better readability and analysis.
