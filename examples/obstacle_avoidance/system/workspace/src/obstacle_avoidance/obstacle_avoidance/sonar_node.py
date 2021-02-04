
from rclpy.qos import QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy, QoSLivelinessPolicy
from rclpy.qos import QoSProfile
from rclpy.qos import QoSPresetProfiles
from rcl_interfaces.msg import ParameterDescriptor

import rclpy
from rclpy.node import Node
import sys
# Imports for msg interfaces
from sensor_msgs.msg import Range
# Imports for srv interfaces
# Imports for action interfaces
# Imports for msg inside custom interfaces


# Class for the node sonar 
class sonar_class(Node):
	
	# Constructor function of the node
	def __init__(self):
				
		super().__init__('sonar', namespace = '')		
		# Params
		#____________________________________________
		
		
		# Publishers
		#____________________________________________
		# left_sonar_publisher
		# Qos profile
		qos_profile_left_sonar_publisher = QoSPresetProfiles.SYSTEM_DEFAULT.value
				
		self.publisher_left_sonar_publisher = self.create_publisher(Range, 'sensors/range/left', qos_profile = qos_profile_left_sonar_publisher)
		self.timer_left_sonar_publisher = self.create_timer(0.2, self.publisher_call_left_sonar_publisher)
		self.i = 0
		#_____
		# right_sonar_publisher
		# Qos profile
		qos_profile_right_sonar_publisher = QoSPresetProfiles.SYSTEM_DEFAULT.value
				
		self.publisher_right_sonar_publisher = self.create_publisher(Range, 'sensors/range/right', qos_profile = qos_profile_right_sonar_publisher)
		self.timer_right_sonar_publisher = self.create_timer(0.2, self.publisher_call_right_sonar_publisher)
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
	# This is the callback of the publisher left_sonar_publisher. 
	# You can store the message in the msg object attributes, according 
	# to the instructions in the comments below. This function will be 
	# called automatically with the chosen publish rate, to publish your 
	# messages. This function is the template of the publisher callback 
	# and you should put your own functionality.
	def publisher_call_left_sonar_publisher(self):
		msg = Range()
		# Please create the message of the publisher in this callback
		# The message definition could be found in the package: sensor_msgs
		
		# The message is type sensor_msgs/Range
		# Remember to store data in its attributes before publishing
		
		
		# TODO: Add functionality here
		
		
		# Then publish the msg with the following code
		self.publisher_left_sonar_publisher.publish(msg)
		
	#_____
	# This is the callback of the publisher right_sonar_publisher. 
	# You can store the message in the msg object attributes, according 
	# to the instructions in the comments below. This function will be 
	# called automatically with the chosen publish rate, to publish your 
	# messages. This function is the template of the publisher callback 
	# and you should put your own functionality.
	def publisher_call_right_sonar_publisher(self):
		msg = Range()
		# Please create the message of the publisher in this callback
		# The message definition could be found in the package: sensor_msgs
		
		# The message is type sensor_msgs/Range
		# Remember to store data in its attributes before publishing
		
		
		# TODO: Add functionality here
		
		
		# Then publish the msg with the following code
		self.publisher_right_sonar_publisher.publish(msg)
		
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
# This is the main executable for the node sonar.
# Run this executable from the root of the workspace using the command:
# $ ros2 run  sonar_exec
#
# This executable creates a node with all its features and spins it to
# wait for its callbacks.
def main(args=None):
	rclpy.init(args=args)
	
	sonar = sonar_class()
		
	rclpy.spin(sonar)
	# Destroy the node explicitly
	# (optional - otherwise it will be done automatically
	# when the garbage collector destroys the node object)
	sonar.destroy_node()
	rclpy.shutdown()

# Clients executables
#____________________________________________
	
if __name__ == '__main__':
	main()