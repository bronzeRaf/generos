"""Definition of meta model 'metageneros'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *


name = 'metageneros'
nsURI = 'http://www.example.org/metageneros'
nsPrefix = 'metageneros'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
ROSVersion = EEnum('ROSVersion', literals=['Ardent_Apalone', 'Bouncy_Bolson',
                                           'Crystal_Clemmys', 'Dashing_Diademata', 'Eloquent_Elusor', 'Foxy_Fitzroy'])

QosHistory = EEnum('QosHistory', literals=['SYSTEM_DEFAULT', 'KEEP_LAST', 'KEEP_ALL'])

QosReliability = EEnum('QosReliability', literals=['SYSTEM_DEFAULT', 'RELIABLE', 'BEST_EFFORT'])

QosDurability = EEnum('QosDurability', literals=['SYSTEM_DEFAULT', 'TRANSIENT_LOCAL', 'VOLATILE'])

QosLiveliness = EEnum('QosLiveliness', literals=[
                      'SYSTEM_DEFAULT', 'AUTOMATIC', 'MANUAL_BY_NODE', 'MANUAL_BY_TOPIC', 'UKNOWN'])

QosPresetProfiles = EEnum('QosPresetProfiles', literals=[
                          'DEFAULT', 'SYSTEM_DEFAULT', 'SENSOR_DATA', 'SERVICES_DEFAULT', 'PARAMETERS', 'PARAMETER_EVENTS', 'ACTION_STATUS_DEFAULT'])

DataTypes = EEnum('DataTypes', literals=['NOT_SET', 'BOOL', 'INTEGER', 'DOUBLE', 'STRING',
                                         'BYTE_ARRAY', 'BOOL_ARRAY', 'INTEGER_ARRAY', 'DOUBLE_ARRAY', 'STRING_ARRAY'])

UIntType = EEnum('UIntType', literals=['uint8', 'uint16', 'uint32', 'uint64'])

IntType = EEnum('IntType', literals=['int8', 'int16', 'int32', 'int64'])

FloatType = EEnum('FloatType', literals=['float32', 'float64'])

IntArrayType = EEnum('IntArrayType', literals=['int8[]', 'int16[]', 'int32[]', 'int64[]'])

UIntArrayType = EEnum('UIntArrayType', literals=['uint8[]', 'uint16[]', 'uint32[]', 'uint64[]'])

FloatArrayType = EEnum('FloatArrayType', literals=['float32[]', 'float64[]'])

AritectureTypes = EEnum('AritectureTypes', literals=['x86', 'x64'])

OSType = EEnum('OSType', literals=['Ubuntu_14', 'Ubuntu_16', 'Ubuntu_18'])


class ROSSystem(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True, default_value='workspace')
    hasTopology = EReference(ordered=True, unique=True, containment=True)
    hasSoftware = EReference(ordered=True, unique=True, containment=True)
    hasSystemGraph = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, name=None, hasTopology=None, hasSoftware=None, hasSystemGraph=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if hasTopology is not None:
            self.hasTopology = hasTopology

        if hasSoftware is not None:
            self.hasSoftware = hasSoftware

        if hasSystemGraph is not None:
            self.hasSystemGraph = hasSystemGraph


class Topology(EObject, metaclass=MetaEClass):

    hasPlatforms = EReference(ordered=True, unique=True, containment=True, upper=-1)
    network = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, hasPlatforms=None, network=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if hasPlatforms:
            self.hasPlatforms.extend(hasPlatforms)

        if network is not None:
            self.network = network


@abstract
class Package(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    rosVersion = EAttribute(eType=ROSVersion, derived=False, changeable=True, upper=-1)
    packagePath = EAttribute(eType=EString, derived=False, changeable=True)
    license = EAttribute(eType=EString, derived=False, changeable=True)
    maintainer = EAttribute(eType=EString, derived=False, changeable=True)
    email = EAttribute(eType=EString, derived=False, changeable=True)
    builtin = EAttribute(eType=EBoolean, derived=False, changeable=True, default_value=False)
    description = EAttribute(eType=EString, derived=False, changeable=True)
    hasDependencies = EReference(ordered=True, unique=True, containment=True, upper=-1)
    hasNodes = EReference(ordered=True, unique=True, containment=True, upper=-1)
    hasDocumentation = EReference(ordered=True, unique=True, containment=True)
    hasTopicMessages = EReference(ordered=True, unique=True, containment=True, upper=-1)
    hasServiceMessages = EReference(ordered=True, unique=True, containment=True, upper=-1)
    hasActionInterfaces = EReference(ordered=True, unique=True, containment=True, upper=-1)
    hasDeployments = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, hasDependencies=None, hasNodes=None, hasDocumentation=None, name=None, rosVersion=None, packagePath=None, hasTopicMessages=None, hasServiceMessages=None, hasActionInterfaces=None, license=None, maintainer=None, email=None, builtin=None, description=None, hasDeployments=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if rosVersion:
            self.rosVersion.extend(rosVersion)

        if packagePath is not None:
            self.packagePath = packagePath

        if license is not None:
            self.license = license

        if maintainer is not None:
            self.maintainer = maintainer

        if email is not None:
            self.email = email

        if builtin is not None:
            self.builtin = builtin

        if description is not None:
            self.description = description

        if hasDependencies:
            self.hasDependencies.extend(hasDependencies)

        if hasNodes:
            self.hasNodes.extend(hasNodes)

        if hasDocumentation is not None:
            self.hasDocumentation = hasDocumentation

        if hasTopicMessages:
            self.hasTopicMessages.extend(hasTopicMessages)

        if hasServiceMessages:
            self.hasServiceMessages.extend(hasServiceMessages)

        if hasActionInterfaces:
            self.hasActionInterfaces.extend(hasActionInterfaces)

        if hasDeployments:
            self.hasDeployments.extend(hasDeployments)


class Software(EObject, metaclass=MetaEClass):

    hasPackages = EReference(ordered=True, unique=True, containment=True, upper=-1)
    hasQosProfiles = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, hasPackages=None, hasQosProfiles=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if hasPackages:
            self.hasPackages.extend(hasPackages)

        if hasQosProfiles:
            self.hasQosProfiles.extend(hasQosProfiles)


@abstract
class QosProfile(EObject, metaclass=MetaEClass):

    def __init__(self, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


class Graph(EObject, metaclass=MetaEClass):

    hasTopics = EReference(ordered=True, unique=True, containment=True, upper=-1)
    hasServiceLinks = EReference(ordered=True, unique=True, containment=True, upper=-1)
    nodes = EReference(ordered=True, unique=True, containment=False, upper=-1)
    hasActionLinks = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, hasTopics=None, hasServiceLinks=None, nodes=None, hasActionLinks=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if hasTopics:
            self.hasTopics.extend(hasTopics)

        if hasServiceLinks:
            self.hasServiceLinks.extend(hasServiceLinks)

        if nodes:
            self.nodes.extend(nodes)

        if hasActionLinks:
            self.hasActionLinks.extend(hasActionLinks)


class ActionLink(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    actionserver = EReference(ordered=True, unique=True, containment=False)
    actionclient = EReference(ordered=True, unique=True, containment=False, upper=-1)

    def __init__(self, *, name=None, actionserver=None, actionclient=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if actionserver is not None:
            self.actionserver = actionserver

        if actionclient:
            self.actionclient.extend(actionclient)


class Topic(EObject, metaclass=MetaEClass):

    topicPath = EAttribute(eType=EString, derived=False, changeable=True)
    publisher = EReference(ordered=True, unique=True, containment=False)
    subscriber = EReference(ordered=True, unique=True, containment=False, upper=-1)

    def __init__(self, *, publisher=None, subscriber=None, topicPath=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if topicPath is not None:
            self.topicPath = topicPath

        if publisher is not None:
            self.publisher = publisher

        if subscriber:
            self.subscriber.extend(subscriber)


class ServiceLink(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    server = EReference(ordered=True, unique=True, containment=False)
    client = EReference(ordered=True, unique=True, containment=False, upper=-1)

    def __init__(self, *, server=None, client=None, name=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if server is not None:
            self.server = server

        if client:
            self.client.extend(client)


class SystemGraph(EObject, metaclass=MetaEClass):

    graph = EReference(ordered=True, unique=True, containment=True)
    packagegraph = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, graph=None, packagegraph=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if graph is not None:
            self.graph = graph

        if packagegraph is not None:
            self.packagegraph = packagegraph


@abstract
class TopicMessage(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)

    def __init__(self, *, name=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name


@abstract
class ServiceMessage(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)

    def __init__(self, *, name=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name


@abstract
class ActionInterface(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)

    def __init__(self, *, name=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name


class Goal(EObject, metaclass=MetaEClass):

    hasObjectProperties = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, hasObjectProperties=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if hasObjectProperties:
            self.hasObjectProperties.extend(hasObjectProperties)


class Result(EObject, metaclass=MetaEClass):

    hasObjectProperties = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, hasObjectProperties=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if hasObjectProperties:
            self.hasObjectProperties.extend(hasObjectProperties)


class Feedback(EObject, metaclass=MetaEClass):

    hasObjectProperties = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, hasObjectProperties=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if hasObjectProperties:
            self.hasObjectProperties.extend(hasObjectProperties)


class Request(EObject, metaclass=MetaEClass):

    hasObjectProperties = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, hasObjectProperties=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if hasObjectProperties:
            self.hasObjectProperties.extend(hasObjectProperties)


class Response(EObject, metaclass=MetaEClass):

    hasObjectProperties = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, hasObjectProperties=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if hasObjectProperties:
            self.hasObjectProperties.extend(hasObjectProperties)


class ActionServer(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    actioninterface = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, name=None, actioninterface=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if actioninterface is not None:
            self.actioninterface = actioninterface


class ActionClient(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    actioninterface = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, name=None, actioninterface=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if actioninterface is not None:
            self.actioninterface = actioninterface


@abstract
class Dependency(EObject, metaclass=MetaEClass):

    def __init__(self, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


class Documentation(EObject, metaclass=MetaEClass):

    def __init__(self, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


class Client(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    servicePath = EAttribute(eType=EString, derived=False, changeable=True)
    serviceName = EAttribute(eType=EString, derived=False, changeable=True)
    servicemessage = EReference(ordered=True, unique=True, containment=False)
    qosprofile = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, name=None, servicePath=None, serviceName=None, servicemessage=None, qosprofile=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if servicePath is not None:
            self.servicePath = servicePath

        if serviceName is not None:
            self.serviceName = serviceName

        if servicemessage is not None:
            self.servicemessage = servicemessage

        if qosprofile is not None:
            self.qosprofile = qosprofile


class Node(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    namespace = EAttribute(eType=EString, derived=False, changeable=True)
    hasSubscribers = EReference(ordered=True, unique=True, containment=True, upper=-1)
    hasPublishers = EReference(ordered=True, unique=True, containment=True, upper=-1)
    hasClients = EReference(ordered=True, unique=True, containment=True, upper=-1)
    hasServers = EReference(ordered=True, unique=True, containment=True, upper=-1)
    hasParameters = EReference(ordered=True, unique=True, containment=True, upper=-1)
    hasActionServers = EReference(ordered=True, unique=True, containment=True, upper=-1)
    hasActionClients = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, hasSubscribers=None, hasPublishers=None, hasClients=None, hasServers=None, hasParameters=None, name=None, namespace=None, hasActionServers=None, hasActionClients=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if namespace is not None:
            self.namespace = namespace

        if hasSubscribers:
            self.hasSubscribers.extend(hasSubscribers)

        if hasPublishers:
            self.hasPublishers.extend(hasPublishers)

        if hasClients:
            self.hasClients.extend(hasClients)

        if hasServers:
            self.hasServers.extend(hasServers)

        if hasParameters:
            self.hasParameters.extend(hasParameters)

        if hasActionServers:
            self.hasActionServers.extend(hasActionServers)

        if hasActionClients:
            self.hasActionClients.extend(hasActionClients)


class Subscriber(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    topicPath = EAttribute(eType=EString, derived=False, changeable=True)
    smsg = EReference(ordered=True, unique=True, containment=False)
    qosprofile = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, name=None, topicPath=None, smsg=None, qosprofile=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if topicPath is not None:
            self.topicPath = topicPath

        if smsg is not None:
            self.smsg = smsg

        if qosprofile is not None:
            self.qosprofile = qosprofile


class Publisher(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    topicPath = EAttribute(eType=EString, derived=False, changeable=True)
    publishRate = EAttribute(eType=EFloat, derived=False, changeable=True, default_value=0.5)
    pmsg = EReference(ordered=True, unique=True, containment=False)
    qosprofile = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, name=None, topicPath=None, publishRate=None, pmsg=None, qosprofile=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if topicPath is not None:
            self.topicPath = topicPath

        if publishRate is not None:
            self.publishRate = publishRate

        if pmsg is not None:
            self.pmsg = pmsg

        if qosprofile is not None:
            self.qosprofile = qosprofile


class Server(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    servicePath = EAttribute(eType=EString, derived=False, changeable=True)
    serviceName = EAttribute(eType=EString, derived=False, changeable=True)
    servicemessage = EReference(ordered=True, unique=True, containment=False)
    qosprofile = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, name=None, servicePath=None, serviceName=None, servicemessage=None, qosprofile=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if servicePath is not None:
            self.servicePath = servicePath

        if serviceName is not None:
            self.serviceName = serviceName

        if servicemessage is not None:
            self.servicemessage = servicemessage

        if qosprofile is not None:
            self.qosprofile = qosprofile


class Parameter(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    type = EAttribute(eType=DataTypes, derived=False, changeable=True, default_value=None)
    value = EAttribute(eType=EString, derived=False, changeable=True)
    description = EAttribute(eType=EString, derived=False, changeable=True)

    def __init__(self, *, name=None, type=None, value=None, description=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if type is not None:
            self.type = type

        if value is not None:
            self.value = value

        if description is not None:
            self.description = description


class ObjectProperty(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    description = EAttribute(eType=EString, derived=False, changeable=True)
    constant = EAttribute(eType=EBoolean, derived=False, changeable=True, default_value=False)
    default = EAttribute(eType=EString, derived=False, changeable=True)
    datatype = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, name=None, description=None, datatype=None, constant=None, default=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if constant is not None:
            self.constant = constant

        if default is not None:
            self.default = default

        if datatype is not None:
            self.datatype = datatype


@abstract
class Datatype(EObject, metaclass=MetaEClass):

    def __init__(self, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


class PackageGraph(EObject, metaclass=MetaEClass):

    package = EReference(ordered=True, unique=True, containment=False, upper=-1)

    def __init__(self, *, package=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if package:
            self.package.extend(package)


class Deployment(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    arguments = EAttribute(eType=EString, derived=False, changeable=True, upper=-1)
    nodes = EReference(ordered=True, unique=True, containment=False, upper=-1)
    host = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, nodes=None, host=None, name=None, arguments=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if arguments:
            self.arguments.extend(arguments)

        if nodes:
            self.nodes.extend(nodes)

        if host is not None:
            self.host = host


class Platform(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    hasHost = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, hasHost=None, name=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if hasHost:
            self.hasHost.extend(hasHost)


class LocalNetwork(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    ip = EAttribute(eType=EString, derived=False, changeable=True)
    subnetMask = EAttribute(eType=EString, derived=False, changeable=True)
    gateway = EAttribute(eType=EString, derived=False, changeable=True)

    def __init__(self, *, name=None, ip=None, subnetMask=None, gateway=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if ip is not None:
            self.ip = ip

        if subnetMask is not None:
            self.subnetMask = subnetMask

        if gateway is not None:
            self.gateway = gateway


class Host(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    architecture = EAttribute(eType=AritectureTypes, derived=False, changeable=True)
    OS = EAttribute(eType=OSType, derived=False, changeable=True)
    hardDisk = EAttribute(eType=EFloat, derived=False, changeable=True)
    memory = EAttribute(eType=EFloat, derived=False, changeable=True)
    rosVersion = EAttribute(eType=ROSVersion, derived=False, changeable=True)
    hasNetworkInterfaces = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, name=None, architecture=None, OS=None, hardDisk=None, memory=None, rosVersion=None, hasNetworkInterfaces=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if architecture is not None:
            self.architecture = architecture

        if OS is not None:
            self.OS = OS

        if hardDisk is not None:
            self.hardDisk = hardDisk

        if memory is not None:
            self.memory = memory

        if rosVersion is not None:
            self.rosVersion = rosVersion

        if hasNetworkInterfaces:
            self.hasNetworkInterfaces.extend(hasNetworkInterfaces)


class NetworkInterface(EObject, metaclass=MetaEClass):

    gateway = EAttribute(eType=EString, derived=False, changeable=True)
    subnetMask = EAttribute(eType=EString, derived=False, changeable=True)
    name = EAttribute(eType=EString, derived=False, changeable=True)
    ip = EAttribute(eType=EString, derived=False, changeable=True)

    def __init__(self, *, gateway=None, subnetMask=None, name=None, ip=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if gateway is not None:
            self.gateway = gateway

        if subnetMask is not None:
            self.subnetMask = subnetMask

        if name is not None:
            self.name = name

        if ip is not None:
            self.ip = ip


class CustomQosProfile(QosProfile):

    history = EAttribute(eType=QosHistory, derived=False, changeable=True)
    depth = EAttribute(eType=EInt, derived=False, changeable=True, default_value=0)
    reliability = EAttribute(eType=QosReliability, derived=False, changeable=True)
    durability = EAttribute(eType=QosDurability, derived=False, changeable=True)
    liveliness = EAttribute(eType=QosLiveliness, derived=False, changeable=True)
    deadlineSec = EAttribute(eType=EInt, derived=False, changeable=True, default_value=0)
    deadlineNSec = EAttribute(eType=EInt, derived=False, changeable=True, default_value=0)
    lifespanSec = EAttribute(eType=EInt, derived=False, changeable=True, default_value=0)
    lifespanNSec = EAttribute(eType=EInt, derived=False, changeable=True, default_value=0)
    liveliness_lease_durationSec = EAttribute(
        eType=EInt, derived=False, changeable=True, default_value=0)
    liveliness_lease_durationNSec = EAttribute(
        eType=EInt, derived=False, changeable=True, default_value=0)
    avoid_ros_namespace_conventions = EAttribute(eType=EBoolean, derived=False, changeable=True)

    def __init__(self, *, history=None, depth=None, reliability=None, durability=None, liveliness=None, deadlineSec=None, deadlineNSec=None, lifespanSec=None, lifespanNSec=None, liveliness_lease_durationSec=None, liveliness_lease_durationNSec=None, avoid_ros_namespace_conventions=None, **kwargs):

        super().__init__(**kwargs)

        if history is not None:
            self.history = history

        if depth is not None:
            self.depth = depth

        if reliability is not None:
            self.reliability = reliability

        if durability is not None:
            self.durability = durability

        if liveliness is not None:
            self.liveliness = liveliness

        if deadlineSec is not None:
            self.deadlineSec = deadlineSec

        if deadlineNSec is not None:
            self.deadlineNSec = deadlineNSec

        if lifespanSec is not None:
            self.lifespanSec = lifespanSec

        if lifespanNSec is not None:
            self.lifespanNSec = lifespanNSec

        if liveliness_lease_durationSec is not None:
            self.liveliness_lease_durationSec = liveliness_lease_durationSec

        if liveliness_lease_durationNSec is not None:
            self.liveliness_lease_durationNSec = liveliness_lease_durationNSec

        if avoid_ros_namespace_conventions is not None:
            self.avoid_ros_namespace_conventions = avoid_ros_namespace_conventions


class RosQosProfile(QosProfile):

    name = EAttribute(eType=QosPresetProfiles, derived=False, changeable=True)

    def __init__(self, *, name=None, **kwargs):

        super().__init__(**kwargs)

        if name is not None:
            self.name = name


class CustomPackage(Package):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class RosPackage(Package):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class PackageDependency(Dependency):

    package = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, package=None, **kwargs):

        super().__init__(**kwargs)

        if package is not None:
            self.package = package


class RosMessage(TopicMessage):

    package = EAttribute(eType=EString, derived=False, changeable=True)

    def __init__(self, *, package=None, **kwargs):

        super().__init__(**kwargs)

        if package is not None:
            self.package = package


class RosService(ServiceMessage):

    package = EAttribute(eType=EString, derived=False, changeable=True)

    def __init__(self, *, package=None, **kwargs):

        super().__init__(**kwargs)

        if package is not None:
            self.package = package


class CustomActionInterface(ActionInterface):

    description = EAttribute(eType=EString, derived=False, changeable=True)
    hasGoal = EReference(ordered=True, unique=True, containment=True)
    hasResult = EReference(ordered=True, unique=True, containment=True)
    hasFeedback = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, description=None, hasGoal=None, hasResult=None, hasFeedback=None, **kwargs):

        super().__init__(**kwargs)

        if description is not None:
            self.description = description

        if hasGoal is not None:
            self.hasGoal = hasGoal

        if hasResult is not None:
            self.hasResult = hasResult

        if hasFeedback is not None:
            self.hasFeedback = hasFeedback


class CustomService(ServiceMessage):

    description = EAttribute(eType=EString, derived=False, changeable=True)
    hasRequest = EReference(ordered=True, unique=True, containment=True)
    hasResponse = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, hasRequest=None, hasResponse=None, description=None, **kwargs):

        super().__init__(**kwargs)

        if description is not None:
            self.description = description

        if hasRequest is not None:
            self.hasRequest = hasRequest

        if hasResponse is not None:
            self.hasResponse = hasResponse


class CustomMessage(TopicMessage):

    description = EAttribute(eType=EString, derived=False, changeable=True)
    hasObjectProperties = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, description=None, hasObjectProperties=None, **kwargs):

        super().__init__(**kwargs)

        if description is not None:
            self.description = description

        if hasObjectProperties:
            self.hasObjectProperties.extend(hasObjectProperties)


class Bool(Datatype):

    type = EAttribute(eType=EString, derived=False, changeable=True, default_value='"bool"')

    def __init__(self, *, type=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type


class String(Datatype):

    type = EAttribute(eType=EString, derived=False, changeable=True, default_value='"string"')

    def __init__(self, *, type=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type


@abstract
class Number(Datatype):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class ROSData(Datatype):

    type = EAttribute(eType=EString, derived=False, changeable=True)
    package = EAttribute(eType=EString, derived=False, changeable=True)

    def __init__(self, *, type=None, package=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type

        if package is not None:
            self.package = package


@abstract
class Array(Datatype):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Int(Number):

    type = EAttribute(eType=IntType, derived=False, changeable=True, default_value=None)

    def __init__(self, *, type=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type


class Uint(Number):

    type = EAttribute(eType=UIntType, derived=False, changeable=True, default_value=None)

    def __init__(self, *, type=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type


class Float(Number):

    type = EAttribute(eType=FloatType, derived=False, changeable=True, default_value=None)

    def __init__(self, *, type=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type


class UintArray(Array):

    type = EAttribute(eType=UIntArrayType, derived=False, changeable=True, default_value=None)

    def __init__(self, *, type=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type


class FloatArray(Array):

    type = EAttribute(eType=FloatArrayType, derived=False, changeable=True, default_value=None)

    def __init__(self, *, type=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type


class IntArray(Array):

    type = EAttribute(eType=IntArrayType, derived=False, changeable=True, default_value=None)

    def __init__(self, *, type=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type
