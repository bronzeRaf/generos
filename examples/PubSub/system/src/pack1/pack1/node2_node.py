
from rclpy.qos import QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy, QoSLivelinessPolicy
from rclpy.qos import QoSProfile
from rclpy.qos import QoSPresetProfiles
from rcl_interfaces.msg import ParameterDescriptor

import rclpy
from rclpy.node import Node
import sys
# Imports for msg interfaces
from std_msgs.msg import Header
# Imports for srv interfaces
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
		# sub1
		# Qos profile
		qos_profile_sub1 = QoSPresetProfiles.SYSTEM_DEFAULT.value
				
		self.subscriber_sub1 = self.create_subscription(Header, 'topic/path1', self.subscriber_call_sub1, qos_profile = qos_profile_sub1)
		self.subscriber_sub1
		#_____
		
		# Servers
		#____________________________________________
		
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
	# This is the callback of the subscriber sub1. 
	# You can obtain the message from the variables set in this 
	# function, according to the instructions in the comments below. 
	# This function will be called automatically every time a message is
	# received. This function is the template of the subscriber callback 
	# and you should put your own functionality.
	def subscriber_call_sub1(self, msg):
		# Please obtain the message from the subscriber in this callback
		# The message definition could be found in the package: std_msgs
		
		# The message is type std_msgs/Header
		# Remember to obtain data from its attributes
		
		
		# TODO: Add functionality here
		
		# You can see incoming info uncommenting the following line and filling the attributes "msg" object
		# ~ self.get_logger().info('I heard: '+str(msg.<put your attributres>))
	#_____
	
	# Servers
	#____________________________________________
		
	# Clients
	#____________________________________________
			
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
	
if __name__ == '__main__':
	main()