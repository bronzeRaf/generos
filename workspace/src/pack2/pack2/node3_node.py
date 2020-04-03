
import rclpy
from rclpy.node import Node
import sys


from interfaces.msg import ValueString

#*********
from interfaces.msg import ValueInt
from interfaces.msg import ValueString
from interfaces.srv import Addtwo
from interfaces.srv import SrFloatFloatString
# ~ from std_msgs.msg import 
# ~ from example_interfaces.srv import AddTwoInts


class node3_class(Node):

	def __init__(self):
		super().__init__('node3')
		# Publishers
		#____________________________________________
		
		# Subscribers
		#____________________________________________
		self.subscriber_suby3= self.create_subscription(ValueString, 'topic/path3', self.subscriber_call_suby3, 10)
		self.subscriber_suby3
		#____________________________________________
		
		# Servers
		#____________________________________________
		
		# Clients
		#____________________________________________
		self.client_Client2= self.create_client(SrFloatFloatString, 'str')
		#____________________________________________
		
		
	# ************Calls************
	# Publishers
	#____________________________________________
	
	# Subscribers
	#____________________________________________
	def subscriber_call_suby3(self, msg):
		# Store the variables of the msg
		x = msg.x
		self.get_logger().info('I heard: '+str(msg.x))
	#____________________________________________
	
	#Servers
	#____________________________________________
		
	# Clients
	#____________________________________________
	def client_call_Client2(self, x, y):
		while not self.client_Client2.wait_for_service(timeout_sec=1.0):
			self.get_logger().info('service not available, waiting again...')
		self.request_Client2 = SrFloatFloatString.Request()
		self.request_Client2.x = x
		self.request_Client2.y = y
		self.future_Client2 = self.client_Client2.call_async(self.request_Client2)
		# Result after server's response is stored in 
		# self.future_Client2.result().z 
	#____________________________________________
		
		
		
# Main executable
#____________________________________________
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
def Client2(args=None):
	rclpy.init(args=args)
	
	node3 = node3_class()
	#TODO create typecast from command line to client call type (change int to custom type)
	node3.client_call_Client2(int(sys.argv[1]), int(sys.argv[2]))
	while rclpy.ok():
		rclpy.spin_once(node3)
		if node3.future_Client2.done():
			try:
				response = node3.future_Client2.result()
			except Exception as e:
				node3.get_logger().info('Service call failed %r' % (e,))
			else:
				node3.get_logger().info(
				'Result of add_three_ints: for %d + %d = %d' %
				(node3.request_Client2.a, node3.request_Client2.b, response.c))
			break
	
	
if __name__ == '__main__':
	main()