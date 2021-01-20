
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


# Class for the node node1 
class node1_class(Node):
	
	# Constructor function of the node
	def __init__(self):
				
		super().__init__('node1', namespace = '')		
		# Params
		#____________________________________________
		
		
		# Publishers
		#____________________________________________
		
		# Subscribers
		#____________________________________________
		
		# Servers
		#____________________________________________
		# serv1
		# Qos profile
		qos_profile_serv1 = QoSPresetProfiles.SERVICES_DEFAULT.value
				
		self.server_serv1 = self.create_service(SetBool, 'service1', self.server_call_serv1, qos_profile = qos_profile_serv1)
		#_____
		
		# Clients
		#____________________________________________
		
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
	# This is the callback of the server serv1. 
	# You can obtain the request to the server from the variables set in 
	# this function, according to the instructions in the comments 
	# below. This function will be called automatically every time a 
	# request is received. This function is the template of the server 
	# callback and you should put your own functionality.
	def server_call_serv1(self, request, response):
		# Please add the server's functionality in this callback
		# The service is type std_srvs/SetBool
		# Remember to store data in its attributes
		
		
		# TODO: Add functionality here
		
		# You can store the result uncommenting the following line and filling the attributes of the "response" object 
		# ~ response.<put your attributres> = <put your values> 
		
		# You can see incoming info uncommenting the following line and filling the attributes "request" object
		# ~ self.get_logger().info('Incoming request\nvalue 1: '+ str(request.<put your attributres>)+' value 2: '+str(request.<put your attributres>))
		
		# Finally forward the response
		return response
	#_____
		
	# Clients
	#____________________________________________
			
	# Action Servers
	#____________________________________________
	
	# Action Clients
	#____________________________________________
		
		
# Main executable
#____________________________________________
# This is the main executable for the node node1.
# Run this executable from the root of the workspace using the command:
# $ ros2 run  node1_exec
#
# This executable creates a node with all its features and spins it to
# wait for its callbacks.
def main(args=None):
	rclpy.init(args=args)
	
	node1 = node1_class()
		
	rclpy.spin(node1)
	# Destroy the node explicitly
	# (optional - otherwise it will be done automatically
	# when the garbage collector destroys the node object)
	node1.destroy_node()
	rclpy.shutdown()

# Clients executables
#____________________________________________
	
if __name__ == '__main__':
	main()