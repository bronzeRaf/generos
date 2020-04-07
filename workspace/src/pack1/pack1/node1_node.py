
import rclpy
from rclpy.node import Node
import sys

from interfaces.msg import ValueString
from interfaces.msg import ValueInt


from interfaces.srv import Addtwo
from std_srvs.srv import SetBool

#*********
# ~ # ~ from interfaces.msg import ValueInt
# ~ # ~ from interfaces.msg import ValueString
# ~ # ~ # ~ from interfaces.srv import Addtwo
# ~ # ~ from interfaces.srv import SrFloatFloatString
# ~ # ~ from std_msgs.msg import 
# ~ from example_interfaces.srv import AddTwoInts

# Class for the node node1 
class node1_class(Node):
	
	# Constructor function of the node
	def __init__(self):
		super().__init__('node1')
		# Publishers
		#____________________________________________
		# publy3
		self.publisher_publy3= self.create_publisher(ValueString, 'topic/path3', 10)
		self.timer_publy3 = self.create_timer(12.0, self.publisher_call_publy3)
		self.i = 0
		#_____
		# publy2
		self.publisher_publy2= self.create_publisher(ValueInt, 'topic/path2', 10)
		self.timer_publy2 = self.create_timer(8.0, self.publisher_call_publy2)
		self.i = 0
		#_____
		
		# Subscribers
		#____________________________________________
		
		# Servers
		#____________________________________________
		# Server1
		self.server_Server1= self.create_service(Addtwo, 'add_two', self.server_call_Server1)
		#_____
		# Server3
		self.server_Server3= self.create_service(SetBool, 'set_bool', self.server_call_Server3)
		#_____
		
		# Clients
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
		msg = ValueString()
		# Please create the message of the publisher in this callback
		# Message after calculactions should be stored in
		# msg.x 
		
		msg.x = 'Hello World: %d' % self.i
		
		
		self.publisher_publy3.publish(msg)
		self.get_logger().info('Publishing: "%s"' % msg.x)
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
	node1.destroy_node()
	rclpy.shutdown()

# Clients executables
#____________________________________________
	
if __name__ == '__main__':
	main()