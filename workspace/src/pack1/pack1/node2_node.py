
import rclpy
from rclpy.node import Node
import sys


from interfaces.msg import ValueInt


from interfaces.srv import Addtwo
from std_srvs.srv import SetBool
#*********
# ~ # ~ from interfaces.msg import ValueInt
# ~ # ~ from interfaces.msg import ValueString
# ~ # ~ # ~ from interfaces.srv import Addtwo
# ~ # ~ from interfaces.srv import SrFloatFloatString
# ~ # ~ from std_msgs.msg import 
# ~ from example_interfaces.srv import AddTwoInts

# Class for the node node2 
class node2_class(Node):
	
	# Constructor function of the node
	def __init__(self):
		super().__init__('node2')
		# Publishers
		#____________________________________________
		
		# Subscribers
		#____________________________________________
		# suby2
		self.subscriber_suby2= self.create_subscription(ValueInt, 'topic/path2', self.subscriber_call_suby2, 10)
		self.subscriber_suby2
		#_____
		
		# Servers
		#____________________________________________
		
		# Clients
		#____________________________________________
		# Client1
		self.client_Client1= self.create_client(Addtwo, 'add_two')
		#_____
		# Client3
		self.client_Client3= self.create_client(SetBool, 'set_bool')
		#_____
		
		
	# ************Callbacks************
	# Publishers
	#____________________________________________
	
	# Subscribers
	#____________________________________________
	# This is the callback of the subscriber suby2. 
	# You can obtain the message from the variables set in this 
	# function, according to the instructions in the comments below. 
	# This function will be called automatically every time a message is
	# received. This function is the template of the subscriber callback 
	# and you should put your own functionality.
	def subscriber_call_suby2(self, msg):
		# Please obtain the message from the subscriber in this callback
		# Store the variables of the msg
		x = msg.x
		# Now you can use the received variables
		self.get_logger().info('I heard: '+str(msg.x))
	#_____
	
	#Servers
	#____________________________________________
		
	# Clients
	#____________________________________________
	# This is the call function of the client Client1. 
	# You can call this function, passing all the arguments of the 
	# service request declaration. This function will not be called 
	# automatically as you should call it to make a request. The 
	# function waits for the service to be available before going on and
	# the server's response is stored in a future object once the server
	# return the response. This function is the template of the client 
	# call and you should call it for applying requests.
	def client_call_Client1(self, a, b):
		# Wait for service
		while not self.client_Client1.wait_for_service(timeout_sec=1.0):
			self.get_logger().info('service not available, waiting again...')
		# Create request and fill it with data
		self.request_Client1 = Addtwo.Request()
		self.request_Client1.a = a
		self.request_Client1.b = b
		self.future_Client1 = self.client_Client1.call_async(self.request_Client1)
		# Result after server's response is stored in 
		# self.future_Client1.result().c 
	#_____
	# This is the call function of the client Client3. 
	# You can call this function, passing all the arguments of the 
	# service request declaration. This function will not be called 
	# automatically as you should call it to make a request. The 
	# function waits for the service to be available before going on and
	# the server's response is stored in a future object once the server
	# return the response. This function is the template of the client 
	# call and you should call it for applying requests.
	def client_call_Client3(self):
		# Wait for service
		while not self.client_Client3.wait_for_service(timeout_sec=1.0):
			self.get_logger().info('service not available, waiting again...')
		# Create request and fill it with data
		self.request_Client3 = SetBool.Request()
		self.future_Client3 = self.client_Client3.call_async(self.request_Client3)
		# Result after server's response is stored in 
	#_____
		
		
		
# Main executable
#____________________________________________
# This is the main executable for the node node2.
# Run this executable from the root of the workspace using the command:
# $ ros2 run  node2_exec
#
# This executable creates a node with all its features and spins it to
# wait for its callbacks.
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
# This is the executable for the client Client1.
# Run this executable from the root of the workspace using the command:
# $ ros2 run  node2_Client1 arg1 arg2 ...
#
# This executable creates a node and call its client's call. It spins 
# the node until the response from the server is received.
def run_Client1(args=None):
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
#_____
# This is the executable for the client Client3.
# Run this executable from the root of the workspace using the command:
# $ ros2 run  node2_Client3 arg1 arg2 ...
#
# This executable creates a node and call its client's call. It spins 
# the node until the response from the server is received.
def run_Client3(args=None):
	rclpy.init(args=args)
	
	node2 = node2_class()
	#TODO create typecast from command line to client call type (change int to custom type)
	node2.client_call_Client3()
	while rclpy.ok():
		rclpy.spin_once(node2)
		if node2.future_Client3.done():
			try:
				response = node2.future_Client3.result()
			except Exception as e:
				node2.get_logger().info('Service call failed %r' % (e,))
			else:
				node2.get_logger().info(
				'Result of add_three_ints: for %d + %d = %d' %
				(node2.request_Client3.a, node2.request_Client3.b, response.c))
			break
#_____
	
if __name__ == '__main__':
	main()