from pyecore.resources import ResourceSet, URI, global_registry
from pyecore.resources.json import JsonResource
from pyecore.ecore import EClass, EAttribute, EObject
import pyecore.ecore as Ecore  # We get a reference to the Ecore metamodle implem.
from pyecoregen.ecore import EcoreGenerator 
import pyecore.behavior as behavior
from pyecore.utils import DynamicEPackage
import sys
sys.path.append('../metamodelLib')
import metamodel

#create rset
global_registry[Ecore.nsURI] = Ecore  
rset = ResourceSet()
rset.metamodel_registry[metamodel.nsURI] = metamodel

rosystem1 = metamodel.ROSSystem(name = "My_first_ROS_system")
#set system
rosystem1.name = "My_first_ROS_system2"
#set packages
package1 = metamodel.Package(name = "pack1", rosVersion = 0, packagePath = "path to pack1")
package2 = metamodel.Package(name = "pack2", rosVersion = 0, packagePath = "path to pack2")
#set nodes
node1 = metamodel.Node(name="node1")
node2 = metamodel.Node(name="node2")
node3 = metamodel.Node(name="node3")
#set publishers
publisher1 = metamodel.Publisher(name="publy1", topicPath = "topic/path1", publishRate = 0.5)
publisher2 = metamodel.Publisher(name="publy2", topicPath = "topic/path2", publishRate = 0.8)
publisher3 = metamodel.Publisher(name="publy3", topicPath = "topic/path3", publishRate = 0.3)
#set subscribers
subscriber1 = metamodel.Subscriber(name="suby1",topicPath = "topic/path1")
subscriber2 = metamodel.Subscriber(name="suby2",topicPath = "topic/path2")
subscriber3 = metamodel.Subscriber(name="suby3",topicPath = "topic/path3")
#set the topic messages
topicmessage1 = metamodel.TopicMessage(name="ValueInt")
topicmessage2 = metamodel.TopicMessage(name="ValueString")
#set the service messages
servicemessage1 = metamodel.ServiceMessage(name = "Addtwo")
servicemessage2 = metamodel.ServiceMessage(name = "SrFloatFloatString")
#set the communication objects for the topics
tobject1 = metamodel.CommunicationObject(name="x", type = metamodel.DataTypes.int32)
tobject2 = metamodel.CommunicationObject(name="x", type = metamodel.DataTypes.string)
#set the request for the services
req1 = metamodel.Request()
req2 = metamodel.Request()
#set the response for the services
res1 = metamodel.Response()
res2 = metamodel.Response()
#set the communication objects for the services
sobject1 = metamodel.CommunicationObject(name="a", type = metamodel.DataTypes.int32)
sobject2 = metamodel.CommunicationObject(name="b", type = metamodel.DataTypes.int32)
sobject3 = metamodel.CommunicationObject(name="c", type = metamodel.DataTypes.int32)
sobject4 = metamodel.CommunicationObject(name="x", type = metamodel.DataTypes.float32)
sobject5 = metamodel.CommunicationObject(name="y", type = metamodel.DataTypes.float32)
sobject6 = metamodel.CommunicationObject(name="z", type = metamodel.DataTypes.string)
#set documentation
documentation1 = metamodel.Documentation()
documentation2 = metamodel.Documentation()
#set graph
graph1 = metamodel.Graph()
#set topology
topology1 = metamodel.Topology()
#set server
server1 = metamodel.Server(name = "Server1", servicePath = "ser/vice/path1")
#set client
client1 = metamodel.Client(name = "Client1", servicePath = "ser/vice/path1")

#apply compositions
rosystem1.hasPackages.extend([package1])				#0..*	system-package
rosystem1.hasPackages.extend([package2])				#0..*	system-package
rosystem1.hasGraphs = graph1							#1..1	system-graph
rosystem1.topology = topology1							#1..1	system-topology
rosystem1.hasTopicMessages.extend([topicmessage1])		#0..*	system-topicmessage
rosystem1.hasTopicMessages.extend([topicmessage2])		#0..*	system-topicmessage
rosystem1.hasServiceMessages.extend([servicemessage1])	#0..*	system-servicemessage
rosystem1.hasServiceMessages.extend([servicemessage2])	#0..*	system-servicemessage
package1.hasDocumentation = documentation1				#1..1	package-documentation
package2.hasDocumentation = documentation2				#1..1	package-documentation
package1.hasNodes.extend([node1])						#0..*	package-node
package1.hasNodes.extend([node2])						#0..*	package-node
package2.hasNodes.extend([node3])						#0..*	package-node
node1.hasPublishers.extend([publisher1])				#0..*	node-publisher
node1.hasPublishers.extend([publisher3])				#0..*	node-publisher
node3.hasSubscribers.extend([subscriber1])				#0..*	node-subscriber
node2.hasSubscribers.extend([subscriber2])				#0..*	node-subscriber
node1.hasServers.extend([server1])						#0..*	node-server
node2.hasClients.extend([client1])						#0..*	node-client
topicmessage1.hasCommunicationObjects.extend([tobject1])#0..*	topicmessage-CommunicationObject
topicmessage2.hasCommunicationObjects.extend([tobject2])#0..*	topicmessage-CommunicationObject
servicemessage1.hasRequest = req1						#0..*	servicemessage-request
servicemessage2.hasRequest = req2						#0..*	servicemessage-request
servicemessage1.hasResponse = res1						#0..*	servicemessage-response
servicemessage2.hasResponse = res2						#0..*	servicemessage-response
req1.hasCommunicationObjects.extend([sobject1])			#0..*	request-CommunicationObject
req1.hasCommunicationObjects.extend([sobject2])			#0..*	request-CommunicationObject
req2.hasCommunicationObjects.extend([sobject4])			#0..*	request-CommunicationObject
req2.hasCommunicationObjects.extend([sobject5])			#0..*	request-CommunicationObject
res1.hasCommunicationObjects.extend([sobject3])			#0..*	response-CommunicationObject
res2.hasCommunicationObjects.extend([sobject6])			#0..*	response-CommunicationObject

#apply references
publisher1.pmsg = topicmessage1							#1..1	publisher-topicmessage
publisher3.pmsg = topicmessage2							#1..1	publisher-topicmessage
subscriber1.smsg = topicmessage1						#1..1	subscriber-topicmessage
subscriber2.smsg = topicmessage2						#1..1	subscriber-topicmessage
graph1.nodes.extend([node1, node2, node3])				#0..*	graph-nodes
server1.servicemessage = servicemessage1				#1..1	server-servicemessage
client1.servicemessage = servicemessage1				#1..1	client-servicemessage

# ~ rset = ResourceSet()
model_res = rset.create_resource(URI('../models/test2.xmi'))
model_res.append(rosystem1)
model_res.save()
