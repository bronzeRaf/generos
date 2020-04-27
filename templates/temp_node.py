{# 
#This is a jinja2 template of a ROS2 Node
#
# Written in 13/4/2020
# Written by Rafael Brouzos
#}

from rclpy.qos import QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy
from rclpy.qos import QoSProfile


{% if action_servers is defined and action_servers|length %}
# Imports for Action Servers
from rclpy.action import ActionServer, CancelResponse, GoalResponse
{% endif %}
{% if action_clients is defined and action_clients|length %}
# Imports for Action Clients
from rclpy.action import ActionClient
from action_msgs.msg import GoalStatus
{% endif %}
import rclpy
from rclpy.node import Node
import sys
# Imports for msg interfaces
{%for p in publishers %}
{%if p.unique == 1 %}
from {{p.package}}.msg import {{p.type}}
{%endif%}
{%endfor%}
{%for s in subscribers %}
{%if s.unique == 1 %}
from {{s.package}}.msg import {{s.type}}
{%endif%}
{%endfor%}
# Imports for srv interfaces
{%for s in servers %}
{%if s.unique == 1 %}
from {{s.package}}.srv import {{s.type}}
{%endif%}
{%endfor%}
{%for c in clients %}
{%if c.unique == 1 %}
from {{c.package}}.srv import {{c.type}}
{%endif%}
{%endfor%}
# Imports for action interfaces
{%for s in action_servers %}
{%if s.unique == 1 %}
from {{s.package}}.action import {{s.type}}
{%endif%}
{%endfor%}
{%for c in action_clients %}
{%if c.unique == 1 %}
from {{c.package}}.action import {{c.type}}
{%endif%}
{%endfor%}
# Imports for msg inside custom interfaces
{%for e in extra_imports %}
from {{e.package}}.msg import {{e.type}}
{%endfor%}


# Class for the node {{node.name}} 
class {{node.name}}_class(Node):
	
	# Constructor function of the node
	def __init__(self):
		super().__init__('{{node.name}}'{%if not node.namespace == None%}, namespace = '{{node.namespace}}'{%endif%})		
		# Params
		#____________________________________________
		{%for p in params %}
		# {{p.name}}  -  {{p.type}}
		self.param_{{p.name}} = self.declare_parameter('{{p.name}}', {{p.value}})
		# You can use your parameter {{p.name}} with type {{p.type}}
		# with 		self.get_parameter('{{p.name}}')._value
		# or 		self.param_{{p.name}}._value
		# You can also use your parameter from terminal or yaml file. 
		#_____
		{%endfor%}
		
		
		# Publishers
		#____________________________________________
		{%for p in publishers %}
		# {{p.name}}
		# Qos profile
		qos_profile_{{p.name}} = QoSProfile(history=QoSHistoryPolicy.{{p.profile.history}}, durability = QoSDurabilityPolicy.{{p.profile.durability}},reliability = QoSReliabilityPolicy.{{p.profile.reliability}},depth ={{p.profile.depth}})
		# ~ qos_profile_{{p.name}}.history = QoSHistoryPolicy.{{p.profile.history}}
		# ~ qos_profile_{{p.name}}.durability = QoSDurabilityPolicy.{{p.profile.durability}}
		# ~ qos_profile_{{p.name}}.reliability = QoSReliabilityPolicy.{{p.profile.reliability}}
		# ~ qos_profile_{{p.name}}.depth ={{p.profile.depth}}
		
		# ~ qos_profile_{{p.name}}.liveliness ={{p.profile.liveliness}}
		# ~ qos_profile_{{p.name}}.deadline.sec ={{p.profile.deadlineSec}}
		# ~ qos_profile_{{p.name}}.deadline.nsec ={{p.profile.deadlineNSec}}
		# ~ qos_profile_{{p.name}}.lifespan.sec ={{p.profile.lifespanSec}}
		# ~ qos_profile_{{p.name}}.lifespan.nsec ={{p.profile.lifespanNSec}}
		# ~ qos_profile_{{p.name}}.liveliness_lease_duration.sec ={{p.profile.liveliness_lease_durationSec}}
		# ~ qos_profile_{{p.name}}.liveliness_lease_duration.nsec ={{p.profile.liveliness_lease_durationNSec}}
		# ~ qos_profile_{{p.name}}.avoid_ros_namespace_conventions ={{p.profile.avoid_ros_namespace_conventions}}
		
		self.publisher_{{p.name}} = self.create_publisher({{p.type}}, '{{p.topicPath}}', qos_profile = qos_profile_{{p.name}})
		self.timer_{{p.name}} = self.create_timer({{p.publishRate}}, self.publisher_call_{{p.name}})
		self.i = 0
		#_____
		{%endfor%}
		
		# Subscribers
		#____________________________________________
		{%for s in subscribers %}
		# {{s.name}}
		# Qos profile
		qos_profile_{{s.name}} = QoSProfile(history = QoSHistoryPolicy.{{s.profile.history}}, durability = QoSDurabilityPolicy.{{s.profile.durability}}, reliability = QoSReliabilityPolicy.{{s.profile.reliability}}, depth ={{s.profile.depth}})
		# ~ qos_profile_{{s.name}}.history = QoSHistoryPolicy.{{s.profile.history}}
		# ~ qos_profile_{{s.name}}.durability = QoSDurabilityPolicy.{{s.profile.durability}}
		# ~ qos_profile_{{s.name}}.reliability = QoSReliabilityPolicy.{{s.profile.reliability}}
		# ~ qos_profile_{{s.name}}.depth ={{s.profile.depth}}
		
		# ~ qos_profile_{{s.name}}.liveliness ={{s.profile.liveliness}}
		# ~ qos_profile_{{s.name}}.deadline.sec ={{s.profile.deadlineSec}}
		# ~ qos_profile_{{s.name}}.deadline.nsec ={{s.profile.deadlineNSec}}
		# ~ qos_profile_{{s.name}}.lifespan.sec ={{s.profile.lifespanSec}}
		# ~ qos_profile_{{s.name}}.lifespan.nsec ={{s.profile.lifespanNSec}}
		# ~ qos_profile_{{s.name}}.liveliness_lease_duration.sec ={{s.profile.liveliness_lease_durationSec}}
		# ~ qos_profile_{{s.name}}.liveliness_lease_duration.nsec ={{s.profile.liveliness_lease_durationNSec}}
		# ~ qos_profile_{{s.name}}.avoid_ros_namespace_conventions ={{s.profile.avoid_ros_namespace_conventions}}
		
		self.subscriber_{{s.name}} = self.create_subscription({{s.type}}, '{{s.topicPath}}', self.subscriber_call_{{s.name}}, qos_profile = qos_profile_{{s.name}})
		self.subscriber_{{s.name}}
		#_____
		{%endfor%}
		
		# Servers
		#____________________________________________
		{%for s in servers %}
		# {{s.name}}
		# Qos profile
		qos_profile_{{s.name}} = QoSProfile(history = QoSHistoryPolicy.{{s.profile.history}}, durability = QoSDurabilityPolicy.{{s.profile.durability}}, reliability = QoSReliabilityPolicy.{{s.profile.reliability}}, depth ={{s.profile.depth}})
		# ~ qos_profile_{{s.name}}.history = QoSHistoryPolicy.{{s.profile.history}}
		# ~ qos_profile_{{s.name}}.durability = QoSDurabilityPolicy.{{s.profile.durability}}
		# ~ qos_profile_{{s.name}}.reliability = QoSReliabilityPolicy.{{s.profile.reliability}}
		# ~ qos_profile_{{s.name}}.depth ={{s.profile.depth}}
		
		# ~ qos_profile_{{s.name}}.liveliness ={{s.profile.liveliness}}
		# ~ qos_profile_{{s.name}}.deadline.sec ={{s.profile.deadlineSec}}
		# ~ qos_profile_{{s.name}}.deadline.nsec ={{s.profile.deadlineNSec}}
		# ~ qos_profile_{{s.name}}.lifespan.sec ={{s.profile.lifespanSec}}
		# ~ qos_profile_{{s.name}}.lifespan.nsec ={{s.profile.lifespanNSec}}
		# ~ qos_profile_{{s.name}}.liveliness_lease_duration.sec ={{s.profile.liveliness_lease_durationSec}}
		# ~ qos_profile_{{s.name}}.liveliness_lease_duration.nsec ={{s.profile.liveliness_lease_durationNSec}}
		# ~ qos_profile_{{s.name}}.avoid_ros_namespace_conventions ={{s.profile.avoid_ros_namespace_conventions}}
		
		self.server_{{s.name}} = self.create_service({{s.type}}, '{{s.serviceName}}', self.server_call_{{s.name}}, qos_profile = qos_profile_{{s.name}})
		#_____
		{%endfor%}
		
		# Clients
		#____________________________________________
		{%for c in clients %}
		# {{c.name}}
		# Qos profile
		qos_profile_{{c.name}} = QoSProfile(history = QoSHistoryPolicy.{{c.profile.history}}, durability = QoSDurabilityPolicy.{{c.profile.durability}}, reliability = QoSReliabilityPolicy.{{c.profile.reliability}}, depth ={{c.profile.depth}})
		# ~ qos_profile_{{c.name}}.history = QoSHistoryPolicy.{{c.profile.history}}
		# ~ qos_profile_{{c.name}}.durability = QoSDurabilityPolicy.{{c.profile.durability}}
		# ~ qos_profile_{{c.name}}.reliability = QoSReliabilityPolicy.{{c.profile.reliability}}
		# ~ qos_profile_{{c.name}}.depth ={{c.profile.depth}}
		
		# ~ qos_profile_{{c.name}}.liveliness ={{c.profile.liveliness}}
		# ~ qos_profile_{{c.name}}.deadline.sec ={{c.profile.deadlineSec}}
		# ~ qos_profile_{{c.name}}.deadline.nsec ={{c.profile.deadlineNSec}}
		# ~ qos_profile_{{c.name}}.lifespan.sec ={{c.profile.lifespanSec}}
		# ~ qos_profile_{{c.name}}.lifespan.nsec ={{c.profile.lifespanNSec}}
		# ~ qos_profile_{{c.name}}.liveliness_lease_duration.sec ={{c.profile.liveliness_lease_durationSec}}
		# ~ qos_profile_{{c.name}}.liveliness_lease_duration.nsec ={{c.profile.liveliness_lease_durationNSec}}
		# ~ qos_profile_{{c.name}}.avoid_ros_namespace_conventions ={{c.profile.avoid_ros_namespace_conventions}}
		
		self.client_{{c.name}} = self.create_client({{c.type}}, '{{c.serviceName}}', qos_profile = qos_profile_{{c.name}})
		#_____
		{%endfor%}
		
		# Action Servers
		#____________________________________________
		{%for s in action_servers %}
		# {{s.name}}
		self.action_server_{{s.name}} = ActionServer(self, {{s.type}}, '{{s.name}}', execute_callback=self.action_execute_call_{{s.name}}, goal_callback=self.action_goal_call_{{s.name}}, cancel_callback=self.action_cancel_call_{{s.name}})
		#_____
		{%endfor%}
		
		# Action Clients
		#____________________________________________
		{%for s in action_clients %}
		# {{s.name}}
		self.action_client_{{s.name}} = ActionClient(self, {{s.type}}, '{{s.name}}')
		#_____
		{%endfor%}
		
		
		
	# ************Callbacks************
	# Publishers
	#____________________________________________
	{%for p in publishers %}
	# This is the callback of the publisher {{p.name}}. 
	# You can store the message in the msg object attributes, according 
	# to the instructions in the comments below. This function will be 
	# called automatically with the chosen publish rate, to publish your 
	# messages. This function is the template of the publisher callback 
	# and you should put your own functionality.
	def publisher_call_{{p.name}}(self):
		msg = {{p.type}}()
		# Please create the message of the publisher in this callback
		# Message after calculactions should be stored in
		{%for r in p.msg %}
		# msg.{{r}} 
		{%endfor%}
		
		{% if p.type == "ValueString" %}
		msg.x = 'Hello World: %d' % self.i
		{% endif %}
		
		{% if p.type == "ValueInt" %}
		msg.x = self.i
		
		
		self.publisher_{{p.name}}.publish(msg)
		self.get_logger().info('Publishing: "%s"' % msg.x)
		{% endif %}
		self.i += 1
	#_____
	{%endfor%}
	
	# Subscribers
	#____________________________________________
	{%for s in subscribers %}
	# This is the callback of the subscriber {{s.name}}. 
	# You can obtain the message from the variables set in this 
	# function, according to the instructions in the comments below. 
	# This function will be called automatically every time a message is
	# received. This function is the template of the subscriber callback 
	# and you should put your own functionality.
	def subscriber_call_{{s.name}}(self, msg):
		# Please obtain the message from the subscriber in this callback
		# Store the variables of the msg
		{%for r in s.msg %}
		{{r}} = msg.{{r}}
		{%endfor%}
		# Now you can use the received variables
		self.get_logger().info('I heard: '+str(msg.x))
	#_____
	{%endfor%}
	
	#Servers
	#____________________________________________
	{%for s in servers %}
	# This is the callback of the server {{s.name}}. 
	# You can obtain the request to the server from the variables set in 
	# this function, according to the instructions in the comments 
	# below. This function will be called automatically every time a 
	# request is received. This function is the template of the server 
	# callback and you should put your own functionality.
	def server_call_{{s.name}}(self, request, response):
		# Please add the server's functionality in this callback
		# Store the variables of the request
		{%for r in s.requests %}
		{{r}} = request.{{r}}
		{%endfor%}
		# Service result after calculactions should be stored in
		{%for r in s.responses %}
		# response.{{r}} 
		{%endfor%}
		response.c = request.a + request.b
		self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))
		return response
	#_____
	{%endfor%}
		
	# Clients
	#____________________________________________
	{%for c in clients %}
	# This is the call function of the client {{c.name}}. 
	# You can call this function, passing all the arguments of the 
	# service request declaration. This function will not be called 
	# automatically as you should call it to make a request. The 
	# function waits for the service to be available before going on and
	# the server's response is stored in a future object once the server
	# return the response. This function is the template of the client 
	# call and you should call it for applying requests.
	def client_call_{{c.name}}(self{%for r in c.requests %}, {{r }} {%endfor%}):
		# Wait for service
		while not self.client_{{c.name}}.wait_for_service(timeout_sec=1.0):
			self.get_logger().info('service not available, waiting again...')
		# Create request and fill it with data
		self.request_{{c.name}} = {{c.type}}.Request()
		{%for r in c.requests %}
		self.request_{{c.name}}.{{r}} = {{r}}
		{%endfor%}
		self.future_{{c.name}} = self.client_{{c.name}}.call_async(self.request_{{c.name}})
		# Result after server's response is stored in 
		{%for r in c.responses %}
		# self.future_{{c.name}}.result().{{r}} 
		{%endfor%}
	#_____
	{%endfor%}
			
	# Action Servers
	#____________________________________________
	{%for s in action_servers %}
	# This is the execute callback of the action server {{s.name}}. 
	# You can execute the goal request to the action server from the 
	# variables set in this function, according to the instructions in 
	# the comments below. This function will be called automatically 
	# every time an action goal request is received and needs to be 
	# executed. This function is the template of the action server 
	# callback and you should put your own functionality.
	def action_execute_call_{{s.name}}(self, goal_handle):
		# Please add the server's functionality in this callback
		self.get_logger().info('Executing goal...')
		# Store the variables of the goal request
		{%for r in s.goal %}
		{{r}} = goal_handle.request.{{r}}
		{%endfor%}
		# Create a feedback object
		feedback_msg = {{s.type}}.Feedback()
		# Every time you want to pass feedback update feedback attributes
		{%for r in s.feedback %}
		# feedback_msg.{{r}} = ...
		{%endfor%}
		# And call 
		# goal_handle.publish_feedback(feedback_msg)
		
		# Set the Result
		goal_handle.succeed()
		result = {{s.type}}.Result()
		# Fill the result with data
		{%for r in s.result %}
		# result.{{r}} = ...
		{%endfor%}
		return result
	
	# This is the goal callback of the action server {{s.name}}.
	# This function receives a client goal requests to handle actions.
	# This function is the template of the action server 
	# callback and you should put your own functionality.
	def action_goal_call_{{s.name}}(self,goal_request):
		# Please add the server's functionality in this callback
		self.get_logger().info('Received goal request')
		# Uncomment one of the following to reject or to accept an action request
		#return GoalResponse.REJECT
		return GoalResponse.ACCEPT
	
	# This is the cancel callback of the action server {{s.name}}.
	# This function receives client cancel requests to handle actions.
	# This function is the template of the action server 
	# callback and you should put your own functionality.
	def action_cancel_call_{{s.name}}(self, goal_handle):
		# Please add the server's functionality in this callback
		self.get_logger().info('Received cancel request')
		# Uncomment one of the following to reject or to accept an action request
		#return CancelResponse.REJECT
		return CancelResponse.ACCEPT
	#_____
	{%endfor%}
	
	# Action Clients
	#____________________________________________
	{%for c in action_clients %}
	# This is the call function of the action client {{c.name}}. 
	# You can call this function, passing all the arguments of the 
	# action goal request declaration. This function will not be called 
	# automatically as you should call it to make a request. The 
	# function waits for the action to be available before going on and
	# the action server's response is stored in a future object once 
	# the action server return the response. This function is the 
	# template of the action client call and you should call it for 
	# applying requests.
	def send_goal_call_{{c.name}}(self{%for r in c.goal %}, {{r }} {%endfor%}):
		# Wait for action service
		self.get_logger().info('Waiting for action server...')
		self.action_client_{{c.name}}.wait_for_server()
		# Create goal and fill it with data
		goal_msg = {{c.type}}.Goal()
		{%for r in c.goal %}
		goal_msg.{{r}} = {{r}}
		{%endfor%}
		# Send the goal request
		self.get_logger().info('Sending goal request...')
		self.future_{{c.name}} = self.action_client_{{c.name}}.send_goal_async(goal_msg, feedback_callback=self.feedback_client_call_{{c.name}})
		self.future_{{c.name}}.add_done_callback(self.goal_response_client_call_{{c.name}})
		
	# This is the feedback callback of the action client {{c.name}}.
	# This function receives and handles the feedback that the 
	# action server publishes. This function is the template of the 
	# action client callback and you should put your own 
	# functionality.
	def feedback_client_call_{{c.name}}(self, feedback):
		self.get_logger().info('received feedback')
		# Do something with the variables in feedback
		{%for r in c.feedback %}
		# feedback.feedback.{{r}}
		{%endfor%}
		
	# This is the response callback of the action client {{c.name}}.
	# This function receives and handles the response that the 
	# action server gives. This function is the template of the 
	# action client callback and you should put your own 
	# functionality.
	def goal_response_client_call_{{c.name}}(self, future):
		# Set the goal result
		goal_handle = future.result()
		# Check if the goal was accepted
		if not goal_handle.accepted:
			self.get_logger().info('Goal rejected :(')
			return
		# Goal Accepted
		self.get_logger().info('Goal accepted :)')
		# Create a callback for receiving the result async
		self.client_future_{{c.name}} = goal_handle.get_result_async()
		self.client_future_{{c.name}}.add_done_callback(self.get_result_call_{{c.name}})
		
	# This is the result callback of the action client {{c.name}}.
	# This function receives and final result that the 
	# action server returns. This function is the template of the 
	# action client callback and you should put your own 
	# functionality.
	def get_result_call_{{c.name}}(self, future):
		result = future.result().result
		status = future.result().status
		if status == GoalStatus.STATUS_SUCCEEDED:
			# Do something with the variables in result
			{%for r in c.result %}
			# result.{{r}}
			self.get_logger().info('Result obtained') 
			{%endfor%}
		else:
			self.get_logger().info('Goal failed with status: {0}'.format(status))

	#_____
	{%endfor%}
		
		
# Main executable
#____________________________________________
# This is the main executable for the node {{node.name}}.
# Run this executable from the root of the workspace using the command:
# $ ros2 run {{pack.name}} {{node.name}}_exec
#
# This executable creates a node with all its features and spins it to
# wait for its callbacks.
def main(args=None):
	rclpy.init(args=args)
	
	{{node.name}} = {{node.name}}_class()
		
	rclpy.spin({{node.name}})
	# Destroy the node explicitly
	# (optional - otherwise it will be done automatically
	# when the garbage collector destroys the node object)
	{%for s in action_servers %}
	# Destroy action server {{s.name}}
	{{node.name}}.action_server_{{s.name}}.destroy()
	{%endfor%}
	{%for c in action_clients %}
	# Destroy action server {{c.name}}
	{{node.name}}.action_client_{{c.name}}.destroy()
	{%endfor%}
	{{node.name}}.destroy_node()
	rclpy.shutdown()

# Clients executables
#____________________________________________
{%for c in clients %}
# This is the executable for the client {{c.name}}.
# Run this executable from the root of the workspace using the command:
# $ ros2 run {{pack.name}} {{node.name}}_{{c.name}} arg1 arg2 ...
#
# This executable creates a node and call its client's call. It spins 
# the node until the response from the server is received.
def run_{{c.name}}(args=None):
	rclpy.init(args=args)
	
	{{node.name}} = {{node.name}}_class()
	#TODO create typecast from command line to client call type (change int to custom type)
	{{node.name}}.client_call_{{c.name}}({%for r in c.requests %}int(sys.argv[{{loop.index}}]){% if not loop.last %}, {%endif%} {%endfor%})
	while rclpy.ok():
		rclpy.spin_once({{node.name}})
		if {{node.name}}.future_{{c.name}}.done():
			try:
				response = {{node.name}}.future_{{c.name}}.result()
			except Exception as e:
				{{node.name}}.get_logger().info('Service call failed %r' % (e,))
			else:
				{{node.name}}.get_logger().info(
				'Result of add_three_ints: for %d + %d = %d' %
				({{node.name}}.request_{{c.name}}.a, {{node.name}}.request_{{c.name}}.b, response.c))
			break
#_____
{%endfor%}
	
if __name__ == '__main__':
	main()
