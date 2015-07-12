from fysom import Fysom
from cookiepi.factory.strawberry import StrawberryJob
from cookiepi.factory.chocolate import ChocolateJob
import logging


class Micro:

    def __init__(self, macro, callback=None):
        self.callback = callback
        self.macro = macro
        self._fsm = Fysom(
            initial='waiting',
            events=[('load', 'waiting', 'loaded'),
                    ('produce_strawberry', 'loaded', 'produced_strawberry'),
                    ('produce_chocolate', 'produced_strawberry', 'produced_chocolate'),
                    ('present', 'produced_chocolate', 'waiting')],
            callbacks=[('onload', self._load),
                       ('onproduce_strawberry', self._produce_strawberry),
                       ('onproduce_chocolate', self._produce_chocolate),
                       ('onpresent', self._present)])

    @property
    def status(self):
        return self._fsm.current

    def start(self):
        self._fsm.load()

    def produce_chocolate(self, job):
        self._fsm.produce_chocolate()

    def present(self, job):
        self._fsm.present()

    def _load(self, e):
        logging.info('loading cookie')
        self.macro.track.to_load()
        self._fsm.produce_strawberry()

    def _produce_strawberry(self, e):
        logging.info('producing strawberry')
        job = StrawberryJob(self.macro.strawberry_factory,
                            callback=self.produce_chocolate)

        self.macro.track.to_strawberry()
        job.start()

    def _produce_chocolate(self, e):
        logging.info('producing chocolate')
        job = ChocolateJob(self.macro.chocolate_factory,
                           callback=self.present)

        self.macro.track.to_chocolate()
        job.start()

    def _present(self, e):
        logging.info('presenting cookie')
        self.macro.track.to_present()
        if self.callback:
            self.callback()
