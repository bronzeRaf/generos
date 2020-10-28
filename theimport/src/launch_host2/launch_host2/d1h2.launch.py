
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
            package='pack2',
            namespace='name/space2',
            executable='node2_exec',
            name='node2',
            output='screen',
            arguments=[('__log_level:=debug')]
        ),
    ])