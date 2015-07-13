from cookiebakery.cookies.evolution import Evolution
from cookiebakery.state.micro import Micro
from fysom import Fysom
import Queue
import logging
import threading


class Macro:

    def __init__(self,
                 left_button=None,
                 left_led=None,
                 right_button=None,
                 right_led=None,
                 track=None,
                 strawberry_factory=None,
                 chocolate_factory=None):

        self.buttons_locked = False
        self.micro_lock = threading.Lock()

        self.pending_cookies = Queue.Queue()

        self.left_button = left_button
        self.left_button.register(self.button_pressed)
        self.left_led = left_led
        self.left_led.off()

        self.right_button = right_button
        self.right_button.register(self.button_pressed)
        self.right_led = right_led
        self.right_led.off()

        self.track = track
        self.strawberry_factory = strawberry_factory
        self.chocolate_factory = chocolate_factory

        self.evolution = Evolution()

        self._fsm = Fysom(
            initial='waiting',
            events=[('reproduce', 'waiting', 'waiting')],
            callbacks=[('on_state_waiting', self._unlock),
                       ('onreproduce', self._reproduce)])

    @property
    def status(self):
        return self._fsm.current

    def produce(self):
        self.evolution.register(self.next_step)
        while True:
            self.micro_lock.acquire()
            self.cookie = self.pending_cookies.get()
            logging.info('reproducing one cookie')
            self._fsm.reproduce()

    def finish(self, e=None):
        self.right_led.off()
        self.left_led.off()
        if self.cookie is self.evolution.ancestors[0].last():
            self.left_led.on()
        else:
            self.right_led.on()
        self._unlock()

    def _reproduce(self, e):
        m = Micro(self, self.cookie, callback=self.finish)
        m.start()

    def _unlock(self):
        if self.pending_cookies.empty():
            logging.debug('unlocking buttons')
            self.buttons_locked = False
        self.micro_lock.release()

    def next_step(self, cookie, new_cookie=None):
        self.pending_cookies.put(cookie)
        if new_cookie:
            self.pending_cookies.put(new_cookie)

    def button_pressed(self, pin):
        if self.buttons_locked:
            return
        self.buttons_locked = True
        logging.debug('locking buttons')
        logging.info('button {} pressed'.format(pin))

        if pin == self.left_button.pin:
            self.evolution.next(self.evolution.ancestors[0].last())
        else:
            self.evolution.next(self.evolution.ancestors[1].last())

