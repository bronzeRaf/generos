
from rclpy.qos import QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy, QoSLivelinessPolicy
from rclpy.qos import QoSProfile
from rclpy.qos import QoSPresetProfiles
from rcl_interfaces.msg import ParameterDescriptor

# Imports for Action Servers
from rclpy.action import ActionServer, CancelResponse, GoalResponse
# Imports for Action Clients
from rclpy.action import ActionClient
from action_msgs.msg import GoalStatus
import rclpy
from rclpy.node import Node
import sys
# Imports for msg interfaces
from interfaces.msg import M1
# Imports for srv interfaces
from interfaces.srv import Addtwo
from std_srvs.srv import SetBool
# Imports for action interfaces
from interfaces.action import Increase
from interfaces.action import Dec
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
				
		self.subscriber_sub1 = self.create_subscription(M1, 'topic/path1', self.subscriber_call_sub1, qos_profile = qos_profile_sub1)
		self.subscriber_sub1
		#_____
		
		# Servers
		#____________________________________________
		# s1
		# Qos profile
		qos_profile_s1 = QoSProfile(history = QoSHistoryPolicy.KEEP_ALL, durability = QoSDurabilityPolicy.SYSTEM_DEFAULT, reliability = QoSReliabilityPolicy.RELIABLE, depth =0)
		# Additional qos settings
		qos_profile_s1.liveliness = QoSLivelinessPolicy.SYSTEM_DEFAULT
		qos_profile_s1.deadline.sec = 0
		qos_profile_s1.deadline.nsec = 0
		qos_profile_s1.lifespan.sec = 0
		qos_profile_s1.lifespan.nsec = 0
		qos_profile_s1.liveliness_lease_duration.sec = 0
		qos_profile_s1.liveliness_lease_duration.nsec = 0
		qos_profile_s1.avoid_ros_namespace_conventions = False
				
		self.server_s1 = self.create_service(Addtwo, 'service1', self.server_call_s1, qos_profile = qos_profile_s1)
		#_____
		# s2
		# Qos profile
		qos_profile_s2 = QoSProfile(history = QoSHistoryPolicy.KEEP_ALL, durability = QoSDurabilityPolicy.SYSTEM_DEFAULT, reliability = QoSReliabilityPolicy.RELIABLE, depth =0)
		# Additional qos settings
		qos_profile_s2.liveliness = QoSLivelinessPolicy.SYSTEM_DEFAULT
		qos_profile_s2.deadline.sec = 0
		qos_profile_s2.deadline.nsec = 0
		qos_profile_s2.lifespan.sec = 0
		qos_profile_s2.lifespan.nsec = 0
		qos_profile_s2.liveliness_lease_duration.sec = 0
		qos_profile_s2.liveliness_lease_duration.nsec = 0
		qos_profile_s2.avoid_ros_namespace_conventions = False
				
		self.server_s2 = self.create_service(SetBool, 'service2', self.server_call_s2, qos_profile = qos_profile_s2)
		#_____
		
		# Clients
		#____________________________________________
		
		# Action Servers
		#____________________________________________
		# as1
		self.action_server_as1 = ActionServer(self, Increase, 'as1', execute_callback=self.action_execute_call_as1, goal_callback=self.action_goal_call_as1, cancel_callback=self.action_cancel_call_as1)
		#_____
		
		# Action Clients
		#____________________________________________
		# as2
		self.action_client_as2 = ActionClient(self, Dec, 'as2')
		#_____
		
		
		
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
	# This is the callback of the server s1. 
	# You can obtain the request to the server from the variables set in 
	# this function, according to the instructions in the comments 
	# below. This function will be called automatically every time a 
	# request is received. This function is the template of the server 
	# callback and you should put your own functionality.
	def server_call_s1(self, request, response):
		# Please add the server's functionality in this callback
		# Store the variables of the request
		x = request.x
		y = request.y
		# Service result after calculactions should be stored in:
		# response.b 
		# response.h 
		# response.z 
		
		
		# TODO: Add functionality here
		
		# You can store the result uncommenting the following line and filling the attributes of the "response" object 
		# ~ response.<put your attributres> = <put your values> 
		
		# You can see incoming info uncommenting the following line and filling the attributes "request" object
		# ~ self.get_logger().info('Incoming request\nvalue 1: '+ str(request.<put your attributres>)+' value 2: '+str(request.<put your attributres>))
		
		# Finally forward the response
		return response
	#_____
	# This is the callback of the server s2. 
	# You can obtain the request to the server from the variables set in 
	# this function, according to the instructions in the comments 
	# below. This function will be called automatically every time a 
	# request is received. This function is the template of the server 
	# callback and you should put your own functionality.
	def server_call_s2(self, request, response):
		# Please add the server's functionality in this callback
		# The service is type std_srvs/SetBool
		# Remember to store data in its attributes
		
		
		# TODO: Add functionality here
		
		# You can store the result uncommenting the following line and filling the attributes of the "response" object 
		# ~ response.<put your attributres> = <put your values> 
		
		# You can see incoming info uncommenting the following line and filling the attributes "request" object
		# ~ self.get_logger().info('Incoming request\nvalue 1: '+ str(request.<put your attributres>)+' value 2: '+str(request.<put your attributres>))
		
		# Finally forward the response
		return response
	#_____
		
	# Clients
	#____________________________________________
			
	# Action Servers
	#____________________________________________
	# This is the execute callback of the action server as1. 
	# You can execute the goal request to the action server from the 
	# variables set in this function, according to the instructions in 
	# the comments below. This function will be called automatically 
	# every time an action goal request is received and needs to be 
	# executed. This function is the template of the action server 
	# callback and you should put your own functionality.
	def action_execute_call_as1(self, goal_handle):
		# Please add the server's functionality in this callback
		self.get_logger().info('Executing goal...')
		# If your action interface contain submessages remember to fill their attributes
		# Store the variables of the goal request
		start = goal_handle.request.start
		stop = goal_handle.request.stop
		# Create a feedback object
		feedback_msg = Increase.Feedback()
		# Every time you want to pass feedback update feedback attributes
		# feedback_msg.h = ...
		# feedback_msg.z = ...
		# And call 
		# goal_handle.publish_feedback(feedback_msg)
		
		# Set the Result
		goal_handle.succeed()
		result = Increase.Result()
		# Fill the result with data
		# result.resus = ...
		
		
		# TODO: Add functionality here
		
		# Finally forward the response
		return result
	
	# This is the goal callback of the action server as1.
	# This function receives a client goal requests to handle actions.
	# This function is the template of the action server 
	# callback and you should put your own functionality.
	def action_goal_call_as1(self,goal_request):
		# Please add the server's functionality in this callback
		self.get_logger().info('Received goal request')
		# Uncomment one of the following to reject or to accept an action request
		#return GoalResponse.REJECT
		return GoalResponse.ACCEPT
	
	# This is the cancel callback of the action server as1.
	# This function receives client cancel requests to handle actions.
	# This function is the template of the action server 
	# callback and you should put your own functionality.
	def action_cancel_call_as1(self, goal_handle):
		# Please add the server's functionality in this callback
		self.get_logger().info('Received cancel request')
		# Uncomment one of the following to reject or to accept an action request
		#return CancelResponse.REJECT
		return CancelResponse.ACCEPT
	#_____
	
	# Action Clients
	#____________________________________________
	# This is the call function of the action client as2. 
	# You can call this function, passing all the arguments of the 
	# action goal request declaration. This function will not be called 
	# automatically as you should call it to make a request. The 
	# function waits for the action to be available before going on and
	# the action server's response is stored in a future object once 
	# the action server return the response. This function is the 
	# template of the action client call and you should call it for 
	# applying requests.
	def send_goal_call_as2(self, x1 , x2 ):
		# Wait for action service
		self.get_logger().info('Waiting for action server...')
		self.action_client_as2.wait_for_server()
		# If your action interface contain submessages remember to fill their attributes 
		# Create goal and fill it with data
		goal_msg = Dec.Goal()
		goal_msg.x1 = x1
		goal_msg.x2 = x2
		# Send the goal request
		self.get_logger().info('Sending goal request...')
		self.future_as2 = self.action_client_as2.send_goal_async(goal_msg, feedback_callback=self.feedback_client_call_as2)
		self.future_as2.add_done_callback(self.goal_response_client_call_as2)
		
	# This is the feedback callback of the action client as2.
	# This function receives and handles the feedback that the 
	# action server publishes. This function is the template of the 
	# action client callback and you should put your own 
	# functionality.
	def feedback_client_call_as2(self, feedback):
		self.get_logger().info('received feedback')
		# If your action interface contain submessages remember to obtain their attributes 
		# Do something with the variables in feedback
		# feedback.feedback.h
		# feedback.feedback.yt
		
		
		# TODO: Add functionality here
		
		
		
	# This is the response callback of the action client as2.
	# This function receives and handles the response that the 
	# action server gives. This function is the template of the 
	# action client callback and you should put your own 
	# functionality.
	def goal_response_client_call_as2(self, future):
		# Set the goal result
		goal_handle = future.result()
		# Check if the goal was accepted
		if not goal_handle.accepted:
			self.get_logger().info('Goal rejected :(')
			return
		# Goal Accepted
		self.get_logger().info('Goal accepted :)')
		# Create a callback for receiving the result async
		self.client_future_as2 = goal_handle.get_result_async()
		self.client_future_as2.add_done_callback(self.get_result_call_as2)
		
	# This is the result callback of the action client as2.
	# This function receives and final result that the 
	# action server returns. This function is the template of the 
	# action client callback and you should put your own 
	# functionality.
	def get_result_call_as2(self, future):
		result = future.result().result
		status = future.result().status
		if status == GoalStatus.STATUS_SUCCEEDED:
			# If your action interface contain submessages remember to obtain their attributes 
			# Do something with the variables in result
			# result.y
			self.get_logger().info('Result obtained') 
		else:
			self.get_logger().info('Goal failed with status: {0}'.format(status))
		
		
		# TODO: Add functionality here
		
		
	#_____
		
		
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
	# Destroy action server as1
	node1.action_server_as1.destroy()
	# Destroy action server as2
	node1.action_client_as2.destroy()
	node1.destroy_node()
	rclpy.shutdown()

# Clients executables
#____________________________________________
	
if __name__ == '__main__':
	main()