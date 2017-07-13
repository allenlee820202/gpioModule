import RPi.GPIO as GPIO
import time

def cb1():
	print 'hi'

class PIR_t(object):

	def action(self):
		print 'detected'

	def setCallback(self, cb):
		GPIO.add_event_detect(self.pin, GPIO.RISING, callback=cb, bouncetime=200)

	def __init__(self, pin=18):
		self.pin = pin
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
		# GPIO.add_event_detect(pin, GPIO.RISING, callback= lambda *a: self.action(), bouncetime=200)

if __name__ == '__main__':
	pir = PIR_t(18)
	pir.setCallback(lambda *a: cb1())

	while True:
		time.sleep(10)
