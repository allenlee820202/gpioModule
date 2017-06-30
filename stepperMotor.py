import RPi.GPIO as GPIO
import time, threading

class StepperMotor_t(object):
	state=0
	isStart=False
	def __init__(self, pin1=16, pin2=20, pin3=21, pin4=26):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		self.ControlPin = [pin1, pin2, pin3, pin4]
		for pin in self.ControlPin:
			GPIO.setup(pin, GPIO.OUT)
			GPIO.output(pin, 0)

		self.seq = [ [1, 0, 0, 0],
			     [1, 1, 0, 0],
			     [0, 1, 0, 0],
			     [0, 1, 1, 0],
			     [0, 0, 1, 0],
			     [0, 0, 1, 1],
			     [0, 0, 0, 1],
			     [1, 0, 0, 1] ]

		self.isStart=False
		self.spinthread = threading.Thread(target = self.spin, args = (), name = 'spin')
		self.start()
	
	def spin(self):
		while(self.isStart):
			for halfstep in range(8):
				for pin in range(4):
					GPIO.output(self.ControlPin[pin], self.seq[halfstep][pin])
				time.sleep(0.001)

	def start(self):
		self.isStart=True
		self.spinthread = threading.Thread(target = self.spin, args = (), name = 'spin')
		self.spinthread.start()

	def stop(self):
		self.isStart=False
		self.spinthread.join()

if __name__ == '__main__':
	motor = StepperMotor_t()
	
	while(True):
		raw_input('press any key to stop')
		motor.stop()
		raw_input('press any key to start')
		motor.start()
