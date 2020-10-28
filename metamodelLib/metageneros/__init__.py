
from .metageneros import getEClassifier, eClassifiers
from .metageneros import name, nsURI, nsPrefix, eClass
from .metageneros import ROSSystem, Topology, Package, Software, ROSVersion, CustomQosProfile, QosHistory, QosReliability, QosDurability, QosProfile, RosQosProfile, QosLiveliness, QosPresetProfiles, Graph, ActionLink, Topic, ServiceLink, SystemGraph, CustomPackage, RosPackage, PackageDependency, TopicMessage, RosMessage, ServiceMessage, RosService, ActionInterface, CustomActionInterface, Goal, Result, Feedback, CustomService, Request, Response, CustomMessage, ActionServer, ActionClient, Dependency, Documentation, DataTypes, Client, Node, Subscriber, Publisher, Server, Parameter, ObjectProperty, Datatype, Bool, String, Number, Int, Uint, Float, UIntType, IntType, FloatType, ROSData, Array, UintArray, FloatArray, IntArray, IntArrayType, UIntArrayType, FloatArrayType, PackageGraph, Deployment, Platform, LocalNetwork, Host, AritectureTypes, OSType, NetworkInterface


from . import metageneros

__all__ = ['ROSSystem', 'Topology', 'Package', 'Software', 'ROSVersion', 'CustomQosProfile', 'QosHistory', 'QosReliability', 'QosDurability', 'QosProfile', 'RosQosProfile', 'QosLiveliness', 'QosPresetProfiles', 'Graph', 'ActionLink', 'Topic', 'ServiceLink', 'SystemGraph', 'CustomPackage', 'RosPackage', 'PackageDependency', 'TopicMessage', 'RosMessage', 'ServiceMessage', 'RosService', 'ActionInterface', 'CustomActionInterface', 'Goal', 'Result', 'Feedback', 'CustomService', 'Request', 'Response',
           'CustomMessage', 'ActionServer', 'ActionClient', 'Dependency', 'Documentation', 'DataTypes', 'Client', 'Node', 'Subscriber', 'Publisher', 'Server', 'Parameter', 'ObjectProperty', 'Datatype', 'Bool', 'String', 'Number', 'Int', 'Uint', 'Float', 'UIntType', 'IntType', 'FloatType', 'ROSData', 'Array', 'UintArray', 'FloatArray', 'IntArray', 'IntArrayType', 'UIntArrayType', 'FloatArrayType', 'PackageGraph', 'Deployment', 'Platform', 'LocalNetwork', 'Host', 'AritectureTypes', 'OSType', 'NetworkInterface']

eSubpackages = []
eSuperPackage = None
metageneros.eSubpackages = eSubpackages
metageneros.eSuperPackage = eSuperPackage

ROSSystem.hasTopology.eType = Topology
ROSSystem.hasSoftware.eType = Software
ROSSystem.hasSystemGraph.eType = SystemGraph
Topology.hasPlatforms.eType = Platform
Topology.network.eType = LocalNetwork
Package.hasDependencies.eType = Dependency
Package.hasNodes.eType = Node
Package.hasDocumentation.eType = Documentation
Package.hasTopicMessages.eType = TopicMessage
Package.hasServiceMessages.eType = ServiceMessage
Package.hasActionInterfaces.eType = ActionInterface
Package.hasDeployments.eType = Deployment
Software.hasPackages.eType = Package
Software.hasQosProfiles.eType = QosProfile
Graph.hasTopics.eType = Topic
Graph.hasServiceLinks.eType = ServiceLink
Graph.nodes.eType = Node
Graph.hasActionLinks.eType = ActionLink
ActionLink.actionserver.eType = ActionServer
ActionLink.actionclient.eType = ActionClient
Topic.publisher.eType = Publisher
Topic.subscriber.eType = Subscriber
ServiceLink.server.eType = Server
ServiceLink.client.eType = Client
SystemGraph.graph.eType = Graph
SystemGraph.packagegraph.eType = PackageGraph
PackageDependency.package.eType = Package
CustomActionInterface.hasGoal.eType = Goal
CustomActionInterface.hasResult.eType = Result
CustomActionInterface.hasFeedback.eType = Feedback
Goal.hasObjectProperties.eType = ObjectProperty
Result.hasObjectProperties.eType = ObjectProperty
Feedback.hasObjectProperties.eType = ObjectProperty
CustomService.hasRequest.eType = Request
CustomService.hasResponse.eType = Response
Request.hasObjectProperties.eType = ObjectProperty
Response.hasObjectProperties.eType = ObjectProperty
CustomMessage.hasObjectProperties.eType = ObjectProperty
ActionServer.actioninterface.eType = ActionInterface
ActionClient.actioninterface.eType = ActionInterface
Client.servicemessage.eType = ServiceMessage
Client.qosprofile.eType = QosProfile
Node.hasSubscribers.eType = Subscriber
Node.hasPublishers.eType = Publisher
Node.hasClients.eType = Client
Node.hasServers.eType = Server
Node.hasParameters.eType = Parameter
Node.hasActionServers.eType = ActionServer
Node.hasActionClients.eType = ActionClient
Subscriber.smsg.eType = TopicMessage
Subscriber.qosprofile.eType = QosProfile
Publisher.pmsg.eType = TopicMessage
Publisher.qosprofile.eType = QosProfile
Server.servicemessage.eType = ServiceMessage
Server.qosprofile.eType = QosProfile
ObjectProperty.datatype.eType = Datatype
PackageGraph.package.eType = Package
Deployment.nodes.eType = Node
Deployment.host.eType = Host
Platform.hasHost.eType = Host
Host.hasNetworkInterfaces.eType = NetworkInterface

otherClassifiers = [ROSVersion, QosHistory, QosReliability, QosDurability, QosLiveliness, QosPresetProfiles,
                    DataTypes, UIntType, IntType, FloatType, IntArrayType, UIntArrayType, FloatArrayType, AritectureTypes, OSType]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
