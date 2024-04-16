import logging
import threading
from logging.handlers import RotatingFileHandler
import inspect

class Logger:
    def __init__(self, filename, max_bytes, backup_count):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        handler = RotatingFileHandler(filename, maxBytes=max_bytes, backupCount=backup_count)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(thread)d - %(message)s')
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

    def log(self, level, message):
        if level == "DEBUG":
            self.logger.debug(message)
        elif level == "INFO":
            self.logger.info(message)
        elif level == "ERROR":
            self.logger.error(message)
        else:
            raise ValueError("Invalid log level. Valid levels are DEBUG, INFO, and ERROR.")

def test_logging(logger):
    def worker():
        frame = inspect.currentframe()
        caller_frame = frame.f_back
        module_name = caller_frame.f_globals['__name__']
        function_name = caller_frame.f_code.co_name

        logger.log("DEBUG", f"This is a debug message from {module_name}.{function_name}.")
        logger.log("INFO", f"This is an info message from {module_name}.{function_name}.")
        logger.log("ERROR", f"This is an error message from {module_name}.{function_name}.")

    threads = []
    for _ in range(10):
        thread = threading.Thread(target=worker)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    log_file = "app.log"
    max_bytes = 5 * 1024 * 1024
    backup_count = 10

    logger = Logger(log_file, max_bytes, backup_count)

    test_logging(logger)