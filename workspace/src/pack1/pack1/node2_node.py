
from rclpy.qos import QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy, QoSLivelinessPolicy
from rclpy.qos import QoSProfile
from rclpy.qos import QoSPresetProfiles


# Imports for Action Clients
from rclpy.action import ActionClient
from action_msgs.msg import GoalStatus
import rclpy
from rclpy.node import Node
import sys
# Imports for msg interfaces
from interfaces.msg import ValueInt
# Imports for srv interfaces
from interfaces.srv import Addtwo
from std_srvs.srv import SetBool
# Imports for action interfaces
from interfaces.action import Increase
# Imports for msg inside custom interfaces
from std_msgs.msg import Header


# Class for the node node2 
class node2_class(Node):
	
	# Constructor function of the node
	def __init__(self):
				
		super().__init__('node2')		
		# Params
		#____________________________________________
		
		
		# Publishers
		#____________________________________________
		
		# Subscribers
		#____________________________________________
		# suby2
		# Qos profile
		qos_profile_suby2 = QoSProfile(history = QoSHistoryPolicy.KEEP_ALL, durability = QoSDurabilityPolicy.TRANSIENT_LOCAL, reliability = QoSReliabilityPolicy.RELIABLE, depth =10)
		# Additional qos settings
		qos_profile_suby2.liveliness = QoSLivelinessPolicy.SYSTEM_DEFAULT
		qos_profile_suby2.deadline.sec = 0
		qos_profile_suby2.deadline.nsec = 0
		qos_profile_suby2.lifespan.sec = 0
		qos_profile_suby2.lifespan.nsec = 0
		qos_profile_suby2.liveliness_lease_duration.sec = 0
		qos_profile_suby2.liveliness_lease_duration.nsec = 0
		qos_profile_suby2.avoid_ros_namespace_conventions = False
				
		self.subscriber_suby2 = self.create_subscription(ValueInt, 'topic/path2', self.subscriber_call_suby2, qos_profile = qos_profile_suby2)
		self.subscriber_suby2
		#_____
		
		# Servers
		#____________________________________________
		
		# Clients
		#____________________________________________
		# Client1
		# Qos profile
		qos_profile_Client1 = QoSProfile(history = QoSHistoryPolicy.KEEP_LAST, durability = QoSDurabilityPolicy.VOLATILE, reliability = QoSReliabilityPolicy.RELIABLE, depth =5)
		# Additional qos settings
		qos_profile_Client1.liveliness = QoSLivelinessPolicy.SYSTEM_DEFAULT
		qos_profile_Client1.deadline.sec = 0
		qos_profile_Client1.deadline.nsec = 0
		qos_profile_Client1.lifespan.sec = 0
		qos_profile_Client1.lifespan.nsec = 0
		qos_profile_Client1.liveliness_lease_duration.sec = 0
		qos_profile_Client1.liveliness_lease_duration.nsec = 0
		qos_profile_Client1.avoid_ros_namespace_conventions = False
				
		self.client_Client1 = self.create_client(Addtwo, 'add_two', qos_profile = qos_profile_Client1)
		#_____
		# Client3
		# Qos profile
		qos_profile_Client3 = QoSProfile(history = QoSHistoryPolicy.KEEP_LAST, durability = QoSDurabilityPolicy.VOLATILE, reliability = QoSReliabilityPolicy.RELIABLE, depth =5)
		# Additional qos settings
		qos_profile_Client3.liveliness = QoSLivelinessPolicy.SYSTEM_DEFAULT
		qos_profile_Client3.deadline.sec = 0
		qos_profile_Client3.deadline.nsec = 0
		qos_profile_Client3.lifespan.sec = 0
		qos_profile_Client3.lifespan.nsec = 0
		qos_profile_Client3.liveliness_lease_duration.sec = 0
		qos_profile_Client3.liveliness_lease_duration.nsec = 0
		qos_profile_Client3.avoid_ros_namespace_conventions = False
				
		self.client_Client3 = self.create_client(SetBool, 'set_bool', qos_profile = qos_profile_Client3)
		#_____
		
		# Action Servers
		#____________________________________________
		
		# Action Clients
		#____________________________________________
		# action1
		self.action_client_action1 = ActionClient(self, Increase, 'action1')
		#_____
		
		
		
	# ************Callbacks************
	# Publishers
	#____________________________________________
	
	# Subscribers
	#____________________________________________
	# This is the callback of the subscriber suby2. 
	# You can obtain the message from the variables set in this 
	# function, according to the instructions in the comments below. 
	# This function will be called automatically every time a message is
	# received. This function is the template of the subscriber callback 
	# and you should put your own functionality.
	def subscriber_call_suby2(self, msg):
		# Please obtain the message from the subscriber in this callback
		# The message definition could be found in the package: interfaces
		
		# Store the variables of the msg
		header = msg.header
		x = msg.x
		# Now you can use the received variables

		self.get_logger().info('I heard: '+str(msg.x))
	#_____
	
	# Servers
	#____________________________________________
		
	# Clients
	#____________________________________________
	# This is the call function of the client Client1. 
	# You can call this function, passing all the arguments of the 
	# service request declaration (if the service is a Custom Service). 
	# This function will not be called automatically as you should call 
	# it to make a request. The function waits for the service to be 
	# available before going on and the server's response is stored in 
	# a future object once the server returns the response. This 
	# function is the template of the client call and you should call 
	# it for applying requests. Remember to change the arguments of the 
	# function based on the service you use.
	def client_call_Client1(self, a, b):
		# Wait for service
		while not self.client_Client1.wait_for_service(timeout_sec=1.0):
			self.get_logger().info('service not available, waiting again...')
		# Create request and fill it with data
		self.request_Client1 = Addtwo.Request()
		self.request_Client1.a = a
		self.request_Client1.b = b
		self.future_Client1 = self.client_Client1.call_async(self.request_Client1)
		# Result after server's response is stored in 
		# self.future_Client1.result().c 
	#_____
	# This is the call function of the client Client3. 
	# You can call this function, passing all the arguments of the 
	# service request declaration (if the service is a Custom Service). 
	# This function will not be called automatically as you should call 
	# it to make a request. The function waits for the service to be 
	# available before going on and the server's response is stored in 
	# a future object once the server returns the response. This 
	# function is the template of the client call and you should call 
	# it for applying requests. Remember to change the arguments of the 
	# function based on the service you use.
	def client_call_Client3(self):
		# Wait for service
		while not self.client_Client3.wait_for_service(timeout_sec=1.0):
			self.get_logger().info('service not available, waiting again...')
		# Create request and fill it with data
		self.request_Client3 = SetBool.Request()
		# The service is type std_srvs/SetBool
		# Remember to store data in the attributes of self.request_Client3
		self.future_Client3 = self.client_Client3.call_async(self.request_Client3)
		# Result after server's response is stored in 
	#_____
			
	# Action Servers
	#____________________________________________
	
	# Action Clients
	#____________________________________________
	# This is the call function of the action client action1. 
	# You can call this function, passing all the arguments of the 
	# action goal request declaration. This function will not be called 
	# automatically as you should call it to make a request. The 
	# function waits for the action to be available before going on and
	# the action server's response is stored in a future object once 
	# the action server return the response. This function is the 
	# template of the action client call and you should call it for 
	# applying requests.
	def send_goal_call_action1(self, start, goal):
		# Wait for action service
		self.get_logger().info('Waiting for action server...')
		self.action_client_action1.wait_for_server()
		# Create goal and fill it with data
		goal_msg = Increase.Goal()
		goal_msg.start = start
		goal_msg.goal = goal
		# Send the goal request
		self.get_logger().info('Sending goal request...')
		self.future_action1 = self.action_client_action1.send_goal_async(goal_msg, feedback_callback=self.feedback_client_call_action1)
		self.future_action1.add_done_callback(self.goal_response_client_call_action1)
		
	# This is the feedback callback of the action client action1.
	# This function receives and handles the feedback that the 
	# action server publishes. This function is the template of the 
	# action client callback and you should put your own 
	# functionality.
	def feedback_client_call_action1(self, feedback):
		self.get_logger().info('received feedback')
		# Do something with the variables in feedback
		# feedback.feedback.update
		
	# This is the response callback of the action client action1.
	# This function receives and handles the response that the 
	# action server gives. This function is the template of the 
	# action client callback and you should put your own 
	# functionality.
	def goal_response_client_call_action1(self, future):
		# Set the goal result
		goal_handle = future.result()
		# Check if the goal was accepted
		if not goal_handle.accepted:
			self.get_logger().info('Goal rejected :(')
			return
		# Goal Accepted
		self.get_logger().info('Goal accepted :)')
		# Create a callback for receiving the result async
		self.client_future_action1 = goal_handle.get_result_async()
		self.client_future_action1.add_done_callback(self.get_result_call_action1)
		
	# This is the result callback of the action client action1.
	# This function receives and final result that the 
	# action server returns. This function is the template of the 
	# action client callback and you should put your own 
	# functionality.
	def get_result_call_action1(self, future):
		result = future.result().result
		status = future.result().status
		if status == GoalStatus.STATUS_SUCCEEDED:
			# Do something with the variables in result
			# result.a
			self.get_logger().info('Result obtained') 
		else:
			self.get_logger().info('Goal failed with status: {0}'.format(status))

	#_____
		
		
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
	# Destroy action server action1
	node2.action_client_action1.destroy()
	node2.destroy_node()
	rclpy.shutdown()

# Clients executables
#____________________________________________
# This is the executable for the client Client1.
# Run this executable from the root of the workspace using the command:
# $ ros2 run  node2_Client1 arg1 arg2 ...
#
# This executable creates a node and call its client's call. It spins 
# the node until the response from the server is received.
def run_Client1(args=None):
	rclpy.init(args=args)
	
	node2 = node2_class()
	#TODO create typecast from command line to client call type (change int to custom type)
	node2.client_call_Client1(int(sys.argv[1]), int(sys.argv[2]))
	while rclpy.ok():
		rclpy.spin_once(node2)
		if node2.future_Client1.done():
			try:
				response = node2.future_Client1.result()
			except Exception as e:
				node2.get_logger().info('Service call failed %r' % (e,))
			else:
				node2.get_logger().info(
				'Result of add_three_ints: for %d + %d = %d' %
				(node2.request_Client1.a, node2.request_Client1.b, response.c))
			break
#_____
# This is the executable for the client Client3.
# Run this executable from the root of the workspace using the command:
# $ ros2 run  node2_Client3 arg1 arg2 ...
#
# This executable creates a node and call its client's call. It spins 
# the node until the response from the server is received.
def run_Client3(args=None):
	rclpy.init(args=args)
	
	node2 = node2_class()
	#TODO create typecast from command line to client call type (change int to custom type)
	node2.client_call_Client3(int(sys.argv[1]))
	while rclpy.ok():
		rclpy.spin_once(node2)
		if node2.future_Client3.done():
			try:
				response = node2.future_Client3.result()
			except Exception as e:
				node2.get_logger().info('Service call failed %r' % (e,))
			else:
				node2.get_logger().info(
				'Result of add_three_ints: for %d + %d = %d' %
				(node2.request_Client3.a, node2.request_Client3.b, response.c))
			break
#_____
	
if __name__ == '__main__':
	main()