
import rclpy
from rclpy.node import Node
import sys


from std_msgs.msg import Int32

#*********
from interfaces.msg import ValueInt
from interfaces.msg import ValueString
from interfaces.srv import Addtwo
from interfaces.srv import SrFloatFloatString
# ~ from std_msgs.msg import 
# ~ from example_interfaces.srv import AddTwoInts


class node2_class(Node):

	def __init__(self):
		super().__init__('node2')
		# Publishers
		#____________________________________________
		
		# Subscribers
		#____________________________________________
		self.subscriber_suby2= self.create_subscription(Int32, 'topic/path2', self.subscriber_call_suby2, 10)
		self.subscriber_suby2
		#____________________________________________
		
		# Servers
		#____________________________________________
		
		# Clients
		#____________________________________________
		self.client_Client1= self.create_client(Addtwo, 'add_two')
		#____________________________________________
		
		
	# ************Calls************
	# Publishers
	#____________________________________________
	
	# Subscribers
	#____________________________________________
	def subscriber_call_suby2(self, msg):
		# Store the variables of the msg
		self.get_logger().info('I heard: '+str(msg.data))
	#____________________________________________
	
	#Servers
	#____________________________________________
		
	# Clients
	#____________________________________________
	def client_call_Client1(self, a, b):
		while not self.client_Client1.wait_for_service(timeout_sec=1.0):
			self.get_logger().info('service not available, waiting again...')
		self.request_Client1 = Addtwo.Request()
		self.request_Client1.a = a
		self.request_Client1.b = b
		self.future_Client1 = self.client_Client1.call_async(self.request_Client1)
		# Result after server's response is stored in 
		# self.future_Client1.result().c 
	#____________________________________________
		
		
		
# Main executable
#____________________________________________
def main(args=None):
	rclpy.init(args=args)
	
	node2 = node2_class()
		
	rclpy.spin(node2)
	# Destroy the node explicitly
	# (optional - otherwise it will be done automatically
	# when the garbage collector destroys the node object)
	node2.destroy_node()
	rclpy.shutdown()

# Clients executables
#____________________________________________
def Client1(args=None):
	rclpy.init(args=args)
	
	node2 = node2_class()
	#TODO create typecast from command line to client call type (change int to custom type)
	node2.client_call_Client1(int(sys.argv[1]), int(sys.argv[2]))
	while rclpy.ok():
		rclpy.spin_once(node2)
		if node2.future_Client1.done():
			try:
				response = node2.future_Client1.result()
			except Exception as e:
				node2.get_logger().info('Service call failed %r' % (e,))
			else:
				node2.get_logger().info(
				'Result of add_three_ints: for %d + %d = %d' %
				(node2.request_Client1.a, node2.request_Client1.b, response.c))
			break
	
	
if __name__ == '__main__':
	main()
