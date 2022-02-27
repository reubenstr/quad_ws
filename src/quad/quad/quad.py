from .quad_commander import QuadCommander
# from .quad_simulation import QuadCommander

from time import sleep
import rclpy
from rclpy.node import Node
import numpy as np
import copy
import yaml
import io
from os import path, read
from sensor_msgs.msg import Joy
from std_msgs.msg import Float32MultiArray

from rclpy.executors import SingleThreadedExecutor
from src.motion_parameters import MotionParameters
# from rclpy.logging import LoggingSeverity
from quad_interfaces.msg import JointAngles
from .joystick_interpreter import JoystickInterpreter

from rclpy.logging import LoggingSeverity
from rclpy.parameter import Parameter


# Temp location
def valmap(value, istart, istop, ostart, ostop):
  return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

class JoystickSubscriber(Node):
    def __init__(self):
        super().__init__('joy_subscriber_node')
        self.subscription = self.create_subscription(
            Joy, 'joy', self.listener_callback, 10)
        self.joystick_interpreter = JoystickInterpreter()
        self.motion_parameters = MotionParameters()

    def listener_callback(self, msg):
        axes = msg.axes
        buttons = msg.buttons
        self.motion_parameters = self.joystick_interpreter.get_motion_parameters(
            axes, buttons)

    def get_motion_parameters(self):
        return copy.deepcopy(self.motion_parameters)


class QuadPublisher(Node):
    def __init__(self):
        super().__init__('quad_publisher_node')
        self.publisher_ = self.create_publisher(JointAngles, 'joint_angles', 10)
        timer_period_ms = 0.020
        self.timer = self.create_timer(timer_period_ms, self.timer_callback)       
        self.joint_angles = np.empty([12])
        self.joint_angles_linked_leg = np.empty([12])
           
    def set_joint_angles(self, joint_angles):
        self.joint_angles = joint_angles

    def set_joint_angles_linked_leg(self, joint_angles_linked_leg):
        self.joint_angles_linked_leg = joint_angles_linked_leg

    def timer_callback(self):
        msg = JointAngles()   
        # TODO: remove the loop
        for i in range(12):
            msg.joint_angles[i] = self.joint_angles[i]
            msg.joint_angles_linked_leg[i] = self.joint_angles_linked_leg[i]
        self.publisher_.publish(msg)  

def main(args=None):
    rclpy.init(args=args)
    rclpy.logging._root_logger.log("QUAD STARTED", LoggingSeverity.INFO)

    quad_publisher = QuadPublisher()
    joystick_subscriber = JoystickSubscriber()

    parameters = quad_publisher.declare_parameters(
        namespace='',
        parameters=[
            ('motion_servo_parameters_path', None),
            ('frame_parameters_path', None),
            ('linked_leg_parameters_path', None)])

    motion_servo_parameters_path = quad_publisher.get_parameter(
        'motion_servo_parameters_path').get_parameter_value().string_value
    frame_parameters_path = quad_publisher.get_parameter(
        'frame_parameters_path').get_parameter_value().string_value
    linked_leg_parameters_path = quad_publisher.get_parameter(
        'linked_leg_parameters_path').get_parameter_value().string_value       

    rclpy.logging._root_logger.log(
        "motion_servo_parameters_path: " + motion_servo_parameters_path, LoggingSeverity.INFO)
    rclpy.logging._root_logger.log(
        "frame_parameters_path: " + frame_parameters_path, LoggingSeverity.INFO)
    rclpy.logging._root_logger.log(
        "linked_leg_parameters_path: " + linked_leg_parameters_path, LoggingSeverity.INFO)

    if path.exists(motion_servo_parameters_path):
        with open(motion_servo_parameters_path, 'r') as stream:
            motion_servo_parameters = yaml.safe_load(stream)

    if path.exists(frame_parameters_path):
        with open(frame_parameters_path, 'r') as stream:
            frame_parameters = yaml.safe_load(stream)

    if path.exists(linked_leg_parameters_path):
        with open(linked_leg_parameters_path, 'r') as stream:
            linked_leg_parameters = yaml.safe_load(stream)

    quad_commander = QuadCommander(frame_parameters, linked_leg_parameters)

    executor = SingleThreadedExecutor()
    executor.add_node(quad_publisher)
    executor.add_node(joystick_subscriber)

    
    while rclpy.ok():
        motion_parameters = joystick_subscriber.get_motion_parameters()
        joint_angles, joint_angles_linked_leg = quad_commander.tick(
            motion_parameters)
        quad_publisher.set_joint_angles(joint_angles)
        quad_publisher.set_joint_angles_linked_leg(joint_angles_linked_leg)

              
        '''    
        print (joint_angles[5]  * 180/3.1415) 
        print (joint_angles_linked_leg[5]  * 180/3.1415) 
        print (kit.servo[5].angle)
        print ()
        '''  
                     
        """  
        temp = temp + 1
        if temp > 5:
    quad_publisher.destroy_node()
    joystick_subscriber.destroy_node()
    rclpy.shutdown()gingSeverity.INFO)    
            rclpy.logging._root_logger.log("servo_pulse_widths[0] : " + str(servo_pulse_widths[offset + 0]), LoggingSeverity.INFO)
            rclpy.logging._root_logger.log("servo_pulse_widths[1] : " + str(servo_pulse_widths[offset + 1]), LoggingSeverity.INFO)
            rclpy.logging._root_logger.log("servo_pulse_widths[2] : " + str(servo_pulse_widths[offset + 2]), LoggingSeverity.INFO)
            rclpy.logging._root_logger.log("FR-HIP [0]  : " + str(joint_angles[offset + 0] * 180/np.pi), LoggingSeverity.INFO)
            rclpy.logging._root_logger.log("FR-ULEG [1] : " + str(joint_angles[offset + 1] * 180/np.pi), LoggingSeverity.INFO)
            rclpy.logging._root_logger.log("FR-LLEG [2] : " + str(joint_angles[offset + 2] * 180/np.pi), LoggingSeverity.INFO)
            rclpy.logging._root_logger.log("[L] FR-HIP [0]  : " + str(joint_angles_linked_leg[offset + 0] * 180/np.pi), LoggingSeverity.INFO)
            rclpy.logging._root_logger.log("[L] FR-ULEG [1] : " + str(joint_angles_linked_leg[offset + 1] * 180/np.pi), LoggingSeverity.INFO)
            rclpy.logging._root_logger.log("[L] FR-LLEG [2] : " + str(joint_angles_linked_leg[offset + 2] * 180/np.pi), LoggingSeverity.INFO)
            """   
        executor.spin_once()

    executor.shutdown()
    quad_publisher.destroy_node()
    joystick_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
