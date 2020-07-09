import RPi.gpio as GPIO
import time

btn_input = 15

GPIO.setmode(GPIO.BCM)

Gpio.setup(btn_input, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while 1:
	if GPIO.input(btn_input) == GPIO.HIGH:
	print(@Button pushed!@)
	time.sleep(0.1)

GPIO.cleanup()

