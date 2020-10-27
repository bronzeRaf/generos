{# 
#This is a jinja2 template of a ROS2 launch python file
#
# Written in 26/10/2020
# Written by Rafael Brouzos
#}

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        {%for node in nodes %}
        Node(
            package='{{node.package}}',
            {%if node.version<5%}
            node_namespace='{{node.namespace}}',
            node_executable='{{node.executable}}',
            node_name='{{node.name}}',
            {%else%}
            namespace='{{node.namespace}}',
            executable='{{node.executable}}',
            name='{{node.name}}',
            {%endif%}
            output='screen',
            arguments=[('__log_level:=debug')]
        ),
        {%endfor%}
    ])
