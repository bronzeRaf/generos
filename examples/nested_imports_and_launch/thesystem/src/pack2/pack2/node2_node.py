
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
# Imports for action interfaces
from interfaces.action import Dec
from interfaces.action import Increase
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
				
		self.publisher_pub1 = self.create_publisher(M1, 'topic/path1', qos_profile = qos_profile_pub1)
		self.timer_pub1 = self.create_timer(10.0, self.publisher_call_pub1)
		self.i = 0
		#_____
		
		# Subscribers
		#____________________________________________
		
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
		# as2
		self.action_server_as2 = ActionServer(self, Dec, 'as2', execute_callback=self.action_execute_call_as2, goal_callback=self.action_goal_call_as2, cancel_callback=self.action_cancel_call_as2)
		#_____
		
		# Action Clients
		#____________________________________________
		# ac1
		self.action_client_ac1 = ActionClient(self, Increase, 'ac1')
		#_____
		
		
		
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
		
		
		# Then publish the msg with the following code
		self.publisher_pub1.publish(msg)
		
	#_____
	
	# Subscribers
	#____________________________________________
	
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
	def client_call_c1(self, x , y ):
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
	# This is the execute callback of the action server as2. 
	# You can execute the goal request to the action server from the 
	# variables set in this function, according to the instructions in 
	# the comments below. This function will be called automatically 
	# every time an action goal request is received and needs to be 
	# executed. This function is the template of the action server 
	# callback and you should put your own functionality.
	def action_execute_call_as2(self, goal_handle):
		# Please add the server's functionality in this callback
		self.get_logger().info('Executing goal...')
		# If your action interface contain submessages remember to fill their attributes
		# Store the variables of the goal request
		x1 = goal_handle.request.x1
		x2 = goal_handle.request.x2
		# Create a feedback object
		feedback_msg = Dec.Feedback()
		# Every time you want to pass feedback update feedback attributes
		# feedback_msg.h = ...
		# feedback_msg.yt = ...
		# And call 
		# goal_handle.publish_feedback(feedback_msg)
		
		# Set the Result
		goal_handle.succeed()
		result = Dec.Result()
		# Fill the result with data
		# result.y = ...
		
		
		# TODO: Add functionality here
		
		# Finally forward the response
		return result
	
	# This is the goal callback of the action server as2.
	# This function receives a client goal requests to handle actions.
	# This function is the template of the action server 
	# callback and you should put your own functionality.
	def action_goal_call_as2(self,goal_request):
		# Please add the server's functionality in this callback
		self.get_logger().info('Received goal request')
		# Uncomment one of the following to reject or to accept an action request
		#return GoalResponse.REJECT
		return GoalResponse.ACCEPT
	
	# This is the cancel callback of the action server as2.
	# This function receives client cancel requests to handle actions.
	# This function is the template of the action server 
	# callback and you should put your own functionality.
	def action_cancel_call_as2(self, goal_handle):
		# Please add the server's functionality in this callback
		self.get_logger().info('Received cancel request')
		# Uncomment one of the following to reject or to accept an action request
		#return CancelResponse.REJECT
		return CancelResponse.ACCEPT
	#_____
	
	# Action Clients
	#____________________________________________
	# This is the call function of the action client ac1. 
	# You can call this function, passing all the arguments of the 
	# action goal request declaration. This function will not be called 
	# automatically as you should call it to make a request. The 
	# function waits for the action to be available before going on and
	# the action server's response is stored in a future object once 
	# the action server return the response. This function is the 
	# template of the action client call and you should call it for 
	# applying requests.
	def send_goal_call_ac1(self, start , stop ):
		# Wait for action service
		self.get_logger().info('Waiting for action server...')
		self.action_client_ac1.wait_for_server()
		# If your action interface contain submessages remember to fill their attributes 
		# Create goal and fill it with data
		goal_msg = Increase.Goal()
		goal_msg.start = start
		goal_msg.stop = stop
		# Send the goal request
		self.get_logger().info('Sending goal request...')
		self.future_ac1 = self.action_client_ac1.send_goal_async(goal_msg, feedback_callback=self.feedback_client_call_ac1)
		self.future_ac1.add_done_callback(self.goal_response_client_call_ac1)
		
	# This is the feedback callback of the action client ac1.
	# This function receives and handles the feedback that the 
	# action server publishes. This function is the template of the 
	# action client callback and you should put your own 
	# functionality.
	def feedback_client_call_ac1(self, feedback):
		self.get_logger().info('received feedback')
		# If your action interface contain submessages remember to obtain their attributes 
		# Do something with the variables in feedback
		# feedback.feedback.h
		# feedback.feedback.z
		
		
		# TODO: Add functionality here
		
		
		
	# This is the response callback of the action client ac1.
	# This function receives and handles the response that the 
	# action server gives. This function is the template of the 
	# action client callback and you should put your own 
	# functionality.
	def goal_response_client_call_ac1(self, future):
		# Set the goal result
		goal_handle = future.result()
		# Check if the goal was accepted
		if not goal_handle.accepted:
			self.get_logger().info('Goal rejected :(')
			return
		# Goal Accepted
		self.get_logger().info('Goal accepted :)')
		# Create a callback for receiving the result async
		self.client_future_ac1 = goal_handle.get_result_async()
		self.client_future_ac1.add_done_callback(self.get_result_call_ac1)
		
	# This is the result callback of the action client ac1.
	# This function receives and final result that the 
	# action server returns. This function is the template of the 
	# action client callback and you should put your own 
	# functionality.
	def get_result_call_ac1(self, future):
		result = future.result().result
		status = future.result().status
		if status == GoalStatus.STATUS_SUCCEEDED:
			# If your action interface contain submessages remember to obtain their attributes 
			# Do something with the variables in result
			# result.resus
			self.get_logger().info('Result obtained') 
		else:
			self.get_logger().info('Goal failed with status: {0}'.format(status))
		
		
		# TODO: Add functionality here
		
		
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
	# Destroy action server as2
	node2.action_server_as2.destroy()
	# Destroy action server ac1
	node2.action_client_ac1.destroy()
	node2.destroy_node()
	rclpy.shutdown()

# Clients executables
#____________________________________________
# This is the executable for the client c1.
# Run this executable from the root of the workspace using the command:
# $ ros2 run  node2_c1 arg1 arg2 ...
#
# This executable creates a node and call its client's call. It spins 
# the node until the response from the server is received.
def run_c1(args=None):
	rclpy.init(args=args)
	
	node2 = node2_class()
	#TODO create typecast from command line to client call type (change int to custom type)
	node2.client_call_c1(int(sys.argv[1]),  int(sys.argv[2]) )
	while rclpy.ok():
		rclpy.spin_once(node2)
		if node2.future_c1.done():
			try:
				response = node2.future_c1.result()
			except Exception as e:
				node2.get_logger().info('Service call failed %r' % (e,))
			else:
				node2.get_logger().info(
				'Result of add_three_ints: for %d + %d = %d' %
				(node2.request_c1.a, node2.request_c1.b, response.c))
			break
#_____
	
if __name__ == '__main__':
	main()