
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


# Class for the node node1 
class node1_class(Node):
	
	# Constructor function of the node
	def __init__(self):
				
		super().__init__('node1', namespace = '')		
		# Params
		#____________________________________________
		
		
		# Publishers
		#____________________________________________
		# pub1
		# Qos profile
		qos_profile_pub1 = QoSPresetProfiles.SYSTEM_DEFAULT.value
				
		self.publisher_pub1 = self.create_publisher(Header, 'topic/path1', qos_profile = qos_profile_pub1)
		self.timer_pub1 = self.create_timer(10.0, self.publisher_call_pub1)
		self.i = 0
		#_____
		
		# Subscribers
		#____________________________________________
		
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
	# This is the callback of the publisher pub1. 
	# You can store the message in the msg object attributes, according 
	# to the instructions in the comments below. This function will be 
	# called automatically with the chosen publish rate, to publish your 
	# messages. This function is the template of the publisher callback 
	# and you should put your own functionality.
	def publisher_call_pub1(self):
		msg = Header()
		# Please create the message of the publisher in this callback
		# The message definition could be found in the package: std_msgs
		
		# The message is type std_msgs/Header
		# Remember to store data in its attributes before publishing
		
		
		# TODO: Add functionality here
		
		
		# Then publish the msg with the following code
		self.publisher_pub1.publish(msg)
		
	#_____
	
	# Subscribers
	#____________________________________________
	
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