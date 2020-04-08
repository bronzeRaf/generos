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
{%if p.unique == 1 %}
from {{p.package}}.msg import {{p.type}}
{%endif%}
{%endfor%}

{%for s in subscribers %}
{%if s.unique == 1 %}
from {{s.package}}.msg import {{s.type}}
{%endif%}
{%endfor%}

{%for s in servers %}
{%if s.unique == 1 %}
from {{s.package}}.srv import {{s.type}}
{%endif%}
{%endfor%}

{%for c in clients %}
{%if c.unique == 1 %}
from {{c.package}}.srv import {{c.type}}
{%endif%}
{%endfor%}
#*********
# ~ {%for t in tmessages %}
# ~ from interfaces.msg import {{t}}
# ~ {%endfor%}
# ~ {%for s in smessages %}
# ~ from interfaces.srv import {{s}}
# ~ {%endfor%}
# ~ from std_msgs.msg import {{objects.type}}
# ~ from example_interfaces.srv import AddTwoInts

# Class for the node {{node.name}} 
class {{node.name}}_class(Node):
	
	# Constructor function of the node
	def __init__(self):
		super().__init__('{{node.name}}'{%if not node.namespace == None%}, namespace = '{{node.namespace}}'{%endif%})
		# Params
		#____________________________________________
		{%for p in params %}
		# {{p.name}}
		self.param_{{p.name}} = self.declare_parameter('{{p.name}}', {{p.value}})
		# You can use your parameter {{p.name}} with type {{p.type}}
		# with 		self.get_parameter('{{p.name}}')._value
		# or 		self.param_{{p.name}}._value
		# You can also use your parameter from terminal or yaml file. 
		#_____
		{%endfor%}
		
		
		# Publishers
		#____________________________________________
		{%for p in publishers %}
		# {{p.name}}
		self.publisher_{{p.name}} = self.create_publisher({{p.type}}, '{{p.topicPath}}', {{p.qos}})
		self.timer_{{p.name}} = self.create_timer({{p.publishRate}}, self.publisher_call_{{p.name}})
		self.i = 0
		#_____
		{%endfor%}
		
		# Subscribers
		#____________________________________________
		{%for s in subscribers %}
		# {{s.name}}
		self.subscriber_{{s.name}} = self.create_subscription({{s.type}}, '{{s.topicPath}}', self.subscriber_call_{{s.name}}, {{s.qos}})
		self.subscriber_{{s.name}}
		#_____
		{%endfor%}
		
		# Servers
		#____________________________________________
		{%for s in servers %}
		# {{s.name}}
		self.server_{{s.name}} = self.create_service({{s.type}}, '{{s.serviceName}}', self.server_call_{{s.name}})
		#_____
		{%endfor%}
		
		# Clients
		#____________________________________________
		{%for c in clients %}
		# {{c.name}}
		self.client_{{c.name}} = self.create_client({{c.type}}, '{{c.serviceName}}')
		#_____
		{%endfor%}
		
		
	# ************Callbacks************
	# Publishers
	#____________________________________________
	{%for p in publishers %}
	# This is the callback of the publisher {{p.name}}. 
	# You can store the message in the msg object attributes, according 
	# to the instructions in the comments below. This function will be 
	# called automatically with the chosen publish rate, to publish your 
	# messages. This function is the template of the publisher callback 
	# and you should put your own functionality.
	def publisher_call_{{p.name}}(self):
		msg = {{p.type}}()
		# Please create the message of the publisher in this callback
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
	#_____
	{%endfor%}
	
	# Subscribers
	#____________________________________________
	{%for s in subscribers %}
	# This is the callback of the subscriber {{s.name}}. 
	# You can obtain the message from the variables set in this 
	# function, according to the instructions in the comments below. 
	# This function will be called automatically every time a message is
	# received. This function is the template of the subscriber callback 
	# and you should put your own functionality.
	def subscriber_call_{{s.name}}(self, msg):
		# Please obtain the message from the subscriber in this callback
		# Store the variables of the msg
		{%for r in s.msg %}
		{{r}} = msg.{{r}}
		{%endfor%}
		# Now you can use the received variables
		self.get_logger().info('I heard: '+str(msg.x))
	#_____
	{%endfor%}
	
	#Servers
	#____________________________________________
	{%for s in servers %}
	# This is the callback of the server {{s.name}}. 
	# You can obtain the request to the server from the variables set in 
	# this function, according to the instructions in the comments 
	# below. This function will be called automatically every time a 
	# request is received. This function is the template of the server 
	# callback and you should put your own functionality.
	def server_call_{{s.name}}(self, request, response):
		# Please add the server's functionality in this callback
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
	#_____
	{%endfor%}
		
	# Clients
	#____________________________________________
	{%for c in clients %}
	# This is the call function of the client {{c.name}}. 
	# You can call this function, passing all the arguments of the 
	# service request declaration. This function will not be called 
	# automatically as you should call it to make a request. The 
	# function waits for the service to be available before going on and
	# the server's response is stored in a future object once the server
	# return the response. This function is the template of the client 
	# call and you should call it for applying requests.
	def client_call_{{c.name}}(self{%for r in c.requests %}, {{r }} {%endfor%}):
		# Wait for service
		while not self.client_{{c.name}}.wait_for_service(timeout_sec=1.0):
			self.get_logger().info('service not available, waiting again...')
		# Create request and fill it with data
		self.request_{{c.name}} = {{c.type}}.Request()
		{%for r in c.requests %}
		self.request_{{c.name}}.{{r}} = {{r}}
		{%endfor%}
		self.future_{{c.name}} = self.client_{{c.name}}.call_async(self.request_{{c.name}})
		# Result after server's response is stored in 
		{%for r in c.responses %}
		# self.future_{{c.name}}.result().{{r}} 
		{%endfor%}
	#_____
	{%endfor%}
		
		
		
# Main executable
#____________________________________________
# This is the main executable for the node {{node.name}}.
# Run this executable from the root of the workspace using the command:
# $ ros2 run {{pack.name}} {{node.name}}_exec
#
# This executable creates a node with all its features and spins it to
# wait for its callbacks.
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
# This is the executable for the client {{c.name}}.
# Run this executable from the root of the workspace using the command:
# $ ros2 run {{pack.name}} {{node.name}}_{{c.name}} arg1 arg2 ...
#
# This executable creates a node and call its client's call. It spins 
# the node until the response from the server is received.
def run_{{c.name}}(args=None):
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
#_____
{%endfor%}
	
if __name__ == '__main__':
	main()
