import RPi.GPIO as GPIO
import time

class PIR_t(object):

	def action(self):
		print 'detected'

	def __init__(self, pin=18):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
		GPIO.add_event_detect(pin, GPIO.RISING, callback= lambda *a: self.action(), bouncetime=200)

if __name__ == '__main__':
	PIR_t(18)
	while True:
		time.sleep(10)
