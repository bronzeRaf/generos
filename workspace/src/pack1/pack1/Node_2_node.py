
# ~ node: Node_2

# ~ 

# TODO messages

import rclpy
from rclpy.node import Node

from interfaces.msg import ValueInt
from interfaces.msg import ValueString
from interfaces.srv import Addtwo
from interfaces.srv import SrFloatFloatString
# ~ from std_msgs.msg import 
# ~ from example_interfaces.srv import AddTwoInts


class Node_2_class(Node):

	def __init__(self):
		super().__init__('Node_2')
		# Publishers
		#____________________________________________
		
		# Subscribers
		#____________________________________________
		self.suby1= self.create_subscription(ValueInt, 'topic/path', self.listener1, 10)
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
	
	Node_2 = Node_2_class()
	
	
	#TODO add client code here
	
	rclpy.spin(Node_2)
	# Destroy the node explicitly
	# (optional - otherwise it will be done automatically
	# when the garbage collector destroys the node object)
	Node_2.destroy_node()
	rclpy.shutdown()
	

if __name__ == '__main__':
	main()