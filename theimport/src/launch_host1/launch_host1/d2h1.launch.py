
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='pack1',
            namespace='',
            executable='node1_exec',
            name='node1',
            output='screen',
            arguments=[('__log_level:=debug')]
        ),
        Node(
            package='pack1',
            namespace='name/space3',
            executable='node3_exec',
            name='node3',
            output='screen',
            arguments=[('__log_level:=debug')]
        ),
    ])