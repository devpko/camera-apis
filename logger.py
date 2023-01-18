import logging


class Logger:
    """This class is for logging"""
    instance = None

    @classmethod
    def __set_logger(cls, name):
        logger = logging.getLogger(name)
        logger.propagate = False
        logger.setLevel(logging.WARNING)
        formatter = logging.Formatter('%(asctime)s \t %(levelname)s :: %(name)s :: %(message)s')

        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        handler.setLevel(logging.INFO)

        logger.addHandler(handler)

        return logger

    @classmethod
    def get_logger(cls):
        if not cls.instance:
            cls.instance = Logger.__set_logger("camera-apis")
        return cls.instance

    @classmethod
    def decorate(cls, func):
        def deco(*args, **kwargs):
            Logger.get_logger().info(f"{func.__name__}")
            return func(*args, **kwargs)
        return deco
