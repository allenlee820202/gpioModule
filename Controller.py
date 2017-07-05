from stepperMotor import StepperMotor_t
import time

motor = StepperMotor_t()
while(True):
	time.sleep(5)
	motor.start()
	time.sleep(5)
	motor.stop()
