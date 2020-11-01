
from rclpy.qos import QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy, QoSLivelinessPolicy
from rclpy.qos import QoSProfile
from rclpy.qos import QoSPresetProfiles
from rcl_interfaces.msg import ParameterDescriptor

import rclpy
from rclpy.node import Node
import sys
# Imports for msg interfaces
from geometry_msgs.msg import Twist
from interfaces.msg import Distance
# Imports for srv interfaces
# Imports for action interfaces
# Imports for msg inside custom interfaces
from std_msgs.msg import Header


# Class for the node cpu 
class cpu_class(Node):
	
	# Constructor function of the node
	def __init__(self):
				
		super().__init__('cpu', namespace = '')		
		# Params
		#____________________________________________
		
		
		# Publishers
		#____________________________________________
		# toActuators
		# Qos profile
		qos_profile_toActuators = QoSPresetProfiles.SYSTEM_DEFAULT.value
				
		self.publisher_toActuators = self.create_publisher(Twist, 'topic/path/act', qos_profile = qos_profile_toActuators)
		self.timer_toActuators = self.create_timer(0.5, self.publisher_call_toActuators)
		self.i = 0
		#_____
		
		# Subscribers
		#____________________________________________
		# fromSonar1
		# Qos profile
		qos_profile_fromSonar1 = QoSProfile(history = QoSHistoryPolicy.KEEP_LAST, durability = QoSDurabilityPolicy.SYSTEM_DEFAULT, reliability = QoSReliabilityPolicy.SYSTEM_DEFAULT, depth =15)
		# Additional qos settings
		qos_profile_fromSonar1.liveliness = QoSLivelinessPolicy.SYSTEM_DEFAULT
		qos_profile_fromSonar1.deadline.sec = 0
		qos_profile_fromSonar1.deadline.nsec = 0
		qos_profile_fromSonar1.lifespan.sec = 0
		qos_profile_fromSonar1.lifespan.nsec = 0
		qos_profile_fromSonar1.liveliness_lease_duration.sec = 0
		qos_profile_fromSonar1.liveliness_lease_duration.nsec = 0
		qos_profile_fromSonar1.avoid_ros_namespace_conventions = False
				
		self.subscriber_fromSonar1 = self.create_subscription(Distance, 'topic/path/s1', self.subscriber_call_fromSonar1, qos_profile = qos_profile_fromSonar1)
		self.subscriber_fromSonar1
		#_____
		# fromSonar2
		# Qos profile
		qos_profile_fromSonar2 = QoSProfile(history = QoSHistoryPolicy.KEEP_LAST, durability = QoSDurabilityPolicy.SYSTEM_DEFAULT, reliability = QoSReliabilityPolicy.SYSTEM_DEFAULT, depth =15)
		# Additional qos settings
		qos_profile_fromSonar2.liveliness = QoSLivelinessPolicy.SYSTEM_DEFAULT
		qos_profile_fromSonar2.deadline.sec = 0
		qos_profile_fromSonar2.deadline.nsec = 0
		qos_profile_fromSonar2.lifespan.sec = 0
		qos_profile_fromSonar2.lifespan.nsec = 0
		qos_profile_fromSonar2.liveliness_lease_duration.sec = 0
		qos_profile_fromSonar2.liveliness_lease_duration.nsec = 0
		qos_profile_fromSonar2.avoid_ros_namespace_conventions = False
				
		self.subscriber_fromSonar2 = self.create_subscription(Distance, 'topic/path/s2', self.subscriber_call_fromSonar2, qos_profile = qos_profile_fromSonar2)
		self.subscriber_fromSonar2
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
	# This is the callback of the publisher toActuators. 
	# You can store the message in the msg object attributes, according 
	# to the instructions in the comments below. This function will be 
	# called automatically with the chosen publish rate, to publish your 
	# messages. This function is the template of the publisher callback 
	# and you should put your own functionality.
	def publisher_call_toActuators(self):
		msg = Twist()
		# Please create the message of the publisher in this callback
		# The message definition could be found in the package: geometry_msgs
		
		# The message is type geometry_msgs/Twist
		# Remember to store data in its attributes before publishing
		
		
		# TODO: Add functionality here
		
		
		# Then publish the msg with the following code
		self.publisher_toActuators.publish(msg)
		
	#_____
	
	# Subscribers
	#____________________________________________
	# This is the callback of the subscriber fromSonar1. 
	# You can obtain the message from the variables set in this 
	# function, according to the instructions in the comments below. 
	# This function will be called automatically every time a message is
	# received. This function is the template of the subscriber callback 
	# and you should put your own functionality.
	def subscriber_call_fromSonar1(self, msg):
		# Please obtain the message from the subscriber in this callback
		# The message definition could be found in the package: interfaces
		
		# Store the variables of the msg
		h = msg.h
		range = msg.range
		# Now you can use the received variables
		
		
		# TODO: Add functionality here
		
		# You can see incoming info uncommenting the following line and filling the attributes "msg" object
		# ~ self.get_logger().info('I heard: '+str(msg.<put your attributres>))
	#_____
	# This is the callback of the subscriber fromSonar2. 
	# You can obtain the message from the variables set in this 
	# function, according to the instructions in the comments below. 
	# This function will be called automatically every time a message is
	# received. This function is the template of the subscriber callback 
	# and you should put your own functionality.
	def subscriber_call_fromSonar2(self, msg):
		# Please obtain the message from the subscriber in this callback
		# The message definition could be found in the package: interfaces
		
		# Store the variables of the msg
		h = msg.h
		range = msg.range
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
# This is the main executable for the node cpu.
# Run this executable from the root of the workspace using the command:
# $ ros2 run  cpu_exec
#
# This executable creates a node with all its features and spins it to
# wait for its callbacks.
def main(args=None):
	rclpy.init(args=args)
	
	cpu = cpu_class()
		
	rclpy.spin(cpu)
	# Destroy the node explicitly
	# (optional - otherwise it will be done automatically
	# when the garbage collector destroys the node object)
	cpu.destroy_node()
	rclpy.shutdown()

# Clients executables
#____________________________________________
	
if __name__ == '__main__':
	main()