import inspect
import logging


class Logger:
    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        # filehandler = logging.FileHandler("./logs/automation.log")
        # filehandler = logging.FileHandler("./logs/automation.log", "a")
        filehandler = logging.FileHandler("./logs/automation.log", "w")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)  # File handler object
        logger.setLevel(logging.INFO)
        return logger
