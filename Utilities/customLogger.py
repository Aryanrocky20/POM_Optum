import logging
import os

class LogGen:

    @staticmethod
    def loggen():
        file_path = os.path.relpath('.\\Logs\\automation.log')
        logging.basicConfig(filename=file_path,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m%d%Y %I:%M:%S %p')

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
