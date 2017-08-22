import RPi.GPIO

class GPIO():
    """control the LED and button

    Note:..

    """
    def open_led(self, r, g, b):
        RPi.GPIO.setup(r, RPi.GPIO.OUT)
        RPi.GPIO.setup(g, RPi.GPIO.OUT)
        RPi.GPIO.setup(b, RPi.GPIO.OUT)

        print('open led')
        RPi.GPIO.output(r, low)
        RPi.GPIO.output(g, low)
        RPi.GPIO.output(b, low)


    def close_led(self, r, g, b):
        print('open close')
        RPi.GPIO.output(r, False)
        RPi.GPIO.output(g, False)
        RPi.GPIO.output(b, False)


    def clean_up(self, r, g, b):
        print('Clean up GPIO')
        GPIO.cleanup(r,g,b)





