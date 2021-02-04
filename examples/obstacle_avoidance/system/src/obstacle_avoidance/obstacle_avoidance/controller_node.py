
from rclpy.qos import QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy, QoSLivelinessPolicy
from rclpy.qos import QoSProfile
from rclpy.qos import QoSPresetProfiles
from rcl_interfaces.msg import ParameterDescriptor

import rclpy
from rclpy.node import Node
import sys
# Imports for msg interfaces
from interfaces.msg import Velocities
from sensor_msgs.msg import Range
# Imports for srv interfaces
# Imports for action interfaces
# Imports for msg inside custom interfaces
from std_msgs.msg import Header


# Class for the node controller 
class controller_class(Node):
	
	# Constructor function of the node
	def __init__(self):
				
		super().__init__('controller', namespace = '')		
		# Params
		#____________________________________________
		
		
		# Publishers
		#____________________________________________
		# motion_publisher
		# Qos profile
		qos_profile_motion_publisher = QoSPresetProfiles.SYSTEM_DEFAULT.value
				
		self.publisher_motion_publisher = self.create_publisher(Velocities, 'actuators/velocities', qos_profile = qos_profile_motion_publisher)
		self.timer_motion_publisher = self.create_timer(0.2, self.publisher_call_motion_publisher)
		self.i = 0
		#_____
		
		# Subscribers
		#____________________________________________
		# left_sonar_subscriber
		# Qos profile
		qos_profile_left_sonar_subscriber = QoSPresetProfiles.SYSTEM_DEFAULT.value
				
		self.subscriber_left_sonar_subscriber = self.create_subscription(Range, 'sensors/range/left', self.subscriber_call_left_sonar_subscriber, qos_profile = qos_profile_left_sonar_subscriber)
		self.subscriber_left_sonar_subscriber
		#_____
		# right_sonar_subscriber
		# Qos profile
		qos_profile_right_sonar_subscriber = QoSPresetProfiles.SYSTEM_DEFAULT.value
				
		self.subscriber_right_sonar_subscriber = self.create_subscription(Range, 'sensors/range/right', self.subscriber_call_right_sonar_subscriber, qos_profile = qos_profile_right_sonar_subscriber)
		self.subscriber_right_sonar_subscriber
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
	# This is the callback of the publisher motion_publisher. 
	# You can store the message in the msg object attributes, according 
	# to the instructions in the comments below. This function will be 
	# called automatically with the chosen publish rate, to publish your 
	# messages. This function is the template of the publisher callback 
	# and you should put your own functionality.
	def publisher_call_motion_publisher(self):
		msg = Velocities()
		# Please create the message of the publisher in this callback
		# The message definition could be found in the package: interfaces
		
		# Some attributes of the message may be submessages and have special attributes
		# Message after calculactions should be stored in the attibutes:
		# msg.h 
		# msg.left_rpm 
		# msg.right_rpm 
		
		
		# TODO: Add functionality here
		
		
		# Then publish the msg with the following code
		self.publisher_motion_publisher.publish(msg)
		
	#_____
	
	# Subscribers
	#____________________________________________
	# This is the callback of the subscriber left_sonar_subscriber. 
	# You can obtain the message from the variables set in this 
	# function, according to the instructions in the comments below. 
	# This function will be called automatically every time a message is
	# received. This function is the template of the subscriber callback 
	# and you should put your own functionality.
	def subscriber_call_left_sonar_subscriber(self, msg):
		# Please obtain the message from the subscriber in this callback
		# The message definition could be found in the package: sensor_msgs
		
		# The message is type sensor_msgs/Range
		# Remember to obtain data from its attributes
		
		
		# TODO: Add functionality here
		
		# You can see incoming info uncommenting the following line and filling the attributes "msg" object
		# ~ self.get_logger().info('I heard: '+str(msg.<put your attributres>))
	#_____
	# This is the callback of the subscriber right_sonar_subscriber. 
	# You can obtain the message from the variables set in this 
	# function, according to the instructions in the comments below. 
	# This function will be called automatically every time a message is
	# received. This function is the template of the subscriber callback 
	# and you should put your own functionality.
	def subscriber_call_right_sonar_subscriber(self, msg):
		# Please obtain the message from the subscriber in this callback
		# The message definition could be found in the package: sensor_msgs
		
		# The message is type sensor_msgs/Range
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
# This is the main executable for the node controller.
# Run this executable from the root of the workspace using the command:
# $ ros2 run  controller_exec
#
# This executable creates a node with all its features and spins it to
# wait for its callbacks.
def main(args=None):
	rclpy.init(args=args)
	
	controller = controller_class()
		
	rclpy.spin(controller)
	# Destroy the node explicitly
	# (optional - otherwise it will be done automatically
	# when the garbage collector destroys the node object)
	controller.destroy_node()
	rclpy.shutdown()

# Clients executables
#____________________________________________
	
if __name__ == '__main__':
	main()