
from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port
from orangepwm import *


gpio.init ()


led = port.PA21
pwm = OrangePwm(100, led)
pwm.start(20)




      
