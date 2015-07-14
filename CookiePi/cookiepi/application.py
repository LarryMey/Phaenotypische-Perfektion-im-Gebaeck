#!/usr/bin/python
from cookiepi.io.stepper import Stepper
from cookiepi.io.out import Out
from cookiepi.io.button import Button
from cookiepi.io.track import Track
from cookiepi.factory.strawberry import StrawberryFactory
from cookiepi.factory.chocolate import ChocolateFactory
from cookiebakery.state.macro import Macro
import logging
import time

logformat = "%(asctime)s %(levelname)s [%(name)s][%(threadName)s] %(message)s"
logging.basicConfig(format=logformat, level=logging.DEBUG)

def run_production():
    track1 = Out(24)
    track2 = Out(26)

    sdown = Stepper('down', (31, 33, 35, 37))
    sforward = Stepper('forward', (7, 11, 13, 15))
    cdown = Stepper('down', (8, 10, 12, 16))
    cforward = Stepper('forward', (19, 21, 23, 29))
    rotate = Stepper('rotate', (32, 36, 38, 40))

    track = Track(track1, track2)
    sfactory = StrawberryFactory(sdown, sforward, rotate)
    cfactory = ChocolateFactory(cdown, cforward, rotate)

    left_button = Button(3)
    left_led = Out(22)
    right_button = Button(5)
    right_led = Out(18)

    m = Macro(
        left_button=left_button,
        right_button=right_button,
        left_led=left_led,
        right_led=right_led,
        track=track,
        strawberry_factory=sfactory,
        chocolate_factory=cfactory)

    m.produce()

