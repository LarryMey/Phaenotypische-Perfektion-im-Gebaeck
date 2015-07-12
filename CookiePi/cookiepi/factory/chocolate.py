from threading import Thread
from cookiepi.io.stepper import Stepper, Job
import logging


class ChocolateFactory:

    MAX_ROUNDS = 10
    MIN_ROUNDS = 1

    MAX_FORWARD_DELAY = 10
    MIN_FORWARD_DELAY = 1

    DOWN_DELAY = 2

    def __init__(self, down, forward, rotate):

        self.stepper = dict(down=down, forward=forward, rotate=rotate)


class ChocolateJob(Thread):

    def __init__(self, factory, rounds=50, velocity=50, callback=None):
        Thread.__init__(self)

        self.factory = factory
        self.callback = callback

        forward_range = factory.MAX_FORWARD_DELAY - factory.MIN_FORWARD_DELAY
        self.forward_delay = ((100 - velocity) * forward_range / 100) + factory.MIN_FORWARD_DELAY

        rounds_range = factory.MAX_ROUNDS - factory.MIN_ROUNDS
        self.rounds = (rounds * rounds_range / 100) + factory.MIN_ROUNDS

    def run(self):
        logging.info('starting chocolate job')
        rotate_job = Job(
            self.factory.stepper['rotate'],
            steps=Stepper.FULLCIRCLE * self.rounds,
            callback=self.callback)
        forward_job = Job(
            self.factory.stepper['forward'],
            delay=self.forward_delay,
            steps=(Stepper.FULLCIRCLE * self.rounds) / self.forward_delay)
        down_job = Job(
            self.factory.stepper['down'],
            delay=ChocolateFactory.DOWN_DELAY,
            steps=(Stepper.FULLCIRCLE * self.rounds) / ChocolateFactory.DOWN_DELAY)

        rotate_job.start()
        forward_job.start()
        down_job.start()
