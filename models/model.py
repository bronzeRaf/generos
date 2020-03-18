from pyecore.resources import ResourceSet, URI, global_registry
from pyecore.resources.json import JsonResource
from pyecore.ecore import EClass, EAttribute, EObject
import pyecore.ecore as Ecore  # We get a reference to the Ecore metamodle implem.
from pyecoregen.ecore import EcoreGenerator 
import pyecore.behavior as behavior
from pyecore.utils import DynamicEPackage
 
global_registry[Ecore.nsURI] = Ecore  # We load the Ecore metamodel first
rset = ResourceSet()
resource = rset.get_resource(URI('../metamodel.ecore'))
# ~ rset.resource_factory['json'] = lambda uri: JsonResource(uri)
root = resource.contents[0]  # We get the root (an EPackage here)
rset.metamodel_registry[root.nsURI] = root



ROSSystem = root.getEClassifier('ROSSystem')
Package = root.getEClassifier('Package')
Node = root.getEClassifier('Node')
Publisher = root.getEClassifier('Publisher')
Subscriber = root.getEClassifier('Subscriber')
TopicMessage = root.getEClassifier('TopicMessage')
CommunicationObject = root.getEClassifier('CommunicationObject')
Documentation = root.getEClassifier('Documentation')
Graph = root.getEClassifier('Graph')
Topology = root.getEClassifier('Topology')
DataType = root.getEClassifier('DataTypes')
ServiceMessage = root.getEClassifier('ServiceMessage')
Server = root.getEClassifier('Server')
Response = root.getEClassifier('Response')
Request = root.getEClassifier('Request')

#set system
rosystem1 = ROSSystem()
rosystem1.name = "My_first_ROS_system"

#set package
package1 = Package()
package1.name = "pack1"
package1.ROSVersion = 'eloquent'
package1.packagePath = "path to pack1"
#set node
node1 = Node()
node1.name = "Nodes_name"
node2 = Node()
node2.name = "Node_2"
node3 = Node()
node3.name = "Node_3"
#set publisher
publisher1 = Publisher()
publisher1.name = "publy1"
publisher1.topicPath = "topic/path"
publisher1.publishRate = 0.5
publisher3 = Publisher()
publisher3.name = "publy3"
publisher3.topicPath = "topic/path2"
publisher3.publishRate = 0.8
#set subscriber
subscriber1 = Subscriber()
subscriber1.name = "suby1"
subscriber1.topicPath = "topic/path"
#set the topic messages
topicmessage1 = TopicMessage()
topicmessage1.name = "valueInt"
topicmessage2 = TopicMessage()
topicmessage2.name = "valueString"
#set the service messages
servicemessage1 = ServiceMessage()
servicemessage1.name = "srIntInt_Int"
servicemessage2 = ServiceMessage()
servicemessage2.name = "srFloatFloat_String"
#set the communication objects for the topics
tobject1 = CommunicationObject()
tobject1.name = "x"
tobject1.type = DataType.Int
tobject2 = CommunicationObject()
tobject2.name = "s"
tobject2.type = DataType.String
#set the request for the services
req1 = Request()
req2 = Request()
#set the response for the services
res1 = Response()
res2 = Response()
#set the communication objects for the services
sobject1 = CommunicationObject()
sobject1.name = "a"
sobject1.type = DataType.Int
sobject2 = CommunicationObject()
sobject2.name = "b"
sobject2.type = DataType.Int
sobject3 = CommunicationObject()
sobject3.name = "c"
sobject3.type = DataType.Int
sobject4 = CommunicationObject()
sobject4.name = "x"
sobject4.type = DataType.Float
sobject5 = CommunicationObject()
sobject5.name = "y"
sobject5.type = DataType.Float
sobject6 = CommunicationObject()
sobject6.name = "z"
sobject6.type = DataType.String
#set documentation
documentation1 = Documentation()
#set graph
graph1 = Graph()
#set topology
topology1 = Topology()
#set server
server1 = Server()
server1.name = "Server-1"
server1.servicePath = "ser/vice/path"

#apply compositions
rosystem1.hasPackages.extend([package1])				#0..*	system-package
rosystem1.hasGraphs = graph1							#1..1	system-graph
rosystem1.topology = topology1							#1..1	system-topology
package1.hasDocumentation = documentation1				#1..1	package-documentation
package1.hasNodes.extend([node1])						#0..*	package-node
package1.hasNodes.extend([node2])						#0..*	package-node
package1.hasNodes.extend([node3])						#0..*	package-node
package1.hasTopicMessages.extend([topicmessage1])		#0..*	package-topicmessage
package1.hasTopicMessages.extend([topicmessage2])		#0..*	package-topicmessage
package1.hasServiceMessages.extend([servicemessage1])	#0..*	package-servicemessage
package1.hasServiceMessages.extend([servicemessage2])	#0..*	package-servicemessage
node1.hasPublishers.extend([publisher1])				#0..*	node-publisher
node3.hasPublishers.extend([publisher3])				#0..*	node-publisher
node2.hasSubscribers.extend([subscriber1])				#0..*	node-subscriber
node2.hasServers.extend([server1])						#0..*	node-server
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
graph1.nodes.extend([node1, node2, node3])				#0..*	graph-nodes
server1.servicemessage = servicemessage1				#1..1	server-servicemessage

# ~ rosystem1.system_init();
# ~ behavior.run(root)

#save the model resource
model_res = rset.create_resource(URI('../models/test.xmi'))
# ~ model_res = XMIResource(URI('/home/raf/Desktop/Thesis Project/ecoreWork/test.xmi'))

model_res.append(rosystem1)
model_res.save()
# ~ model_res.append(package1)
# ~ model_res.append(node1)
# ~ model_res.append(documentation1)
# ~ model_res.append(graph1)
# ~ model_res.append(topology1)

#generate code
# ~ rset.metamodel_registry[root.nsURI] = root
# ~ generator = EcoreGenerator()
# ~ generator.generate(rosystem1, 'oa23')
