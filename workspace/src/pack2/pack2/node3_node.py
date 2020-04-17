import rclpy
from rclpy.node import Node
import sys
# Imports for msg interfaces
from std_msgs.msg import Header
# Imports for srv interfaces
from interfaces.srv import SrFloatFloatString
# Imports for action interfaces
# Imports for msg inside custom interfaces


# Class for the node node3 
class node3_class(Node):
	
	# Constructor function of the node
	def __init__(self):
		super().__init__('node3')
		# Params
		#____________________________________________
		
		
		# Publishers
		#____________________________________________
		
		# Subscribers
		#____________________________________________
		# suby3
		self.subscriber_suby3 = self.create_subscription(Header, 'topic/path3', self.subscriber_call_suby3, 10)
		self.subscriber_suby3
		#_____
		
		# Servers
		#____________________________________________
		
		# Clients
		#____________________________________________
		# Client2
		self.client_Client2 = self.create_client(SrFloatFloatString, 'str')
		#_____
		
		# Action Servers
		#____________________________________________
		
		# Action Clients
		#____________________________________________
		
		
		
	# ************Callbacks************
	# Publishers
	#____________________________________________
	
	# Subscribers
	#____________________________________________
	# This is the callback of the subscriber suby3. 
	# You can obtain the message from the variables set in this 
	# function, according to the instructions in the comments below. 
	# This function will be called automatically every time a message is
	# received. This function is the template of the subscriber callback 
	# and you should put your own functionality.
	def subscriber_call_suby3(self, msg):
		# Please obtain the message from the subscriber in this callback
		# Store the variables of the msg
		# Now you can use the received variables
		self.get_logger().info('I heard: '+str(msg.x))
	#_____
	
	#Servers
	#____________________________________________
		
	# Clients
	#____________________________________________
	# This is the call function of the client Client2. 
	# You can call this function, passing all the arguments of the 
	# service request declaration. This function will not be called 
	# automatically as you should call it to make a request. The 
	# function waits for the service to be available before going on and
	# the server's response is stored in a future object once the server
	# return the response. This function is the template of the client 
	# call and you should call it for applying requests.
	def client_call_Client2(self, x, y):
		# Wait for service
		while not self.client_Client2.wait_for_service(timeout_sec=1.0):
			self.get_logger().info('service not available, waiting again...')
		# Create request and fill it with data
		self.request_Client2 = SrFloatFloatString.Request()
		self.request_Client2.x = x
		self.request_Client2.y = y
		self.future_Client2 = self.client_Client2.call_async(self.request_Client2)
		# Result after server's response is stored in 
		# self.future_Client2.result().z 
	#_____
			
	# Action Servers
	#____________________________________________
	
	# Action Clients
	#____________________________________________
		
		
# Main executable
#____________________________________________
# This is the main executable for the node node3.
# Run this executable from the root of the workspace using the command:
# $ ros2 run  node3_exec
#
# This executable creates a node with all its features and spins it to
# wait for its callbacks.
def main(args=None):
	rclpy.init(args=args)
	
	node3 = node3_class()
		
	rclpy.spin(node3)
	# Destroy the node explicitly
	# (optional - otherwise it will be done automatically
	# when the garbage collector destroys the node object)
	node3.destroy_node()
	rclpy.shutdown()

# Clients executables
#____________________________________________
# This is the executable for the client Client2.
# Run this executable from the root of the workspace using the command:
# $ ros2 run  node3_Client2 arg1 arg2 ...
#
# This executable creates a node and call its client's call. It spins 
# the node until the response from the server is received.
def run_Client2(args=None):
	rclpy.init(args=args)
	
	node3 = node3_class()
	#TODO create typecast from command line to client call type (change int to custom type)
	node3.client_call_Client2(int(sys.argv[1]), int(sys.argv[2]))
	while rclpy.ok():
		rclpy.spin_once(node3)
		if node3.future_Client2.done():
			try:
				response = node3.future_Client2.result()
			except Exception as e:
				node3.get_logger().info('Service call failed %r' % (e,))
			else:
				node3.get_logger().info(
				'Result of add_three_ints: for %d + %d = %d' %
				(node3.request_Client2.a, node3.request_Client2.b, response.c))
			break
#_____
	
if __name__ == '__main__':
	main()