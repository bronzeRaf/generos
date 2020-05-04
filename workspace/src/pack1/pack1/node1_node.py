
from rclpy.qos import QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy, QoSLivelinessPolicy
from rclpy.qos import QoSProfile
from rclpy.qos import QoSPresetProfiles


# Imports for Action Servers
from rclpy.action import ActionServer, CancelResponse, GoalResponse
import rclpy
from rclpy.node import Node
import sys
# Imports for msg interfaces
from std_msgs.msg import Header
from interfaces.msg import ValueInt
# Imports for srv interfaces
from interfaces.srv import Addtwo
from std_srvs.srv import SetBool
# Imports for action interfaces
from interfaces.action import Increase
# Imports for msg inside custom interfaces
from std_msgs.msg import Int32


# Class for the node node1 
class node1_class(Node):
	
	# Constructor function of the node
	def __init__(self):
				
		super().__init__('node1')		
		# Params
		#____________________________________________
		# p1  -  int32
		self.param_p1 = self.declare_parameter('p1', 32)
		# You can use your parameter p1 with type int32
		# with 		self.get_parameter('p1')._value
		# or 		self.param_p1._value
		# You can also use your parameter from terminal or yaml file. 
		#_____
		
		
		# Publishers
		#____________________________________________
		# publy3
		# Qos profile
		qos_profile_publy3 = QoSPresetProfiles.SYSTEM_DEFAULT.value
				
		self.publisher_publy3 = self.create_publisher(Header, 'topic/path3', qos_profile = qos_profile_publy3)
		self.timer_publy3 = self.create_timer(12.0, self.publisher_call_publy3)
		self.i = 0
		#_____
		# publy2
		# Qos profile
		qos_profile_publy2 = QoSProfile(history=QoSHistoryPolicy.KEEP_ALL, durability = QoSDurabilityPolicy.TRANSIENT_LOCAL,reliability = QoSReliabilityPolicy.RELIABLE,depth =10)
		# Additional qos settings
		qos_profile_publy2.liveliness = QoSLivelinessPolicy.SYSTEM_DEFAULT
		qos_profile_publy2.deadline.sec = 0
		qos_profile_publy2.deadline.nsec = 0
		qos_profile_publy2.lifespan.sec = 0
		qos_profile_publy2.lifespan.nsec = 0
		qos_profile_publy2.liveliness_lease_duration.sec = 0
		qos_profile_publy2.liveliness_lease_duration.nsec = 0
		qos_profile_publy2.avoid_ros_namespace_conventions = False
				
		self.publisher_publy2 = self.create_publisher(ValueInt, 'topic/path2', qos_profile = qos_profile_publy2)
		self.timer_publy2 = self.create_timer(8.0, self.publisher_call_publy2)
		self.i = 0
		#_____
		
		# Subscribers
		#____________________________________________
		
		# Servers
		#____________________________________________
		# Server1
		# Qos profile
		qos_profile_Server1 = QoSPresetProfiles.SERVICES_DEFAULT.value
				
		self.server_Server1 = self.create_service(Addtwo, 'add_two', self.server_call_Server1, qos_profile = qos_profile_Server1)
		#_____
		# Server3
		# Qos profile
		qos_profile_Server3 = QoSPresetProfiles.SERVICES_DEFAULT.value
				
		self.server_Server3 = self.create_service(SetBool, 'set_bool', self.server_call_Server3, qos_profile = qos_profile_Server3)
		#_____
		
		# Clients
		#____________________________________________
		
		# Action Servers
		#____________________________________________
		# action1
		self.action_server_action1 = ActionServer(self, Increase, 'action1', execute_callback=self.action_execute_call_action1, goal_callback=self.action_goal_call_action1, cancel_callback=self.action_cancel_call_action1)
		#_____
		
		# Action Clients
		#____________________________________________
		
		
		
	# ************Callbacks************
	# Publishers
	#____________________________________________
	# This is the callback of the publisher publy3. 
	# You can store the message in the msg object attributes, according 
	# to the instructions in the comments below. This function will be 
	# called automatically with the chosen publish rate, to publish your 
	# messages. This function is the template of the publisher callback 
	# and you should put your own functionality.
	def publisher_call_publy3(self):
		msg = Header()
		# Please create the message of the publisher in this callback
		# Message after calculactions should be stored in
		
		
		self.i += 1
	#_____
	# This is the callback of the publisher publy2. 
	# You can store the message in the msg object attributes, according 
	# to the instructions in the comments below. This function will be 
	# called automatically with the chosen publish rate, to publish your 
	# messages. This function is the template of the publisher callback 
	# and you should put your own functionality.
	def publisher_call_publy2(self):
		msg = ValueInt()
		# Please create the message of the publisher in this callback
		# Message after calculactions should be stored in
		# msg.header 
		# msg.x 
		
		
		msg.x = self.i
		
		
		self.publisher_publy2.publish(msg)
		self.get_logger().info('Publishing: "%s"' % msg.x)
		self.i += 1
	#_____
	
	# Subscribers
	#____________________________________________
	
	#Servers
	#____________________________________________
	# This is the callback of the server Server1. 
	# You can obtain the request to the server from the variables set in 
	# this function, according to the instructions in the comments 
	# below. This function will be called automatically every time a 
	# request is received. This function is the template of the server 
	# callback and you should put your own functionality.
	def server_call_Server1(self, request, response):
		# Please add the server's functionality in this callback
		# Store the variables of the request
		a = request.a
		b = request.b
		# Service result after calculactions should be stored in
		# response.c 
		response.c = request.a + request.b
		self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))
		return response
	#_____
	# This is the callback of the server Server3. 
	# You can obtain the request to the server from the variables set in 
	# this function, according to the instructions in the comments 
	# below. This function will be called automatically every time a 
	# request is received. This function is the template of the server 
	# callback and you should put your own functionality.
	def server_call_Server3(self, request, response):
		# Please add the server's functionality in this callback
		# Store the variables of the request
		# Service result after calculactions should be stored in
		response.c = request.a + request.b
		self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))
		return response
	#_____
		
	# Clients
	#____________________________________________
			
	# Action Servers
	#____________________________________________
	# This is the execute callback of the action server action1. 
	# You can execute the goal request to the action server from the 
	# variables set in this function, according to the instructions in 
	# the comments below. This function will be called automatically 
	# every time an action goal request is received and needs to be 
	# executed. This function is the template of the action server 
	# callback and you should put your own functionality.
	def action_execute_call_action1(self, goal_handle):
		# Please add the server's functionality in this callback
		self.get_logger().info('Executing goal...')
		# Store the variables of the goal request
		start = goal_handle.request.start
		goal = goal_handle.request.goal
		# Create a feedback object
		feedback_msg = Increase.Feedback()
		# Every time you want to pass feedback update feedback attributes
		# feedback_msg.update = ...
		# And call 
		# goal_handle.publish_feedback(feedback_msg)
		
		# Set the Result
		goal_handle.succeed()
		result = Increase.Result()
		# Fill the result with data
		# result.a = ...
		return result
	
	# This is the goal callback of the action server action1.
	# This function receives a client goal requests to handle actions.
	# This function is the template of the action server 
	# callback and you should put your own functionality.
	def action_goal_call_action1(self,goal_request):
		# Please add the server's functionality in this callback
		self.get_logger().info('Received goal request')
		# Uncomment one of the following to reject or to accept an action request
		#return GoalResponse.REJECT
		return GoalResponse.ACCEPT
	
	# This is the cancel callback of the action server action1.
	# This function receives client cancel requests to handle actions.
	# This function is the template of the action server 
	# callback and you should put your own functionality.
	def action_cancel_call_action1(self, goal_handle):
		# Please add the server's functionality in this callback
		self.get_logger().info('Received cancel request')
		# Uncomment one of the following to reject or to accept an action request
		#return CancelResponse.REJECT
		return CancelResponse.ACCEPT
	#_____
	
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
	# Destroy action server action1
	node1.action_server_action1.destroy()
	node1.destroy_node()
	rclpy.shutdown()

# Clients executables
#____________________________________________
	
if __name__ == '__main__':
	main()