
# ~ node: Node_2

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


class Node_2_class(Node):

	def __init__(self):
		super().__init__('Node_2')
		# Publishers
		#____________________________________________
		
		# Subscribers
		#____________________________________________
		
		# Servers
		#____________________________________________
		
		# Clients
		#____________________________________________
		self.Client1= self.create_client(Addtwo, 'Addtwo_n')
		
		while not self.Client1.wait_for_service(timeout_sec=1.0):
			self.get_logger().info('service not available, waiting again...')
		self.req_Client1 = Addtwo.Request()
		
		
	def send_request_Client1(self):
		self.req_Client1.a = int(sys.argv[1])
		self.req_Client1.b = int(sys.argv[2])
		self.future_Client1 = self.Client1.call_async(self.req_Client1)


def main(args=None):
	rclpy.init(args=args)
	
	Node_2 = Node_2_class()
	
	Node_2.send_request_Client1()
	while rclpy.ok():
		rclpy.spin_once(Node_2)
		if Node_2.future_Client1.done():
			try:
				response = Node_2.future_Client1.result()
			except Exception as e:
				Node_2.get_logger().info('Service call failed %r' % (e,))
			else:
				Node_2.get_logger().info(
				'Result of add_three_ints: for %d + %d = %d' %
				(Node_2.req_Client1.a, Node_2.req_Client1.b, response.c))
			break
	
	
	#TODO add client code here
	
	
	# Destroy the node explicitly
	# (optional - otherwise it will be done automatically
	# when the garbage collector destroys the node object)
	Node_2.destroy_node()
	rclpy.shutdown()
	

if __name__ == '__main__':
	main()
