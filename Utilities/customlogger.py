import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.INFO, force=True)
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.info('This is a debug message')
        return logger

    #or
    #def loggen():
    # formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    # handler = logging.FileHandler(filename='.\\Logs\\automation.log')
    # handler.setFormatter(formatter)
    # logger = logging.getLogger()
    # logger.setLevel(logging.INFO)
    # logger.addHandler(handler)
    # return logger