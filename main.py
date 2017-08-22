import time
import booting,gauge_display,standby_display
import PRi.GPIO as GPIO


# INIT
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

button_is_on = True
system_is_on = False


def is_button_on():
    input_state = GPIO.input(16)
    print('button_is_on', not(input_state))
    return not(input_state)

system_flag = 'standby' #booting,standby,gauge_display

while True:
    button_is_on = is_button_on()
    if button_is_on is True and system_is_on is False:
        print 'booting'
        booting.display()
        system_is_on = True
    if button_is_on is True and system_is_on is True:
        print 'guage_display'
        gauge_display.display(system_flag)
        system_flag = 'gauge_display'
    if button_is_on is False:
        print 'standby_display'
        standby_display.display(system_flag)
        system_is_on = False
        system_flag = 'standby'

    time.sleep(5)
