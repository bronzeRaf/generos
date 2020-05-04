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
publisher1 = metamodel.Publisher(name="publy1", topicPath = "topic/path1", publishRate = 5.0)
publisher2 = metamodel.Publisher(name="publy2", topicPath = "topic/path2", publishRate = 8.0)
publisher3 = metamodel.Publisher(name="publy3", topicPath = "topic/path3", publishRate = 12.0)
#set subscribers
subscriber1 = metamodel.Subscriber(name="suby1",topicPath = "topic/path1")
subscriber2 = metamodel.Subscriber(name="suby2",topicPath = "topic/path2")
subscriber3 = metamodel.Subscriber(name="suby3",topicPath = "topic/path3")
#set the topic messages
custommessage1 = metamodel.CustomMessage(name="ValueInt", description = "Message for passing a header and an integer")
custommessage2 = metamodel.CustomMessage(name="ValueString", description = "Message for testing purposes")
rosmessage1 = metamodel.RosMessage(name="Header", package = "std_msgs")
rosmessage2 = metamodel.RosMessage(name="Int32", package = "std_msgs")
#set the service messages
servicemessage1 = metamodel.CustomService(name = "Addtwo", description = "Service for receiving two numbers and returning their their sum")
servicemessage2 = metamodel.CustomService(name = "SrFloatFloatString", description = "Service for testing purposes")
servicemessage3 = metamodel.RosService(name="SetBool", package = "std_srvs")
#set the communication objects for the topics
tobject1 = metamodel.ObjectProperty(name="x", description = "x value for integer message")
dt1 = metamodel.Int(type = metamodel.IntType.int32)
tobject1.datatype = dt1
tobject2 = metamodel.ObjectProperty(name="x", description = "x value for string message")
dt2 = metamodel.String(type="string")
tobject2.datatype = dt2

tobject3 = metamodel.ObjectProperty(name="header", description = "header type object")
dt3 = metamodel.ROSData(type="Header",package="std_msgs")
tobject3.datatype = dt3

#set the request for the services
req1 = metamodel.Request()
req2 = metamodel.Request()
#set the response for the services
res1 = metamodel.Response()
res2 = metamodel.Response()
#set the communication objects for the services
sobject1 = metamodel.ObjectProperty(name="a", description = "a value for integer service Addtwo request 1")
st1 = metamodel.ROSData(type = "Int32", package="std_msgs")
sobject1.datatype = st1

sobject2 = metamodel.ObjectProperty(name="b", description = "b value for integer service Addtwo request 2")
st2 = metamodel.Int(type = metamodel.IntType.int64)
sobject2.datatype = st2

sobject3 = metamodel.ObjectProperty(name="c", description = "c value for integer service Addtwo response")
st3 = metamodel.Int(type = metamodel.IntType.int32)
sobject3.datatype = st3

sobject4 = metamodel.ObjectProperty(name="x", description = "x value for float service SrFloatFloatString request 1")
st4 = metamodel.Float(type = metamodel.FloatType.float64)
sobject4.datatype = st4

sobject5 = metamodel.ObjectProperty(name="y", description = "y value for float service SrFloatFloatString request 2")
st5 = metamodel.Float(type = metamodel.FloatType.float32)
sobject5.datatype = st5

sobject6 = metamodel.ObjectProperty(name="z", description = "z value for string service SrFloatFloatString response")
st6 = metamodel.String(type="string")
sobject6.datatype = st6

#set documentation
documentation1 = metamodel.Documentation()
documentation2 = metamodel.Documentation()
#set graph
graph1 = metamodel.Graph()
#set topology
topology1 = metamodel.Topology()
#set server
server1 = metamodel.Server(name = "Server1", servicePath = "ser/vice/path1", serviceName = "add_two")
server3 = metamodel.Server(name = "Server3", servicePath = "ser/vice/path3", serviceName = "set_bool")
#set client
client1 = metamodel.Client(name = "Client1", servicePath = "ser/vice/path1", serviceName = "add_two")
client2 = metamodel.Client(name = "Client2", servicePath = "ser/vice/path2", serviceName = "str")
client3 = metamodel.Client(name = "Client3", servicePath = "ser/vice/path3", serviceName = "set_bool")

#set parameters
param1 = metamodel.Parameter(name = "p1",  value = "32")

# ACTIONS
#set the action interfaces
action1 = metamodel.CustomActionInterface(name = "Increase", description = "Action for enabling counters")
#set the action
actionserver1 = metamodel.ActionServer(name = "action1")
#set client
actionclient1 = metamodel.ActionClient(name = "action1")

goal1 = metamodel.Goal()
result1 = metamodel.Result()
feedback1 = metamodel.Feedback()

ac1 = metamodel.ObjectProperty(name="start", description = "a value for start value")
acc1 = metamodel.Int(type = metamodel.IntType.int64)
ac1.datatype = acc1

ac2 = metamodel.ObjectProperty(name="goal", description = "a value for goal value")
acc2 = metamodel.Int(type = metamodel.IntType.int64)
ac2.datatype = acc2

ac3 = metamodel.ObjectProperty(name="update", description = "a value for feedback")
acc3 = metamodel.Int(type = metamodel.IntType.int64)
ac3.datatype = acc3

ac4 = metamodel.ObjectProperty(name="a", description = "a value for result trigger")
acc4 = metamodel.Int(type = metamodel.IntType.int64)
ac4.datatype = acc4

rosystem1.hasCustomActionInterfaces.extend([action1])	#0..*	system-customservice

action1.hasResult = result1
action1.hasGoal = goal1
action1.hasFeedback = feedback1

result1.hasObjectProperties.extend([ac4])
goal1.hasObjectProperties.extend([ac1])
goal1.hasObjectProperties.extend([ac2])
feedback1.hasObjectProperties.extend([ac3])

actionserver1.actioninterface=action1
actionclient1.actioninterface=action1
node1.hasActionServers.extend([actionserver1])				#0..*	node-action server
node2.hasActionClients.extend([actionclient1])				#0..*	node-action client



#QoS Profiles
qos1 = metamodel.CustomQosProfile(history = metamodel.QosHistory.KEEP_ALL, depth = 10, reliability = metamodel.QosReliability.RELIABLE, durability = metamodel.QosDurability.TRANSIENT_LOCAL)
rosystem1.hasCustomQosProfiles.extend([qos1])
publisher2.qosprofile = qos1
subscriber2.qosprofile = qos1

# ~ qos2 = metamodel.RosQosProfile(name = metamodel.QosPresetProfiles.SENSOR_DATA)
# ~ package1.hasRosQosProfiles.extend([qos2])
# ~ publisher2.qosprofile = qos2
# ~ subscriber2.qosprofile = qos2


#apply compositions
rosystem1.hasPackages.extend([package1])				#0..*	system-package
rosystem1.hasPackages.extend([package2])				#0..*	system-package
rosystem1.hasGraphs = graph1							#1..1	system-graph
rosystem1.topology = topology1							#1..1	system-topology
rosystem1.hasCustomMessages.extend([custommessage1])		#0..*	system-custommessage
rosystem1.hasCustomMessages.extend([custommessage2])		#0..*	system-custommessage
rosystem1.hasCustomServices.extend([servicemessage1])	#0..*	system-customservice
rosystem1.hasCustomServices.extend([servicemessage2])	#0..*	system-customservice
package1.hasDocumentation = documentation1				#1..1	package-documentation
package2.hasDocumentation = documentation2				#1..1	package-documentation

package1.hasNodes.extend([node1])						#0..*	package-node
package1.hasNodes.extend([node2])						#0..*	package-node
package2.hasNodes.extend([node3])						#0..*	package-node

package1.hasRosMessages.extend([rosmessage1])						#0..*	package-node
package1.hasRosServices.extend([servicemessage3])						#0..*	package-node

node1.hasPublishers.extend([publisher3])				#0..*	node-publisher
node1.hasPublishers.extend([publisher2])				#0..*	node-publisher
node3.hasSubscribers.extend([subscriber3])				#0..*	node-subscriber
node2.hasSubscribers.extend([subscriber2])				#0..*	node-subscriber

node1.hasServers.extend([server1])						#0..*	node-server
node1.hasServers.extend([server3])						#0..*	node-server
node2.hasClients.extend([client1])						#0..*	node-client
node2.hasClients.extend([client3])						#0..*	node-client
node3.hasClients.extend([client2])						#0..*	node-client

node1.hasParameters.extend([param1])					#0..*	node-parameter


custommessage1.hasObjectProperties.extend([tobject3])	#0..*	custommessage-objectproperty
custommessage1.hasObjectProperties.extend([tobject1])	#0..*	custommessage-objectproperty
custommessage2.hasObjectProperties.extend([tobject2])	#0..*	custommessage-objectproperty
servicemessage1.hasRequest = req1						#0..*	customservice-request
servicemessage2.hasRequest = req2						#0..*	customservice-request
servicemessage1.hasResponse = res1						#0..*	customservice-response
servicemessage2.hasResponse = res2						#0..*	customservice-response
req1.hasObjectProperties.extend([sobject1])				#0..*	request-CommunicationObject
req1.hasObjectProperties.extend([sobject2])				#0..*	request-CommunicationObject
req2.hasObjectProperties.extend([sobject4])				#0..*	request-CommunicationObject
req2.hasObjectProperties.extend([sobject5])				#0..*	request-CommunicationObject
res1.hasObjectProperties.extend([sobject3])				#0..*	response-CommunicationObject
res2.hasObjectProperties.extend([sobject6])				#0..*	response-CommunicationObject

#apply references
publisher3.pmsg = rosmessage1							#1..1	publisher-custommessage
publisher2.pmsg = custommessage1							#1..1	publisher-custommessage
subscriber3.smsg = rosmessage1						#1..1	subscriber-custommessage
subscriber2.smsg = custommessage1						#1..1	subscriber-custommessage

graph1.nodes.extend([node1, node2, node3])				#0..*	graph-nodes
server1.servicemessage = servicemessage1				#1..1	server-servicemessage
server3.servicemessage = servicemessage3				#1..1	server-servicemessage
client1.servicemessage = servicemessage1				#1..1	client-servicemessage
client2.servicemessage = servicemessage2				#1..1	client-servicemessage
client3.servicemessage = servicemessage3				#1..1	client-servicemessage

# ~ rset = ResourceSet()
model_res = rset.create_resource(URI('../models/test2.xmi'))
model_res.append(rosystem1)
model_res.save()
