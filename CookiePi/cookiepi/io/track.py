import logging
import time


class Track:

    def __init__(self, gpio1, gpio2):
        self.gpio1 = gpio1
        self.gpio2 = gpio2

    def to_load(self):
        logging.info('driving to load')
        self.gpio1.on()
        time.sleep(11)

    def to_strawberry(self):
        logging.info('driving to strawberry')
        self.gpio1.off()
        time.sleep(10)

    def to_chocolate(self):
        logging.info('driving to chocolate')
        self.gpio2.on()
        time.sleep(7)

    def to_present(self):
        logging.info('driving to present')
        self.gpio2.off()
