# gpioModule

## PIR sensor
  P18 (BCM) as the input of PIR sensor
  Usage
  ```python
  from PIR import PIR_t
  import time
  PIR_t(18)  
  while(True):
    time.sleep(10)
  ```
  
## Stepper motor 
  P16, P20, P21, P26 as the pin1, pin2, pin3 and pin4 of stepper motor
 ```python
from stepperMotor import StepperMotor_t
import time

motor = StepperMotor_t()
while(True):
        time.sleep(5)
        motor.start()
        time.sleep(5)
        motor.stop()
 ```
