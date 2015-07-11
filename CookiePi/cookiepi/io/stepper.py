from threading import Thread
import RPi.GPIO as GPIO
import logging
import time


class Stepper:

    CLOCKWISE = 1
    ANTICLOCKWISE = -1

    Seq = ((1,0,0,0),
           (1,1,0,0),
           (0,1,0,0),
           (0,1,1,0),
           (0,0,1,0),
           (0,0,1,1),
           (0,0,0,1),
           (1,0,0,1))
    StepCount = len(Seq) - 1

    def __init__(self, name, gpios):
        self.name = name
        self.gpios = gpios

        GPIO.setmode(GPIO.BOARD)

        for gpio in self.gpios:
            GPIO.setup(gpio, GPIO.OUT)
            GPIO.output(gpio, False)


class Job(Thread):

    def __init__(self, stepper, steps=4076, delay=1, direction=Stepper.CLOCKWISE):
        Thread.__init__(self)

        self.stepper = stepper
        self.steps = steps
        self.delay = delay/1000.0
        self.direction = direction

    def run(self):
        logging.info('rotating stepper {} by {} steps'.format(
            self.stepper.name, self.steps))

        StepCounter = 0

        while abs(StepCounter) < self.steps:
            for pin in range(0, len(self.stepper.gpios)):
                gpio = self.stepper.gpios[pin]
                GPIO.output(
                    gpio,
                    bool(Stepper.Seq[StepCounter % len(Stepper.Seq)][pin]))
            StepCounter += self.direction

            # Wait before moving on
            time.sleep(self.delay)

