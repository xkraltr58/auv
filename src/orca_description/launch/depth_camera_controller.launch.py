import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'controller_config_package',
            default_value=['my_robot_control'],  # Replace with your package name
            description='Package name where the controller config resides'
        ),
        DeclareLaunchArgument(
            'controller_config_file',
            default_value='camera_controller.yaml',  # The name of your controller config file
            description='Name of the controller configuration file'
        ),
        Node(
            package='controller_manager',
            executable='spawner',
            name='spawner',
            namespace=LaunchConfiguration('controller_config_package'),  # Use the declared package name
            output='screen',
            parameters=[
                {'use_sim_time': 'false'},
                {'config': LaunchConfiguration('controller_config_file')}  # Use the declared config file name
            ],
        ),
    ])
