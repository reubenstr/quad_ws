

from lib.PCA9685Servos import PCA9685Servos




class ServoController:
    def __init__(
        self,
        address,
    ):

        self.servo_driver = PCA9685Servos(address)

        servos = []
        for i in range(16):
            s = Servo(dat1=i, dat2=i*2)
            servos.append(s) 


class Servo:
    def __init__(
        self, 
        center_pulse_width = 1500,
        pulses_per_degree = 10.0,
        min_pulse_width = 2500,
        max_pulse_width = 1500      
    ):
        self.center_pulse_width = center_pulse_width
        self.pulses_per_degree = pulses_per_degree
        self.min_pulse_width = min_pulse_width
        self.max_pulse_width = max_pulse_width