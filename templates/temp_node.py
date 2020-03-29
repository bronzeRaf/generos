{# 
#This is a jinja2 template of a ROS2 Node
#
# Written in 13/3/2020
# Written by Rafael Brouzos
#}

import rclpy
from rclpy.node import Node
import sys

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
		self.{{p.name}}= self.create_publisher({{p.type}}, '{{p.topicPath}}', {{p.qos}})
		timer_period{{loop.index}} = {{p.publishRate}}  # seconds
		self.timer{{loop.index}} = self.create_timer(timer_period{{loop.index}}, self.timer_callback{{loop.index}})
		self.i = 0
		{%endfor%}
		
		# Subscribers
		#____________________________________________
		{%for s in subscribers %}
		self.{{s.name}}= self.create_subscription({{s.type}}, '{{s.topicPath}}', self.listener{{loop.index}}, {{s.qos}})
		self.{{s.name}} 
		{%endfor%}
		
		# Servers
		#____________________________________________
		{%for s in servers %}
		self.{{s.name}}= self.create_service({{s.type}}, '{{s.type}}_n', self.{{s.name}}_call)
		{%endfor%}
		
		# Clients
		#____________________________________________
		{%for c in clients %}
		self.{{c.name}}= self.create_client({{c.type}}, '{{c.type}}_n')
		while not self.{{c.name}}.wait_for_service(timeout_sec=1.0):
			self.get_logger().info('service not available, waiting again...')
		{%endfor%}
		
		
	# Calls
	#____________________________________________
	# Publishers
	{%for p in publishers %}
	def timer_callback{{loop.index}}(self):
		msg = {{p.type}}()
		{% if p.type == "ValueString" %}
		msg.x = 'Hello World: %d' % self.i
		{% endif %}
		
		{% if p.type == "ValueInt" %}
		msg.x = self.i
		{% endif %}
		
		self.{{p.name}}.publish(msg)
		self.get_logger().info('Publishing: "%s"' % msg.x)
		self.i += 1
	{%endfor%}
	
	# Subscribers
	{%for s in subscribers %}
	def listener{{loop.index}}(self, msg):
		#TODO variables set here
		self.get_logger().info('I heard: '+str(msg.x))
	{%endfor%}
	
	#Servers
	{%for s in servers %}
	def {{s.name}}_call(self, request, response):
		#TODO variables set here
		response.c = request.a + request.b
		self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))
		return response
	{%endfor%}
		
	# Clients
	{%for c in clients %}
	def send_request_{{c.name}}(self):
		self.req_{{c.name}}.a = int(sys.argv[1])
		self.req_{{c.name}}.b = int(sys.argv[2])
		self.future_{{c.name}} = self.{{c.name}}.call_async(self.req_{{c.name}})
	{%endfor%}
		
		
		
		
def main(args=None):
	rclpy.init(args=args)
	
	{{node.name}} = {{node.name}}_class()
		
	rclpy.spin({{node.name}})
	# Destroy the node explicitly
	# (optional - otherwise it will be done automatically
	# when the garbage collector destroys the node object)
	{{node.name}}.destroy_node()
	rclpy.shutdown()
	
{%for c in clients %}
def {{c.name}}(args=None):
	rclpy.init(args=args)
	
	{{node.name}} = {{node.name}}_class()
	{{node.name}}.send_request_{{c.name}}()
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
				({{node.name}}.req_{{c.name}}.a, {{node.name}}.req_{{c.name}}.b, response.c))
			break
	
{%endfor%}
	
if __name__ == '__main__':
	main()
