from fysom import Fysom
from cookiepi.factory.strawberry import StrawberryJob
from cookiepi.factory.chocolate import ChocolateJob
import logging


class Micro:

    def __init__(self,
                 track=None,
                 strawberry_factory=None,
                 chocolate_factory=None):
        self.track = track
        self.strawberry_factory = strawberry_factory
        self.chocolate_factory = chocolate_factory
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

    def _load(self, e):
        logging.info('loading cookie')
        self.track.to_load()
        self._fsm.produce_strawberry()

    def _produce_strawberry(self, e):
        logging.info('producing strawberry')
        job = StrawberryJob(self.strawberry_factory,
                            callback=self._fsm.produce_chocolate)

        self.track.to_strawberry()
        job.start()

    def _produce_chocolate(self, e):
        logging.info('producing chocolate')
        job = ChocolateJob(self.chocolate_factory,
                           callback=self._fsm.present)

        self.track.to_chocolate()
        job.start()

    def _present(self, e):
        logging.info('presenting cookie')
        self.track.to_present()
