
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


# Class for the node node2 
class node2_class(Node):
	
	# Constructor function of the node
	def __init__(self):
				
		super().__init__('node2', namespace = 'name/space2')		
		# Params
		#____________________________________________
		
		
		# Publishers
		#____________________________________________
		# pub1
		# Qos profile
		qos_profile_pub1 = QoSPresetProfiles.SYSTEM_DEFAULT.value
				
		self.publisher_pub1 = self.create_publisher(M1, 'topic/path/1', qos_profile = qos_profile_pub1)
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
		msg = M1()
		# Please create the message of the publisher in this callback
		# The message definition could be found in the package: interfaces
		
		# Some attributes of the message may be submessages and have special attributes
		# Message after calculactions should be stored in the attibutes:
		# msg.a 
		# msg.b 
		# msg.c 
		# msg.h 
		# msg.s 
		# msg.y 
		
		
		# TODO: Add functionality here
		
		
		
		
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