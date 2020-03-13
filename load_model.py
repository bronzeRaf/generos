# This File reads the metamodel, reads the model and implements all 
# the behavior of the Classes to introduce ROS code in every component
# Written in 14/2/2020
# Written by Rafael Brouzos

from pyecore.resources import ResourceSet, URI, global_registry
from pyecore.resources.json import JsonResource
from pyecore.ecore import EClass, EAttribute
import pyecore.ecore as Ecore
from pyecoregen.ecore import EcoreGenerator 
import pyecore.behavior as behavior
from pyecore.utils import DynamicEPackage
import subprocess
import os
import rclpy


# We load the Ecore metamodel first
global_registry[Ecore.nsURI] = Ecore  
rset = ResourceSet()
resource = rset.get_resource(URI('/home/raf/Desktop/Thesis Project/ecoreWork/metamodel.ecore'))
# ~ rset.resource_factory['json'] = lambda uri: JsonResource(uri)
root = resource.contents[0]  # We get the root (an EPackage here)
# Register the metamodel (in case we open an XMI model later)
rset.metamodel_registry[root.nsURI] = root





#add behavior
# ~ roros = EClass('ROSSystem')
roros = DynamicEPackage(root)

#implement behavior
@roros.ROSSystem.behavior
def system_init(self):
	#build the system
	rclpy.init()
	os.system('mkdir '+self.name)
	os.system('mkdir '+self.name+'/src')
	os.chdir(self.name)
	subprocess.call('colcon build', shell=True)
	os.chdir('src')
	subprocess.call('pwd', shell=True)
	
	cmd1= 'chmod 755 ms.sh'
	subprocess.call(cmd1, shell=True, executable='/bin/bash')
	
	
	#build the Topology
	self.topology.topology_init()
	
	#build the Packages
	for x in self.hasPackages:
		x.package_init()
	
	#build the Graph
	self.hasGraphs.graph_init()
	
	print('Hello World and', self.name)
	
	
	for x in self.hasPackages:
		for y in x.hasNodes:
			for z in y.timers:
				
				y.node.destroy_timer(z)
			y.node.destroy_node()
	
	
	rclpy.shutdown()
	
	# this will print repr for a2, a4 and a3
	# ~ for child in self.eAllContents():
		# ~ print(child)
	# ~ self.topology.topology_init()

@roros.Package.behavior
def package_init(self):
	#build the package
	cmd = './ms.sh '+self.name
	subprocess.call(cmd, shell=True, executable='/bin/bash')
	
	#build the Documentation
	self.hasDocumentation.documentation_init()
	
	#build the Dependencies
	for x in self.hasDependencies:
		x.dependency_init()
		
	#build the Nodes
	os.chdir(self.name)
	os.chdir(self.name)
	for x in self.hasNodes:
		x.node_init()
		
	
	print('Hello World and', self.name)
	
	
@roros.Dependency.behavior
def dependency_init(self):
	#build the Dependency
	
	print('Hello World and', self.name)

	
@roros.Node.behavior
def node_init(self):
	#build  the Node
	self.node = rclpy.create_node(self.name)
	
	#build  the Parameters
	for x in self.hasParameters:
		x.parameter_init()
	
	#build  the Publishers
	self.timers = []
	for x in self.hasPublishers:
		self.timers.append(x.publisher_init(self.node))
	
	#build  the Subscribers
	for x in self.hasSubscribers:
		x.subscriber_init(self.node)
		
	#build  the Servers
	for x in self.hasServers:
		x.server_init(self)
	
	#build  the Clients
	for x in self.hasClients:
		x.client_init()
	
	if rclpy.ok():
		# ~ rclpy.spin_once(self.node)
		print('Hello World and', self.name)
	
	
@roros.Parameter.behavior
def parameter_init(self):
	#build the Parameter
	
	print('Hello World from parameter ', self.name)
	
	

	
@roros.Subscriber.behavior
def subscriber_init(self, node):
	from std_msgs.msg import String
	#build the Subscriber
	# ~ def listener_callback(msg):
		# ~ node.get_logger().info('I heard: "%s"' % msg.data)
		# ~ node.get_logger().info('I heard: nothing')
		
	# ~ subscription = node.create_subscription(self.smsg.datatype, self.topicPath, listener_callback, 10)
	
	# ~ rclpy.spin_once(node)
	
	print('Hello World from subscriber', self.name)
		

@roros.Publisher.behavior
def publisher_init(self, node):
	#build the Publisher file
	from std_msgs.msg import String
	from std_msgs.msg import Int64
	
	#build the Topic Message
	msg = self.pmsg.topicMessage_init()
	
	publisher = node.create_publisher(self.pmsg.datatype, self.topicPath, 10)
	
	i = 0
	def timer_callback():
		nonlocal i
		if self.pmsg.datatype == String:
			msg.data = 'Data in the msg iter '+str(i)
		elif self.pmsg.datatype == Int64:
			msg.data = 888
		i += 1
		node.get_logger().info('Publishing: "%s"' % msg.data)
		publisher.publish(msg)
	
	#run the timer
	timer = node.create_timer(self.publishRate, timer_callback)
	
	print('Hello World from publisher', self.name)
	
	rclpy.spin_once(node)
	return timer
	

@roros.TopicMessage.behavior
def topicMessage_init(self):
	#build the Topic Message
	
	if self.property.name == "String":
		from std_msgs.msg import String
		msg = String()
		self.datatype = String
		print("^^^^^^^^^^^^^^^^^^^^^^^^^^^ "+self.property.name)
	elif self.property.name == "Int":
		from std_msgs.msg import Int64
		msg = Int64()
		self.datatype = Int64
		print("^^^^^^^^^^^^^^^^^^^^^^^^^^^ "+self.property.name)
	elif self.property.name == "Float":
		from std_msgs.msg import Float64
		msg = Float64()
		self.datatype = Float64
		print("^^^^^^^^^^^^^^^^^^^^^^^^^^^ "+self.property.name)
		
	return msg
	print('Hello World from topic message')
	
		
@roros.Client.behavior
def client_init(self):
	#build the Client
	
	print('Hello World from client', self.name)



    
	
@roros.Server.behavior
def server_init(self, node):
	#build the Server
	# ~ from interfaces.srv import type1
	
	# ~ def add_two_ints_callback(request, response):
		# ~ response.sum = request.a + request.b + request.c
		# ~ node.get_logger().info(
			# ~ 'Incoming request\na: %d b: %d' % (request.a, request.b))
		# ~ return response
		
	# ~ #build the Service Message
	# ~ self.servicemessage.serviceMessage_init()
	# ~ self.srv = self.create_service(type1, 'type1', self.add_three_ints_callback)
	
	 
	print('Hello World from server', self.name)
	
	
@roros.ServiceMessage.behavior
def serviceMessage_init(self):
	#build the Service Message
	# ~ subprocess.call('mkdir srv', shell=True)
	os.chdir('srv')
	
	#build the Request
	self.hasRequest.request_init();
	
	#build the Response
	self.hasResponse.response_init();
	
	print('Hello World from service message', self.name)


@roros.Request.behavior
def request_init(self):
	#build the Service Request
	
	
	print('Hello World from request')

	
@roros.Response.behavior
def response_init(self):
	#build the Service Response
	
	print('Hello World from response')
	
	
@roros.Documentation.behavior
def documentation_init(self):
	#build the Documentation file
	
	print('Hello World from documentation')
	
	
@roros.Graph.behavior
def graph_init(self):
	#build the Communication Graph
	
	#build the Topics
	for x in self.hasTopics:
		x.topic_init()
	
	#build the ServiceLinks
	for x in self.hasServiceLinks:
		x.serviceLink_init()
		
	print('Hello World from graph')
	
	
@roros.Topic.behavior
def topic_init(self):
	#build the Topic
	
	print('Hello World from topic', self.topicPath)
	
	
@roros.ServiceLink.behavior
def serviceLink_init(self):
	#build the Service Link
	
	print('Hello World from service link', self.name)
	
	
@roros.Topology.behavior
def topology_init(self):
	#build the Topology
	
	#build the Local Network
	if self.network is not None:
		self.network.localNetwork_init()
		
	#build the Platforms
	for x in self.hasPlatforms:
		x.platform_init()
		
	print('Hello World from topology')
	
	
@roros.LocalNetwork.behavior
def localNetwork_init(self):
	#build the Local Network
	
	print('Hello World from local network')
		
		
@roros.Platform.behavior
def platform_init(self):
	#build the Platform
	
	#build the Hosts
	for x in self.hasHost:
		x.host_init()
	
	print('Hello World from platform')
	
	
@roros.Host.behavior
def host_init(self):
	#build the Host
	
	#build the Network Interfaces 
	for x in self.hasNetworkInterfaces:
		x.networkInterface_init()
		
	print('Hello World from host')
	
	
@roros.NetworkInterface.behavior
def networkInterface_init(self):
	#build Network Interface
	print('Hello World from network interface')
	


# We obtain the model from an XMI
model_root = rset.get_resource(URI('/home/raf/Desktop/Thesis Project/ecoreWork/test.xmi')).contents[0]
# ~ behavior.run(model_root)
model_root.system_init()
# ~ model_root.hasPackages[0].package_init()
# ~ for x in model_root.hasPackages[0].allInstances():
	# ~ print(x) # display 2 instances 
# ~ os.chdir('/home/raf/Desktop/Thesis Project/ecoreWork')
generator = EcoreGenerator()
generator.generate(model_root, 'oa2')
