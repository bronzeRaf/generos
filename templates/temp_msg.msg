{# 
#This is a jinja2 template of the msg interfaces of ROS2 packages
#
# Written in 13/3/2020
# Written by Rafael Brouzos
#}
# Message {{message_data.name}} definition

# {{message_data.description}}


{%for o in objects %}
# {{o.name}} -- {{o.description}}
{%if not o.package == "no"%}{{o.package}}/{%endif%}{{o.type}} {{o.name}} {% if o.constant==True %} = {{o.default}} {%endif%}


{%endfor%}
