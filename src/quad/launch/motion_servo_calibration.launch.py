import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
    
def generate_launch_description():
    ld = LaunchDescription()
    
    motion_servo_parameters_path = os.path.join(
        get_package_share_directory('quad'),
        'config',
        'motion_servo_parameters.yaml')  
        
    quad_node=Node(
        package = 'quad',
        #name = 'quad_node',
        executable = 'motion_servo_calibration',
        output='screen',  
        parameters = [{"motion_servo_parameters_path": motion_servo_parameters_path}], 
	# launch node in a new terminal to allow keyboard input
	prefix = ['gnome-terminal --'],
    )         
    
    ld.add_action(quad_node)
    return ld   
