import unittest
from app_lib.logger import Logger



class TestLogger(unittest.TestCase):
    def test_my_logger(self):
        logger = Logger(filepath='logs/app.log').setup()
        logger.info('test message')