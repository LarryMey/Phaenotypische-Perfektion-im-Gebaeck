import RPi.GPIO as GPIO

class Out(object):

    def __init__(self, pin, status=GPIO.LOW):
        self.pin = pin
        self.status = status
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        if status==GPIO.HIGH:
            self.on()
        else:
            self.off()

    def on(self):
        self.status = GPIO.HIGH
        GPIO.output(self.pin, self.status)

    def off(self):
        self.status = GPIO.LOW
        GPIO.output(self.pin, self.status)

    def toggle(self):
        if self.status==GPIO.LOW:
            self.on()
        else:
            self.off() 

