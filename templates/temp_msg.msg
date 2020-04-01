{# 
#This is a jinja2 template of the msg interfaces of ROS2 packages
#
# Written in 13/3/2020
# Written by Rafael Brouzos
#}
{%for o in objects %}
{{o.type}} {{o.name}}		# {{o.description}}
{%endfor%}
