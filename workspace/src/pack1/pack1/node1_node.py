
from rclpy.qos import QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy, QoSLivelinessPolicy
from rclpy.qos import QoSProfile
from rclpy.qos import QoSPresetProfiles
from rcl_interfaces.msg import ParameterDescriptor

import rclpy
from rclpy.node import Node
import sys
# Imports for msg interfaces
from interfaces.msg import M1
# Imports for srv interfaces
# Imports for action interfaces
# Imports for msg inside custom interfaces
from std_msgs.msg import Header


# Class for the node node1 
class node1_class(Node):
	
	# Constructor function of the node
	def __init__(self):
				
		super().__init__('node1', namespace = '')		
		# Params
		#____________________________________________
		# p1  -  INTEGER_ARRAY
		# Description: 
		self.param_p1 = self.declare_parameter('p1', 32, descriptor=ParameterDescriptor(name='p1', type=7, description='', additional_constraints='', read_only=False, floating_point_range=[], integer_range=[]))
		# You can use your parameter p1 with type INTEGER_ARRAY
		# with 		self.get_parameter('p1')._value
		# You can also use your parameter from terminal or yaml file. 
		#_____
		
		
		# Publishers
		#____________________________________________
		
		# Subscribers
		#____________________________________________
		# sub1
		# Qos profile
		qos_profile_sub1 = QoSPresetProfiles.SYSTEM_DEFAULT.value
				
		self.subscriber_sub1 = self.create_subscription(M1, 'topic/path/1', self.subscriber_call_sub1, qos_profile = qos_profile_sub1)
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
		# The message definition could be found in the package: interfaces
		
		# Store the variables of the msg
		a = msg.a
		b = msg.b
		c = msg.c
		h = msg.h
		s = msg.s
		y = msg.y
		# Now you can use the received variables
		
		
		# TODO: Add functionality here
		
		
		self.get_logger().info('I heard: '+str(msg.x))
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