
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
from interfaces.srv import Addtwo
# Imports for action interfaces
# Imports for msg inside custom interfaces
from std_msgs.msg import Header


# Class for the node node3 
class node3_class(Node):
	
	# Constructor function of the node
	def __init__(self):
				
		super().__init__('node3', namespace = 'name/space3')		
		# Params
		#____________________________________________
		
		
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
		# c1
		# Qos profile
		qos_profile_c1 = QoSProfile(history = QoSHistoryPolicy.KEEP_ALL, durability = QoSDurabilityPolicy.SYSTEM_DEFAULT, reliability = QoSReliabilityPolicy.RELIABLE, depth =0)
		# Additional qos settings
		qos_profile_c1.liveliness = QoSLivelinessPolicy.SYSTEM_DEFAULT
		qos_profile_c1.deadline.sec = 0
		qos_profile_c1.deadline.nsec = 0
		qos_profile_c1.lifespan.sec = 0
		qos_profile_c1.lifespan.nsec = 0
		qos_profile_c1.liveliness_lease_duration.sec = 0
		qos_profile_c1.liveliness_lease_duration.nsec = 0
		qos_profile_c1.avoid_ros_namespace_conventions = False
				
		self.client_c1 = self.create_client(Addtwo, 'service1', qos_profile = qos_profile_c1)
		#_____
		
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
		
		# You can see incoming info uncommenting the following line and filling the attributes "msg" object
		# ~ self.get_logger().info('I heard: '+str(msg.<put your attributres>))
	#_____
	
	# Servers
	#____________________________________________
		
	# Clients
	#____________________________________________
	# This is the call function of the client c1. 
	# You can call this function, passing all the arguments of the 
	# service request declaration (if the service is a Custom Service). 
	# This function will not be called automatically as you should call 
	# it to make a request. The function waits for the service to be 
	# available before going on and the server's response is stored in 
	# a future object once the server returns the response. This 
	# function is the template of the client call and you should call 
	# it for applying requests. Remember to change the arguments of the 
	# function based on the service you use.
	def client_call_c1(self, x, y):
		# Wait for service
		while not self.client_c1.wait_for_service(timeout_sec=1.0):
			self.get_logger().info('service not available, waiting again...')
		# Create request and fill it with data
		self.request_c1 = Addtwo.Request()
		self.request_c1.x = x
		self.request_c1.y = y
		self.future_c1 = self.client_c1.call_async(self.request_c1)
		# Result after server's response is stored in 
		# self.future_c1.result().b 
		# self.future_c1.result().h 
		# self.future_c1.result().z 
		
		
		# TODO: Add functionality here
		
		
	#_____
			
	# Action Servers
	#____________________________________________
	
	# Action Clients
	#____________________________________________
		
		
# Main executable
#____________________________________________
# This is the main executable for the node node3.
# Run this executable from the root of the workspace using the command:
# $ ros2 run  node3_exec
#
# This executable creates a node with all its features and spins it to
# wait for its callbacks.
def main(args=None):
	rclpy.init(args=args)
	
	node3 = node3_class()
		
	rclpy.spin(node3)
	# Destroy the node explicitly
	# (optional - otherwise it will be done automatically
	# when the garbage collector destroys the node object)
	node3.destroy_node()
	rclpy.shutdown()

# Clients executables
#____________________________________________
# This is the executable for the client c1.
# Run this executable from the root of the workspace using the command:
# $ ros2 run  node3_c1 arg1 arg2 ...
#
# This executable creates a node and call its client's call. It spins 
# the node until the response from the server is received.
def run_c1(args=None):
	rclpy.init(args=args)
	
	node3 = node3_class()
	#TODO create typecast from command line to client call type (change int to custom type)
	node3.client_call_c1(int(sys.argv[1]), int(sys.argv[2]))
	while rclpy.ok():
		rclpy.spin_once(node3)
		if node3.future_c1.done():
			try:
				response = node3.future_c1.result()
			except Exception as e:
				node3.get_logger().info('Service call failed %r' % (e,))
			else:
				node3.get_logger().info(
				'Result of add_three_ints: for %d + %d = %d' %
				(node3.request_c1.a, node3.request_c1.b, response.c))
			break
#_____
	
if __name__ == '__main__':
	main()