{# 
#This is a jinja2 template of a ROS2 Node
#
# Written in 13/3/2020
# Written by Rafael Brouzos
#}

# ~ node: {{node.name}}

# ~ {%for p in publishers %}
# ~ publisher name {{ p.name }}
# ~ publisher path {{p.topicPath}}
# ~ {%endfor%}


# TODO messages

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from example_interfaces.srv import AddTwoInts


class {{node.name}}_class(Node):

	def __init__(self):
		super().__init__('{{node.name}}')
		# Publishers
		#____________________________________________
		{%for p in publishers %}
		self.{{p.name}}= self.create_publisher(String, '{{p.topicPath}}', {{p.qos}})
		
		timer_period{{loop.index}} = {{p.publishRate}}  # seconds
		
		self.timer{{loop.index}} = self.create_timer(timer_period{{loop.index}}, self.timer_callback{{loop.index}})
		self.i = 0
		
		
	def timer_callback{{loop.index}}(self):
		msg = String()
		msg.data = 'Hello World: %d' % self.i
		self.{{p.name}}.publish(msg)
		self.get_logger().info('Publishing: "%s"' % msg.data)
		self.i += 1

		{%endfor%}
		
		# Subscribers
		#____________________________________________
		{%for s in subscribers %}
		self.{{s.name}}= self.create_subscription(String, '{{s.topicPath}}', self.listener{{loop.index}}, {{s.qos}})
		self.{{s.name}} 
		
		timer_period = 0.5  # seconds
        
	def listener{{loop.index}}(self, msg):
		self.get_logger().info('I heard: "%s"' % msg.data)

		{%endfor%}
		
		# Servers
		#____________________________________________
		{%for s in servers %}
		self.{{s.name}}= self.create_service({{s.type}}, '{{s.name}}', self.{{s.name}}_call)
		
	def {{s.name}}_call(self, request, response):
		response.sum = request.a + request.b
        self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))

        return response

		{%endfor%}
		
		# Clients
		#____________________________________________
		{%for c in clients %}
		self.{{c.name}}= self.create_client({{c.type}}, '{{c.name}}')
		
		 while not self.{{c.name}}.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req_{{c.name}} = {{c.type}}.Request()
		
		
    def send_request_{{c.name}}(self):
        self.req_{{c.name}}.a = int(sys.argv[1])
        self.req_{{c.name}}.b = int(sys.argv[2])
        self.future_{{c.name}} = self.{{c.name}}.call_async(self.req_{{c.name}})

		{%endfor%}

def main(args=None):
	rclpy.init(args=args)
	
	{{node.name}} = {{node.name}}_class()
	
	{%for c in clients %}
	{{node.name}}.send_request_{{c.name}}()
	{%endfor%}
	
	#TODO add client code here
	
	rclpy.spin({{node.name}})
	# Destroy the node explicitly
	# (optional - otherwise it will be done automatically
	# when the garbage collector destroys the node object)
	{{node.name}}.destroy_node()
	rclpy.shutdown()
	

if __name__ == '__main__':
	main()
