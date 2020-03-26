
# ~ node: node1

# ~ # ~ publisher name publy1
# ~ publisher path topic/path1
# ~ # ~ publisher name publy3
# ~ publisher path topic/path3
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


class node1_class(Node):

	def __init__(self):
		super().__init__('node1')
		# Publishers
		#____________________________________________
		self.publy1= self.create_publisher(ValueInt, 'topic/path1', 10)
		
		timer_period1 = 0.5  # seconds
		
		self.timer1 = self.create_timer(timer_period1, self.timer_callback1)
		self.i = 0
		
		
	def timer_callback1(self):
		msg = ValueInt()
		
		msg.x = self.i
		
		self.publy1.publish(msg)
		self.get_logger().info('Publishing: "%s"' % msg.x)
		self.i += 1

		self.publy3= self.create_publisher(ValueString, 'topic/path3', 10)
		
		timer_period2 = 0.3  # seconds
		
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
	
	node1 = node1_class()
	
	
	
	#TODO add client code here
	
	rclpy.spin(node1)
	# Destroy the node explicitly
	# (optional - otherwise it will be done automatically
	# when the garbage collector destroys the node object)
	node1.destroy_node()
	rclpy.shutdown()
	
	
if __name__ == '__main__':
	main()