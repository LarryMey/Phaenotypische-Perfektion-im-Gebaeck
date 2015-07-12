import RPi.GPIO as GPIO


class Button:

    def __init__(self, pin):
        self.pin = pin
        self.visits = list()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(pin, GPIO.FALLING, callback=self.pressed)

    def register(self, func):
        if func not in self.visits:
            self.visits.append(func)

    def pressed(self, pin):
        for func in self.visits:
            func(self.pin)
