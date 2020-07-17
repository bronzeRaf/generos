
from rclpy.qos import QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy, QoSLivelinessPolicy
from rclpy.qos import QoSProfile
from rclpy.qos import QoSPresetProfiles
from rcl_interfaces.msg import ParameterDescriptor

import rclpy
from rclpy.node import Node
import sys
# Imports for msg interfaces
from interfaces.msg import Distance
# Imports for srv interfaces
# Imports for action interfaces
# Imports for msg inside custom interfaces
from std_msgs.msg import Header


# Class for the node sonar2 
class sonar2_class(Node):
	
	# Constructor function of the node
	def __init__(self):
				
		super().__init__('sonar2', namespace = '')		
		# Params
		#____________________________________________
		
		
		# Publishers
		#____________________________________________
		# toCpu2
		# Qos profile
		qos_profile_toCpu2 = QoSProfile(history=QoSHistoryPolicy.KEEP_LAST, durability = QoSDurabilityPolicy.SYSTEM_DEFAULT,reliability = QoSReliabilityPolicy.SYSTEM_DEFAULT,depth =15)
		# Additional qos settings
		qos_profile_toCpu2.liveliness = QoSLivelinessPolicy.SYSTEM_DEFAULT
		qos_profile_toCpu2.deadline.sec = 0
		qos_profile_toCpu2.deadline.nsec = 0
		qos_profile_toCpu2.lifespan.sec = 0
		qos_profile_toCpu2.lifespan.nsec = 0
		qos_profile_toCpu2.liveliness_lease_duration.sec = 0
		qos_profile_toCpu2.liveliness_lease_duration.nsec = 0
		qos_profile_toCpu2.avoid_ros_namespace_conventions = False
				
		self.publisher_toCpu2 = self.create_publisher(Distance, 'topic/path/s2', qos_profile = qos_profile_toCpu2)
		self.timer_toCpu2 = self.create_timer(0.5, self.publisher_call_toCpu2)
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
	# This is the callback of the publisher toCpu2. 
	# You can store the message in the msg object attributes, according 
	# to the instructions in the comments below. This function will be 
	# called automatically with the chosen publish rate, to publish your 
	# messages. This function is the template of the publisher callback 
	# and you should put your own functionality.
	def publisher_call_toCpu2(self):
		msg = Distance()
		# Please create the message of the publisher in this callback
		# The message definition could be found in the package: interfaces
		
		# Some attributes of the message may be submessages and have special attributes
		# Message after calculactions should be stored in the attibutes:
		# msg.h 
		# msg.range 
		
		
		# TODO: Add functionality here
		
		
		# Then publish the msg with the following code
		self.publisher_toCpu2.publish(msg)
		
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
# This is the main executable for the node sonar2.
# Run this executable from the root of the workspace using the command:
# $ ros2 run  sonar2_exec
#
# This executable creates a node with all its features and spins it to
# wait for its callbacks.
def main(args=None):
	rclpy.init(args=args)
	
	sonar2 = sonar2_class()
		
	rclpy.spin(sonar2)
	# Destroy the node explicitly
	# (optional - otherwise it will be done automatically
	# when the garbage collector destroys the node object)
	sonar2.destroy_node()
	rclpy.shutdown()

# Clients executables
#____________________________________________
	
if __name__ == '__main__':
	main()