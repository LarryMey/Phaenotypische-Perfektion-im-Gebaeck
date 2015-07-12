from threading import Thread
from cookiepi.io.stepper import Stepper, Job
import logging


class StrawberryFactory:

    MAX_FORWARD_STEPS = 4000
    MIN_FORWARD_STEPS = 1000

    MAX_QUANTITY_DELAY = 10
    MIN_QUANTITY_DELAY = 1

    def __init__(self, down, forward, rotate):

        self.stepper = dict(down=down, forward=forward, rotate=rotate)


class StrawberryJob(Thread):

    def __init__(self, factory, forward=50, quantity=50, callback=None):
        Thread.__init__(self)

        self.factory = factory
        self.callback = callback

        forward_range = factory.MAX_FORWARD_STEPS - factory.MIN_FORWARD_STEPS
        self.forward_steps = (forward * forward_range / 100) + factory.MIN_FORWARD_STEPS

        quantity_range = factory.MAX_QUANTITY_DELAY - factory.MIN_QUANTITY_DELAY
        self.quantity_delay = ((100 - quantity) * quantity_range / 100) + factory.MIN_QUANTITY_DELAY

    def run(self):
        logging.info('starting strawberry job')
        self.step1()

    def step1(self):
        forward_job = Job(
            self.factory.stepper['forward'],
            steps=self.forward_steps,
            callback=self.step2)
        forward_job.start()

    def step2(self, job):
        down_job = Job(
            self.factory.stepper['down'],
            steps = Stepper.FULLCIRCLE / self.quantity_delay,
            delay=self.quantity_delay)
        rotate_job = Job(self.factory.stepper['rotate'], callback=self.step3)
        down_job.start()
        rotate_job.start()

    def step3(self, job):
        forward_job = Job(
            self.factory.stepper['forward'],
            steps=self.forward_steps,
            direction=Stepper.ANTICLOCKWISE,
            callback=self.callback)
        forward_job.start()

