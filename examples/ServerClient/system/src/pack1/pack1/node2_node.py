
from rclpy.qos import QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy, QoSLivelinessPolicy
from rclpy.qos import QoSProfile
from rclpy.qos import QoSPresetProfiles
from rcl_interfaces.msg import ParameterDescriptor

import rclpy
from rclpy.node import Node
import sys
# Imports for msg interfaces
# Imports for srv interfaces
from std_srvs.srv import SetBool
# Imports for action interfaces
# Imports for msg inside custom interfaces


# Class for the node node2 
class node2_class(Node):
	
	# Constructor function of the node
	def __init__(self):
				
		super().__init__('node2', namespace = '')		
		# Params
		#____________________________________________
		
		
		# Publishers
		#____________________________________________
		
		# Subscribers
		#____________________________________________
		
		# Servers
		#____________________________________________
		
		# Clients
		#____________________________________________
		# cli1
		# Qos profile
		qos_profile_cli1 = QoSPresetProfiles.SERVICES_DEFAULT.value
				
		self.client_cli1 = self.create_client(SetBool, 'service1', qos_profile = qos_profile_cli1)
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
	
	# Servers
	#____________________________________________
		
	# Clients
	#____________________________________________
	# This is the call function of the client cli1. 
	# You can call this function, passing all the arguments of the 
	# service request declaration (if the service is a Custom Service). 
	# This function will not be called automatically as you should call 
	# it to make a request. The function waits for the service to be 
	# available before going on and the server's response is stored in 
	# a future object once the server returns the response. This 
	# function is the template of the client call and you should call 
	# it for applying requests. Remember to change the arguments of the 
	# function based on the service you use.
	def client_call_cli1(self):
		# Wait for service
		while not self.client_cli1.wait_for_service(timeout_sec=1.0):
			self.get_logger().info('service not available, waiting again...')
		# Create request and fill it with data
		self.request_cli1 = SetBool.Request()
		# The service is type std_srvs/SetBool
		# Remember to store data in the attributes of self.request_cli1
		self.future_cli1 = self.client_cli1.call_async(self.request_cli1)
		# Result after server's response is stored in 
		
		
		# TODO: Add functionality here
		
		
	#_____
			
	# Action Servers
	#____________________________________________
	
	# Action Clients
	#____________________________________________
		
		
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
# This is the executable for the client cli1.
# Run this executable from the root of the workspace using the command:
# $ ros2 run  node2_cli1 arg1 arg2 ...
#
# This executable creates a node and call its client's call. It spins 
# the node until the response from the server is received.
def run_cli1(args=None):
	rclpy.init(args=args)
	
	node2 = node2_class()
	#TODO create typecast from command line to client call type (change int to custom type)
	node2.client_call_cli1(int(sys.argv[1]) )
	while rclpy.ok():
		rclpy.spin_once(node2)
		if node2.future_cli1.done():
			try:
				response = node2.future_cli1.result()
			except Exception as e:
				node2.get_logger().info('Service call failed %r' % (e,))
			else:
				node2.get_logger().info(
				'Result of add_three_ints: for %d + %d = %d' %
				(node2.request_cli1.a, node2.request_cli1.b, response.c))
			break
#_____
	
if __name__ == '__main__':
	main()