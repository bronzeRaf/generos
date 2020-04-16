
from .metamodel import getEClassifier, eClassifiers
from .metamodel import name, nsURI, nsPrefix, eClass
from .metamodel import Client, Node, Subscriber, Publisher, Server, Parameter, Package, Dependency, Documentation, DataTypes, Graph, Topic, ServiceLink, CustomService, Request, Response, CustomMessage, ROSSystem, Topology, Platform, LocalNetwork, Host, ActionServer, ActionClient, ROSVersion, AritectureTypes, OSType, NetworkInterface, ObjectProperty, Datatype, Bool, String, Number, Int, Uint, Float, UIntType, IntType, FloatType, ROSData, Array, UintArray, FloatArray, IntArray, IntArrayType, UIntArrayType, FloatArrayType, Enumeration, Element, TopicMessage, RosMessage, ServiceMessage, RosService, ActionInterface, CustomActionInterface, Goal, Result, Feedback


from . import metamodel

__all__ = ['Client', 'Node', 'Subscriber', 'Publisher', 'Server', 'Parameter', 'Package', 'Dependency', 'Documentation', 'DataTypes', 'Graph', 'Topic', 'ServiceLink', 'CustomService', 'Request', 'Response', 'CustomMessage', 'ROSSystem', 'Topology', 'Platform', 'LocalNetwork', 'Host', 'ActionServer', 'ActionClient', 'ROSVersion', 'AritectureTypes', 'OSType', 'NetworkInterface',
           'ObjectProperty', 'Datatype', 'Bool', 'String', 'Number', 'Int', 'Uint', 'Float', 'UIntType', 'IntType', 'FloatType', 'ROSData', 'Array', 'UintArray', 'FloatArray', 'IntArray', 'IntArrayType', 'UIntArrayType', 'FloatArrayType', 'Enumeration', 'Element', 'TopicMessage', 'RosMessage', 'ServiceMessage', 'RosService', 'ActionInterface', 'CustomActionInterface', 'Goal', 'Result', 'Feedback']

eSubpackages = []
eSuperPackage = None
metamodel.eSubpackages = eSubpackages
metamodel.eSuperPackage = eSuperPackage

Client.servicemessage.eType = ServiceMessage
Node.hasSubscribers.eType = Subscriber
Node.hasPublishers.eType = Publisher
Node.hasClients.eType = Client
Node.hasServers.eType = Server
Node.hasParameters.eType = Parameter
Node.hasActionServers.eType = ActionServer
Node.hasActionClients.eType = ActionClient
Subscriber.smsg.eType = TopicMessage
Publisher.pmsg.eType = TopicMessage
Server.servicemessage.eType = ServiceMessage
Package.hasDependencies.eType = Dependency
Package.hasNodes.eType = Node
Package.hasDocumentation.eType = Documentation
Package.hasRosMessages.eType = RosMessage
Package.hasRosServices.eType = RosService
Graph.hasTopics.eType = Topic
Graph.hasServiceLinks.eType = ServiceLink
Graph.nodes.eType = Node
Topic.publisher.eType = Publisher
Topic.subscriber.eType = Subscriber
ServiceLink.server.eType = Server
ServiceLink.client.eType = Client
CustomService.hasRequest.eType = Request
CustomService.hasResponse.eType = Response
Request.hasObjectProperties.eType = ObjectProperty
Response.hasObjectProperties.eType = ObjectProperty
CustomMessage.hasObjectProperties.eType = ObjectProperty
ROSSystem.topology.eType = Topology
ROSSystem.hasPackages.eType = Package
ROSSystem.hasGraphs.eType = Graph
ROSSystem.hasCustomMessages.eType = CustomMessage
ROSSystem.hasCustomServices.eType = CustomService
ROSSystem.hasCustomActionInterfaces.eType = CustomActionInterface
Topology.hasPlatforms.eType = Platform
Topology.network.eType = LocalNetwork
Platform.hasHost.eType = Host
Host.hasNetworkInterfaces.eType = NetworkInterface
ActionServer.actioninterface.eType = ActionInterface
ActionClient.actioninterface.eType = ActionInterface
ObjectProperty.datatype.eType = Datatype
Enumeration.hasElements.eType = Element
CustomActionInterface.hasGoal.eType = Goal
CustomActionInterface.hasResult.eType = Result
CustomActionInterface.hasFeedback.eType = Feedback
Goal.hasObjectProperties.eType = ObjectProperty
Result.hasObjectProperties.eType = ObjectProperty
Feedback.hasObjectProperties.eType = ObjectProperty

otherClassifiers = [DataTypes, ROSVersion, AritectureTypes, OSType, UIntType,
                    IntType, FloatType, IntArrayType, UIntArrayType, FloatArrayType]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
