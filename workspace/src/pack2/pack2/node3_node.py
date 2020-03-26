
# ~ node: node3

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


class node3_class(Node):

	def __init__(self):
		super().__init__('node3')
		# Publishers
		#____________________________________________
		
		# Subscribers
		#____________________________________________
		self.suby1= self.create_subscription(ValueInt, 'topic/path1', self.listener1, 10)
		self.suby1 
		
		timer_period = 0.5  # seconds
        
	def listener1(self, msg):
		self.get_logger().info('I heard: '+str(msg.x))
		
		# Servers
		#____________________________________________
		
		# Clients
		#____________________________________________

def main(args=None):
	rclpy.init(args=args)
	
	node3 = node3_class()
	
	
	
	#TODO add client code here
	
	rclpy.spin(node3)
	# Destroy the node explicitly
	# (optional - otherwise it will be done automatically
	# when the garbage collector destroys the node object)
	node3.destroy_node()
	rclpy.shutdown()
	
	
if __name__ == '__main__':
	main()