# TEMP FILE ONLY TO GENERATE YAML FOR TESTING
from time import sleep
import numpy as np
import copy
import yaml
import io
from os import path, read
import sys
import tty
import os
import signal

from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / '../config/motion_servo_parameters.yaml'
# file = file_location.open()


def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    print("Press key to exit.")
    sys.stdin.readline()
    sys.exit(-1)

def save_parameters(motion_servo_parameters_path, parameters):
    with io.open(motion_servo_parameters_path, 'w', encoding='utf8') as outfile:
        yaml.dump(parameters, outfile,
                  default_flow_style=False, allow_unicode=True)

def main(args=None):
    motion_servo_parameters_path = "/home/ubuntu/rpi_quad_ws/quad/config/motion_servo_parameters.yaml"
    
    parameters = {"zero_degrees_pulse_width": [1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500],
                  "pulse_width_per_degree": [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0],
                  "degrees_at_center_pulse_width": [0, -45, 135, 0, -45, 135, 0, -45, 135, 0, -45, 135],
                  "max_angle_degrees": [20, 0, 157.5, 20, 0, 157.5, 20, 0, 157.5, 20, 0, 157.5],
                  "min_angle_degrees": [-20, -67.5, 112.5, -20, -67.5, 112.5, -20, -67.5, 112.5, -20, -67.5, 112.5],
                  "leg_code": ["FLH", "FLU", "FLL", "FRH", "FRU", "FRL", "BLH", "BLU", "BLL", "BRH", "BRU", "BRL"]}

    with io.open(file_location, 'w', encoding='utf8') as outfile:
        yaml.dump(parameters, outfile, default_flow_style=False, allow_unicode=True)

    '''
    try:
        if path.exists(motion_servo_parameters_path):
            with open(motion_servo_parameters_path, 'r') as stream:
                parameters = yaml.safe_load(stream)   
    ''' 

if __name__ == '__main__':
    main()
