
from rclpy.qos import QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy, QoSLivelinessPolicy
from rclpy.qos import QoSProfile
from rclpy.qos import QoSPresetProfiles
from rcl_interfaces.msg import ParameterDescriptor

import rclpy
from rclpy.node import Node
import sys
# Imports for msg interfaces
from interfaces.msg import Velocities
# Imports for srv interfaces
# Imports for action interfaces
# Imports for msg inside custom interfaces
from std_msgs.msg import Header


# Class for the node motor 
class motor_class(Node):
	
	# Constructor function of the node
	def __init__(self):
				
		super().__init__('motor', namespace = '')		
		# Params
		#____________________________________________
		
		
		# Publishers
		#____________________________________________
		
		# Subscribers
		#____________________________________________
		# motion_subscriber
		# Qos profile
		qos_profile_motion_subscriber = QoSPresetProfiles.SYSTEM_DEFAULT.value
				
		self.subscriber_motion_subscriber = self.create_subscription(Velocities, 'actuators/velocities', self.subscriber_call_motion_subscriber, qos_profile = qos_profile_motion_subscriber)
		self.subscriber_motion_subscriber
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
	# This is the callback of the subscriber motion_subscriber. 
	# You can obtain the message from the variables set in this 
	# function, according to the instructions in the comments below. 
	# This function will be called automatically every time a message is
	# received. This function is the template of the subscriber callback 
	# and you should put your own functionality.
	def subscriber_call_motion_subscriber(self, msg):
		# Please obtain the message from the subscriber in this callback
		# The message definition could be found in the package: interfaces
		
		# Store the variables of the msg
		h = msg.h
		left_rpm = msg.left_rpm
		right_rpm = msg.right_rpm
		# Now you can use the received variables
		
		
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
# This is the main executable for the node motor.
# Run this executable from the root of the workspace using the command:
# $ ros2 run  motor_exec
#
# This executable creates a node with all its features and spins it to
# wait for its callbacks.
def main(args=None):
	rclpy.init(args=args)
	
	motor = motor_class()
		
	rclpy.spin(motor)
	# Destroy the node explicitly
	# (optional - otherwise it will be done automatically
	# when the garbage collector destroys the node object)
	motor.destroy_node()
	rclpy.shutdown()

# Clients executables
#____________________________________________
	
if __name__ == '__main__':
	main()