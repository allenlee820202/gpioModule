from stepperMotor import StepperMotor_t
import time
from PIR import PIR_t

motor = StepperMotor_t()
pir = PIR_t()

def mycallback():
	print 'IR detected'
	motorIsStart=False
	if(motor.isStart==False):
		motor.start()
	else:
		motor.stop()
	

pir.setCallback(lambda *a: mycallback())
while True:
	time.sleep(10)

