
# ~ node: Nodes_name

# ~ # ~ publisher name publy1
# ~ publisher path topic/path
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

		
		# Subscribers
		#____________________________________________
		
		# Servers
		#____________________________________________
		
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