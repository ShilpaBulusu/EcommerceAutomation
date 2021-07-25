import logging


class GetLogger:
    @staticmethod
    def get_Logger(file):
        logging.basicConfig(filename=file,
                            format='%(asctime)s: %(levelname)s : %(message)s',
                            datefmt='%d : %m : %Y  %I : %M : %S %p',
                            force=True,
                            filemode='w')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
