
import rclpy
from rclpy.node import Node
import sys

from interfaces.msg import ValueString
from std_msgs.msg import Int32


#*********
from interfaces.msg import ValueInt
from interfaces.msg import ValueString
from interfaces.srv import Addtwo
from interfaces.srv import SrFloatFloatString
# ~ from std_msgs.msg import 
# ~ from example_interfaces.srv import AddTwoInts


class node1_class(Node):

	def __init__(self):
		super().__init__('node1')
		# Publishers
		#____________________________________________
		self.publisher_publy3= self.create_publisher(ValueString, 'topic/path3', 10)
		self.timer_publy3 = self.create_timer(12.0, self.publisher_call_publy3)
		self.i = 0
		#____________________________________________
		self.publisher_publy2= self.create_publisher(Int32, 'topic/path2', 10)
		self.timer_publy2 = self.create_timer(8.0, self.publisher_call_publy2)
		self.i = 0
		#____________________________________________
		
		# Subscribers
		#____________________________________________
		
		# Servers
		#____________________________________________
		self.server_Server1= self.create_service(Addtwo, 'add_two', self.server_call_Server1)
		#____________________________________________
		
		# Clients
		#____________________________________________
		
		
	# ************Calls************
	# Publishers
	#____________________________________________
	def publisher_call_publy3(self):
		msg = ValueString()
		
		# Message after calculactions should be stored in
		# msg.x 
		
		msg.x = 'Hello World: %d' % self.i
		
		
		self.publisher_publy3.publish(msg)
		self.get_logger().info('Publishing: "%s"' % msg.x)
		self.i += 1
	#____________________________________________
	def publisher_call_publy2(self):
		msg = Int32()
		
		# Message after calculactions should be stored in
		
		
		
		self.publisher_publy2.publish(msg)
		self.get_logger().info('Publishing: "%s"' % msg.data)
		self.i += 1
	#____________________________________________
	
	# Subscribers
	#____________________________________________
	
	#Servers
	#____________________________________________
	def server_call_Server1(self, request, response):
		# Store the variables of the request
		a = request.a
		b = request.b
		# Service result after calculactions should be stored in
		# response.c 
		response.c = request.a + request.b
		self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))
		return response
	#____________________________________________
		
	# Clients
	#____________________________________________
		
		
		
# Main executable
#____________________________________________
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
