import logging

class LogGen:
    @staticmethod
    def loggen():
        print("Hello")
        logging.basicConfig(filename=r".\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%Y-%m-%d %H:%M:%S',force=True)
        print("Hello logger File")
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger