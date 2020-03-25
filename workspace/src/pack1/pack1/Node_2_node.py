
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
		self.suby1= self.create_subscription(ValueInt, 'topic/path', self.listener1, 10)
		self.suby1 
		
		timer_period = 0.5  # seconds
        
	def listener1(self, msg):
		self.get_logger().info('I heard: '+str(msg.x))
		self.suby2= self.create_subscription(ValueString, 'topic/path2', self.listener2, 10)
		self.suby2 
		
		timer_period = 0.5  # seconds
        
	def listener2(self, msg):
		self.get_logger().info('I heard: '+str(msg.x))
		
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
	
	
	
	#TODO add client code here
	
	rclpy.spin(Node_2)
	# Destroy the node explicitly
	# (optional - otherwise it will be done automatically
	# when the garbage collector destroys the node object)
	Node_2.destroy_node()
	rclpy.shutdown()
	
def Client1(args=None):
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
	
	
if __name__ == '__main__':
	main()