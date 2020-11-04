
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='pack1',
            node_namespace='',
            node_executable='node1_exec',
            node_name='node1',
            output='screen',
            arguments=[('__log_level:=debug')]
        ),
        Node(
            package='pack1',
            node_namespace='name/space3',
            node_executable='node3_exec',
            node_name='node3',
            output='screen',
            arguments=[('__log_level:=debug')]
        ),
    ])