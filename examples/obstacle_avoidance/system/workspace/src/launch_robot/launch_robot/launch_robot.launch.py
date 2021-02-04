
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='obstacle_avoidance',
            node_namespace='',
            node_executable='sonar_exec',
            node_name='sonar',
            output='screen',
            arguments=[('__log_level:=debug')]
        ),
        Node(
            package='obstacle_avoidance',
            node_namespace='',
            node_executable='motor_exec',
            node_name='motor',
            output='screen',
            arguments=[('__log_level:=debug')]
        ),
        Node(
            package='obstacle_avoidance',
            node_namespace='',
            node_executable='controller_exec',
            node_name='controller',
            output='screen',
            arguments=[('__log_level:=debug')]
        ),
    ])