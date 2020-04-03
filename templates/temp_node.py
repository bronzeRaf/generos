{# 
#This is a jinja2 template of a ROS2 Node
#
# Written in 13/3/2020
# Written by Rafael Brouzos
#}

import rclpy
from rclpy.node import Node
import sys

{%for p in publishers %}
from {{p.package}}.msg import {{p.type}}
{%endfor%}

{%for s in subscribers %}
from {{s.package}}.msg import {{s.type}}
{%endfor%}

#*********
{%for t in tmessages %}
from interfaces.msg import {{t}}
{%endfor%}
{%for s in smessages %}
from interfaces.srv import {{s}}
{%endfor%}
# ~ from std_msgs.msg import {{objects.type}}
# ~ from example_interfaces.srv import AddTwoInts


class {{node.name}}_class(Node):

	def __init__(self):
		super().__init__('{{node.name}}')
		# Publishers
		#____________________________________________
		{%for p in publishers %}
		self.publisher_{{p.name}}= self.create_publisher({{p.type}}, '{{p.topicPath}}', {{p.qos}})
		self.timer_{{p.name}} = self.create_timer({{p.publishRate}}, self.publisher_call_{{p.name}})
		self.i = 0
		#____________________________________________
		{%endfor%}
		
		# Subscribers
		#____________________________________________
		{%for s in subscribers %}
		self.subscriber_{{s.name}}= self.create_subscription({{s.type}}, '{{s.topicPath}}', self.subscriber_call_{{s.name}}, {{s.qos}})
		self.subscriber_{{s.name}}
		#____________________________________________
		{%endfor%}
		
		# Servers
		#____________________________________________
		{%for s in servers %}
		self.server_{{s.name}}= self.create_service({{s.type}}, '{{s.serviceName}}', self.server_call_{{s.name}})
		#____________________________________________
		{%endfor%}
		
		# Clients
		#____________________________________________
		{%for c in clients %}
		self.client_{{c.name}}= self.create_client({{c.type}}, '{{c.serviceName}}')
		#____________________________________________
		{%endfor%}
		
		
	# ************Calls************
	# Publishers
	#____________________________________________
	{%for p in publishers %}
	def publisher_call_{{p.name}}(self):
		msg = {{p.type}}()
		
		# Message after calculactions should be stored in
		{%for r in p.msg %}
		# msg.{{r}} 
		{%endfor%}
		
		{% if p.type == "ValueString" %}
		msg.x = 'Hello World: %d' % self.i
		{% endif %}
		
		{% if p.type == "ValueInt" %}
		msg.x = self.i
		{% endif %}
		
		self.publisher_{{p.name}}.publish(msg)
		self.get_logger().info('Publishing: "%s"' % msg.x)
		self.i += 1
	#____________________________________________
	{%endfor%}
	
	# Subscribers
	#____________________________________________
	{%for s in subscribers %}
	def subscriber_call_{{s.name}}(self, msg):
		# Store the variables of the msg
		{%for r in s.msg %}
		{{r}} = msg.{{r}}
		{%endfor%}
		self.get_logger().info('I heard: '+str(msg.x))
	#____________________________________________
	{%endfor%}
	
	#Servers
	#____________________________________________
	{%for s in servers %}
	def server_call_{{s.name}}(self, request, response):
		# Store the variables of the request
		{%for r in s.requests %}
		{{r}} = request.{{r}}
		{%endfor%}
		# Service result after calculactions should be stored in
		{%for r in s.responses %}
		# response.{{r}} 
		{%endfor%}
		response.c = request.a + request.b
		self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))
		return response
	#____________________________________________
	{%endfor%}
		
	# Clients
	#____________________________________________
	{%for c in clients %}
	def client_call_{{c.name}}(self{%for r in c.requests %}, {{r }} {%endfor%}):
		while not self.client_{{c.name}}.wait_for_service(timeout_sec=1.0):
			self.get_logger().info('service not available, waiting again...')
		self.request_{{c.name}} = {{c.type}}.Request()
		{%for r in c.requests %}
		self.request_{{c.name}}.{{r}} = {{r}}
		{%endfor%}
		self.future_{{c.name}} = self.client_{{c.name}}.call_async(self.request_{{c.name}})
		# Result after server's response is stored in 
		{%for r in c.responses %}
		# self.future_{{c.name}}.result().{{r}} 
		{%endfor%}
	#____________________________________________
	{%endfor%}
		
		
		
# Main executable
#____________________________________________
def main(args=None):
	rclpy.init(args=args)
	
	{{node.name}} = {{node.name}}_class()
		
	rclpy.spin({{node.name}})
	# Destroy the node explicitly
	# (optional - otherwise it will be done automatically
	# when the garbage collector destroys the node object)
	{{node.name}}.destroy_node()
	rclpy.shutdown()

# Clients executables
#____________________________________________
{%for c in clients %}
def {{c.name}}(args=None):
	rclpy.init(args=args)
	
	{{node.name}} = {{node.name}}_class()
	#TODO create typecast from command line to client call type (change int to custom type)
	{{node.name}}.client_call_{{c.name}}({%for r in c.requests %}int(sys.argv[{{loop.index}}]){% if not loop.last %}, {%endif%} {%endfor%})
	while rclpy.ok():
		rclpy.spin_once({{node.name}})
		if {{node.name}}.future_{{c.name}}.done():
			try:
				response = {{node.name}}.future_{{c.name}}.result()
			except Exception as e:
				{{node.name}}.get_logger().info('Service call failed %r' % (e,))
			else:
				{{node.name}}.get_logger().info(
				'Result of add_three_ints: for %d + %d = %d' %
				({{node.name}}.request_{{c.name}}.a, {{node.name}}.request_{{c.name}}.b, response.c))
			break
	
{%endfor%}
	
if __name__ == '__main__':
	main()
