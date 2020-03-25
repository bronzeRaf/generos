
# ~ node: Nodes_name

# ~ # ~ publisher name publy1
# ~ publisher path topic/path
# ~ # ~ publisher name publy3
# ~ publisher path topic/path2
# ~ 

# TODO messages

import rclpy
from rclpy.node import Node
import sys

from interfaces.msg import ValueInt
from interfaces.msg import ValueString
from interfaces.srv import Addtwo
from interfaces.srv import SrFloatFloatString
# ~ from std_msgs.msg import 
# ~ from example_interfaces.srv import AddTwoInts


class Nodes_name_class(Node):

	def __init__(self):
		super().__init__('Nodes_name')
		# Publishers
		#____________________________________________
		self.publy1= self.create_publisher(ValueInt, 'topic/path', 10)
		
		timer_period1 = 0.5  # seconds
		
		self.timer1 = self.create_timer(timer_period1, self.timer_callback1)
		self.i = 0
		
		
	def timer_callback1(self):
		msg = ValueInt()
		
		msg.x = self.i
		
		self.publy1.publish(msg)
		self.get_logger().info('Publishing: "%s"' % msg.x)
		self.i += 1

		self.publy3= self.create_publisher(ValueString, 'topic/path2', 10)
		
		timer_period2 = 0.8  # seconds
		
		self.timer2 = self.create_timer(timer_period2, self.timer_callback2)
		self.i = 0
		
		
	def timer_callback2(self):
		msg = ValueString()
		msg.x = 'Hello World: %d' % self.i
		
		
		self.publy3.publish(msg)
		self.get_logger().info('Publishing: "%s"' % msg.x)
		self.i += 1

		
		# Subscribers
		#____________________________________________
		
		# Servers
		#____________________________________________
		self.Server1= self.create_service(Addtwo, 'Addtwo_n', self.Server1_call)
		
	def Server1_call(self, request, response):
		response.c = request.a + request.b
		self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))
		return response

		
		# Clients
		#____________________________________________

def main(args=None):
	rclpy.init(args=args)
	
	Nodes_name = Nodes_name_class()
	
	
	
	#TODO add client code here
	
	rclpy.spin(Nodes_name)
	# Destroy the node explicitly
	# (optional - otherwise it will be done automatically
	# when the garbage collector destroys the node object)
	Nodes_name.destroy_node()
	rclpy.shutdown()
	
	
if __name__ == '__main__':
	main()