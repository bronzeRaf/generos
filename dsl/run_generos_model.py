from pyecore.resources import ResourceSet, URI, global_registry
from pyecore.resources.json import JsonResource
from pyecore.ecore import EClass, EAttribute, EObject
import pyecore.ecore as Ecore  # We get a reference to the Ecore metamodle implem.
from pyecoregen.ecore import EcoreGenerator 
import pyecore.behavior as behavior
from pyecore.utils import DynamicEPackage
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../metamodelLib'))
# ~ import metamodel
import metageneros
from textx import metamodel_from_file
from textx.export import metamodel_export, model_export
import textx.scoping.providers as scoping_providers
from textx import get_children, get_children_of_type

 
class RosSystem(object):
	def __init__(self):
		#init
		self.rosystem = metageneros.ROSSystem(name = "My_dsl_ROS_system")
		self.rosystem.hasSoftware = metageneros.Software()
		self.rosystem.hasSystemGraph = metageneros.SystemGraph()
		self.rosystem.hasTopology = metageneros.Topology()
		self.platform = metageneros.Platform(name="workspace_platform")
		self.rosystem.hasTopology.hasPlatforms.extend([self.platform])
	
	def interpret(self, model):
		# Initialize
		package_bag = {}
		dependencies_bag = {}
		messages_bag = {}
		services_bag = {}
		actions_bag = {}
		topics_bag = {}
		servicelinks_bag = {}
		actionlinks_bag = {}
		hosts_bag = {}
		networkinterfaces_bag = {}
		deployments_bag = {}
		nodes_bag = {}
		builtins = []
		topics = []
		servicelinks = []
		actionlinks = []
		# Create Interfaces package
		package_bag['interfaces'] = metageneros.CustomPackage(name = "interfaces", rosVersion = 0, packagePath = "")
		self.rosystem.hasSoftware.hasPackages.extend([package_bag['interfaces']])
		# Create Graphs
		graph = metageneros.Graph()
		self.rosystem.hasSystemGraph.graph = graph
		packagegraph = metageneros.PackageGraph()
		self.rosystem.hasSystemGraph.packagegraph = packagegraph
		# Add Interfaces into the package graph
		packagegraph.package.extend([package_bag['interfaces']])
		# Create custom and ros interfaces
		for p in model.commands:
			if p.__class__.__name__ == "CustomMessage":
				# Custom Messages
				messages_bag[p.name] = metageneros.CustomMessage(name=p.name, description = p.description)
				package_bag['interfaces'].hasTopicMessages.extend([messages_bag[p.name]])
				for o in p.hasObjects:
					tempobj = metageneros.ObjectProperty(name=o.name, description = o.description, constant = o.constant, default = o.default)
					messages_bag[p.name].hasObjectProperties.extend([tempobj])
					# Create object based on its type
					if o.type.startswith('int'):
						exec("tempobj.datatype = metageneros.Int(type = metageneros.IntType."+o.type+")")
					elif o.type.startswith('uint'):
						exec("tempobj.datatype = metageneros.Uint(type = metageneros.UIntType."+o.type+")")
					elif o.type.startswith('float'):
						exec("tempobj.datatype = metageneros.Float(type = metageneros.FloatType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metageneros.IntArray(type = metageneros.IntArrayType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metageneros.UintArray(type = metageneros.UIntArrayType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metageneros.FloatArray(type = metageneros.FloatArrayType."+o.type+")")
					elif o.type.startswith('bool'):
						tempobj.datatype = metageneros.Bool(type = "bool")
					elif o.type.startswith('string'):
						tempobj.datatype = metageneros.String(type = "string")
					elif o.__class__.__name__ == "ROSData":
						tempobj.datatype = metageneros.ROSData(type = o.type, package = o.package)
			# Ros Messages
			elif p.__class__.__name__ == "RosMessage":
				messages_bag[p.name] = metageneros.RosMessage(name=p.name, package = p.package)
				if p.package not in builtins:
					builtins.append(p.package)
					package_bag[p.package] = metageneros.RosPackage(name = p.package, rosVersion = 0, packagePath = "", builtin = True)
					self.rosystem.hasSoftware.hasPackages.extend([package_bag[p.package]])
				package_bag[p.package].hasTopicMessages.extend([messages_bag[p.name]])
			# Custom Services
			elif p.__class__.__name__ == "CustomServiceMessage":
				# Custom message
				services_bag[p.name] = metageneros.CustomService(name=p.name, description = p.description)
				package_bag['interfaces'].hasServiceMessages.extend([services_bag[p.name]])
				services_bag[p.name].hasRequest = metageneros.Request()
				services_bag[p.name].hasResponse = metageneros.Response()
				# Build the request of the service
				for o in p.request.hasObjects:
					tempobj = metageneros.ObjectProperty(name=o.name, description = o.description, constant = o.constant, default = o.default)
					services_bag[p.name].hasRequest.hasObjectProperties.extend([tempobj])
					# Create object based on its type
					if o.type.startswith('int'):
						exec("tempobj.datatype = metageneros.Int(type = metageneros.IntType."+o.type+")")
					elif o.type.startswith('uint'):
						exec("tempobj.datatype = metageneros.Uint(type = metageneros.UIntType."+o.type+")")
					elif o.type.startswith('float'):
						exec("tempobj.datatype = metageneros.Float(type = metageneros.FloatType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metageneros.IntArray(type = metageneros.IntArrayType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metageneros.UintArray(type = metageneros.UIntArrayType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metageneros.FloatArray(type = metageneros.FloatArrayType."+o.type+")")
					elif o.type.startswith('bool'):
						tempobj.datatype = metageneros.Bool(type = "bool")
					elif o.type.startswith('string'):
						tempobj.datatype = metageneros.String(type = "string")
					elif o.__class__.__name__ == "ROSData":
						tempobj.datatype = metageneros.ROSData(type = o.type, package = o.package)
				# Build the response of the service
				for o in p.response.hasObjects:
					tempobj = metageneros.ObjectProperty(name=o.name, description = o.description, constant = o.constant, default = o.default)
					services_bag[p.name].hasResponse.hasObjectProperties.extend([tempobj])
					# Create object based on its type
					if o.type.startswith('int'):
						exec("tempobj.datatype = metageneros.Int(type = metageneros.IntType."+o.type+")")
					elif o.type.startswith('uint'):
						exec("tempobj.datatype = metageneros.Uint(type = metageneros.UIntType."+o.type+")")
					elif o.type.startswith('float'):
						exec("tempobj.datatype = metageneros.Float(type = metageneros.FloatType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metageneros.IntArray(type = metageneros.IntArrayType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metageneros.UintArray(type = metageneros.UIntArrayType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metageneros.FloatArray(type = metageneros.FloatArrayType."+o.type+")")
					elif o.type.startswith('bool'):
						tempobj.datatype = metageneros.Bool(type = "bool")
					elif o.type.startswith('string'):
						tempobj.datatype = metageneros.String(type = "string")
					elif o.__class__.__name__ == "ROSData":
						tempobj.datatype = metageneros.ROSData(type = o.type, package = o.package)
			# Ros Services
			elif p.__class__.__name__ == "RosServiceMessage":
				services_bag[p.name] = metageneros.RosService(name=p.name, package = p.package)
				if p.package not in builtins:
					builtins.append(p.package)
					package_bag[p.package] = metageneros.RosPackage(name = p.package, rosVersion = 0, packagePath = "", builtin = True)
					self.rosystem.hasSoftware.hasPackages.extend([package_bag[p.package]])
				package_bag[p.package].hasServiceMessages.extend([services_bag[p.name]])
			# Custom Action Interface
			elif p.__class__.__name__ == "CustomActionInterface":
				# Custom Action Interfaces
				actions_bag[p.name] = metageneros.CustomActionInterface(name=p.name, description = p.description)
				package_bag['interfaces'].hasActionInterfaces.extend([actions_bag[p.name]])
				actions_bag[p.name].hasGoal = metageneros.Goal()
				actions_bag[p.name].hasResult = metageneros.Result()
				actions_bag[p.name].hasFeedback = metageneros.Feedback()
				# Build the goal of the action
				for o in p.goal.hasObjects:
					tempobj = metageneros.ObjectProperty(name=o.name, description = o.description, constant = o.constant, default = o.default)
					actions_bag[p.name].hasGoal.hasObjectProperties.extend([tempobj])
					# Create object based on its type
					if o.type.startswith('int'):
						exec("tempobj.datatype = metageneros.Int(type = metageneros.IntType."+o.type+")")
					elif o.type.startswith('uint'):
						exec("tempobj.datatype = metageneros.Uint(type = metageneros.UIntType."+o.type+")")
					elif o.type.startswith('float'):
						exec("tempobj.datatype = metageneros.Float(type = metageneros.FloatType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metageneros.IntArray(type = metageneros.IntArrayType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metageneros.UintArray(type = metageneros.UIntArrayType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metageneros.FloatArray(type = metageneros.FloatArrayType."+o.type+")")
					elif o.type.startswith('bool'):
						tempobj.datatype = metageneros.Bool(type = "bool")
					elif o.type.startswith('string'):
						tempobj.datatype = metageneros.String(type = "string")
					elif o.__class__.__name__ == "ROSData":
						tempobj.datatype = metageneros.ROSData(type = o.type, package = o.package)
				# Build the result of the action
				for o in p.result.hasObjects:
					tempobj = metageneros.ObjectProperty(name=o.name, description = o.description, constant = o.constant, default = o.default)
					actions_bag[p.name].hasResult.hasObjectProperties.extend([tempobj])
					# Create object based on its type
					if o.type.startswith('int'):
						exec("tempobj.datatype = metageneros.Int(type = metageneros.IntType."+o.type+")")
					elif o.type.startswith('uint'):
						exec("tempobj.datatype = metageneros.Uint(type = metageneros.UIntType."+o.type+")")
					elif o.type.startswith('float'):
						exec("tempobj.datatype = metageneros.Float(type = metageneros.FloatType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metageneros.IntArray(type = metageneros.IntArrayType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metageneros.UintArray(type = metageneros.UIntArrayType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metageneros.FloatArray(type = metageneros.FloatArrayType."+o.type+")")
					elif o.type.startswith('bool'):
						tempobj.datatype = metageneros.Bool(type = "bool")
					elif o.type.startswith('string'):
						tempobj.datatype = metageneros.String(type = "string")
					elif o.__class__.__name__ == "ROSData":
						tempobj.datatype = metageneros.ROSData(type = o.type, package = o.package)
				# Build the feeedback of the action
				for o in p.feedback.hasObjects:
					tempobj = metageneros.ObjectProperty(name=o.name, description = o.description, constant = o.constant, default = o.default)
					actions_bag[p.name].hasFeedback.hasObjectProperties.extend([tempobj])
					# Create object based on its type
					if o.type.startswith('int'):
						exec("tempobj.datatype = metageneros.Int(type = metageneros.IntType."+o.type+")")
					elif o.type.startswith('uint'):
						exec("tempobj.datatype = metageneros.Uint(type = metageneros.UIntType."+o.type+")")
					elif o.type.startswith('float'):
						exec("tempobj.datatype = metageneros.Float(type = metageneros.FloatType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metageneros.IntArray(type = metageneros.IntArrayType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metageneros.UintArray(type = metageneros.UIntArrayType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metageneros.FloatArray(type = metageneros.FloatArrayType."+o.type+")")
					elif o.type.startswith('bool'):
						tempobj.datatype = metageneros.Bool(type = "bool")
					elif o.type.startswith('string'):
						tempobj.datatype = metageneros.String(type = "string")
					elif o.__class__.__name__ == "ROSData":
						tempobj.datatype = metageneros.ROSData(type = o.type, package = o.package)
						
		
						
		# Create custom and ros QoS profiles
		qos_bag = {}
		for p in model.commands:
			# Custom QoS Profile
			if p.__class__.__name__ == "CustomQosProfile":
				# Add default settings
				if p.history=='':
					p.history = "SYSTEM_DEFAULT"
				if p.reliability=='':
					p.reliability = "SYSTEM_DEFAULT"
				if p.durability=='':
					p.durability = "SYSTEM_DEFAULT"
				if p.livelines=='':
					p.livelines = "SYSTEM_DEFAULT"
				# Create the profile
				exec('qos_bag["'+str(p.name)+'"] = metageneros.CustomQosProfile(history=metageneros.QosHistory.'+p.history+', depth='+str(p.depth)+', reliability=metageneros.QosReliability.'+p.reliability+
					', durability=metageneros.QosDurability.'+p.durability+', liveliness=metageneros.QosLiveliness.'+p.livelines+', deadlineSec='+str(p.deadlineSec)+', deadlineNSec = '+ 
					str(p.deadlineNSec)+', lifespanSec='+str(p.lifespanSec)+', lifespanNSec ='+str(p.lifespanNSec)+', liveliness_lease_durationSec='+str(p.liveliness_lease_durationSec)+
					', liveliness_lease_durationNSec='+str(p.liveliness_lease_durationNSec)+', avoid_ros_namespace_conventions='+str(p.avoid_ros_namespace_conventions)+')')
				self.rosystem.hasSoftware.hasQosProfiles.extend([qos_bag[p.name]])
			# Ros QoS Profile
			elif p.__class__.__name__ == "RosQosProfile":
				exec('qos_bag["'+str(p.name)+'"] = metageneros.RosQosProfile(name = metageneros.QosPresetProfiles.'+p.name+')')
				self.rosystem.hasSoftware.hasQosProfiles.extend([qos_bag[p.name]])
						
		#Create packages
		for p in model.commands:
			if p.__class__.__name__ == "CustomPackage" or p.__class__.__name__ == "RosPackage":
				#Package implementation
				if p.__class__.__name__ == "CustomPackage":
					package_bag[p.name] = metageneros.CustomPackage(name = p.name, builtin = p.builtin, license = p.license, maintainer = p.maintainer, email = p.email, description = p.description, packagePath = p.packagePath)
				else:
					package_bag[p.name] = metageneros.RosPackage(name = p.name, builtin = p.builtin, license = p.license, maintainer = p.maintainer, email = p.email, description = p.description, packagePath = p.packagePath)
				
				self.rosystem.hasSoftware.hasPackages.extend([package_bag[p.name]])
				packagegraph.package.extend([package_bag[p.name]])
				# Documentation implement
				package_bag[p.name].hasDocumentation = metageneros.Documentation()
				# Node implement
				node_bag = {}
				for n in p.hasNodes:
					node_bag[n.name] = metageneros.Node(name=n.name, namespace=n.namespace)
					nodes_bag[n.name] = node_bag[n.name]
					package_bag[p.name].hasNodes.extend([node_bag[n.name]])
					graph.nodes.extend([node_bag[n.name]])
					# Parameters implement
					parameter_bag = {}
					for pr in n.hasParameters:
						parameter_bag[pr.name] = metageneros.Parameter(name = pr.name,  value = pr.value, type=metageneros.DataTypes.INTEGER_ARRAY, description= pr.description)
						node_bag[n.name].hasParameters.extend([parameter_bag[pr.name]])
					# Subscriber implement
					subscriber_bag = {}
					for s in n.hasSubscribers:
						subscriber_bag[s.name] = metageneros.Subscriber(name = s.name,  topicPath = s.topicPath)
						node_bag[n.name].hasSubscribers.extend([subscriber_bag[s.name]])
						subscriber_bag[s.name].smsg = messages_bag[s.message.name]
						# Add dependencies
						depname = p.name+ messages_bag[s.message.name]._container.name
						if  depname not in dependencies_bag:
							dependencies_bag[depname] = metageneros.PackageDependency()
							package_bag[p.name].hasDependencies.extend([dependencies_bag[depname]])
							dependencies_bag[depname].package = package_bag[messages_bag[s.message.name]._container.name]
						# Create topic in graph
						if subscriber_bag[s.name].topicPath not in topics:
							topics.append(subscriber_bag[s.name].topicPath)
							topics_bag[subscriber_bag[s.name].topicPath] = metageneros.Topic(topicPath = subscriber_bag[s.name].topicPath)
							graph.hasTopics.extend([topics_bag[subscriber_bag[s.name].topicPath]])
						# Append subscriber to the graph
						topics_bag[subscriber_bag[s.name].topicPath].subscriber.extend([subscriber_bag[s.name]])
						# Add a QoS profile to the subscriber
						if s.qos is not None:
							subscriber_bag[s.name].qosprofile = qos_bag[s.qos.name]
					
					# Publisher implement
					publisher_bag = {}
					for s in n.hasPublishers:
						publisher_bag[s.name] = metageneros.Publisher(name = s.name,  topicPath = s.topicPath, publishRate = s.publishRate)
						node_bag[n.name].hasPublishers.extend([publisher_bag[s.name]])
						publisher_bag[s.name].pmsg = messages_bag[s.message.name]
						# Add dependencies
						depname = p.name+ messages_bag[s.message.name]._container.name
						if  depname not in dependencies_bag:
							dependencies_bag[depname] = metageneros.PackageDependency()
							package_bag[p.name].hasDependencies.extend([dependencies_bag[depname]])
							dependencies_bag[depname].package = package_bag[messages_bag[s.message.name]._container.name]
						# Create topic in graph
						if publisher_bag[s.name].topicPath not in topics:
							topics.append(publisher_bag[s.name].topicPath)
							topics_bag[publisher_bag[s.name].topicPath] = metageneros.Topic(topicPath = publisher_bag[s.name].topicPath)
							graph.hasTopics.extend([topics_bag[publisher_bag[s.name].topicPath]])
						# Append publisher to the graph
						topics_bag[publisher_bag[s.name].topicPath].publisher = publisher_bag[s.name]
						# Add a QoS profile to the publisher
						if s.qos is not None:
							publisher_bag[s.name].qosprofile = qos_bag[s.qos.name]
						
					# Server implement
					server_bag = {}
					for s in n.hasServers:
						server_bag[s.name] = metageneros.Server(name = s.name,  servicePath = s.servicePath, serviceName = s.serviceName)
						node_bag[n.name].hasServers.extend([server_bag[s.name]])
						server_bag[s.name].servicemessage = services_bag[s.service.name]
						# Add dependencies
						depname = p.name+ services_bag[s.service.name]._container.name
						if  depname not in dependencies_bag:
							dependencies_bag[depname] = metageneros.PackageDependency()
							package_bag[p.name].hasDependencies.extend([dependencies_bag[depname]])
							dependencies_bag[depname].package = package_bag[services_bag[s.service.name]._container.name]
						# Create service link in graph
						if server_bag[s.name].servicemessage.name not in servicelinks:
							servicelinks.append(server_bag[s.name].servicemessage.name)
							servicelinks_bag[server_bag[s.name].serviceName] = metageneros.ServiceLink(name = server_bag[s.name].serviceName)
							graph.hasServiceLinks.extend([servicelinks_bag[server_bag[s.name].serviceName]])
						# Append server to the graph
						servicelinks_bag[server_bag[s.name].serviceName].server = server_bag[s.name]
						# Add a QoS profile to the server
						if s.qos is not None:
							server_bag[s.name].qosprofile = qos_bag[s.qos.name]
						
					# Client implement
					client_bag = {}
					for s in n.hasClients:
						client_bag[s.name] = metageneros.Client(name = s.name,  servicePath = s.servicePath, serviceName = s.serviceName)
						node_bag[n.name].hasClients.extend([client_bag[s.name]])
						client_bag[s.name].servicemessage = services_bag[s.service.name]
						# Add dependencies
						depname = p.name+ services_bag[s.service.name]._container.name
						if  depname not in dependencies_bag:
							dependencies_bag[depname] = metageneros.PackageDependency()
							package_bag[p.name].hasDependencies.extend([dependencies_bag[depname]])
							dependencies_bag[depname].package = package_bag[services_bag[s.service.name]._container.name]
						# Create service link in graph
						if client_bag[s.name].servicemessage.name not in servicelinks:
							servicelinks.append(client_bag[s.name].servicemessage.name)
							servicelinks_bag[client_bag[s.name].serviceName] = metageneros.ServiceLink(name = client_bag[s.name].serviceName)
							graph.hasServiceLinks.extend([servicelinks_bag[client_bag[s.name].serviceName]])
						# Append client to the graph
						servicelinks_bag[client_bag[s.name].serviceName].client.extend([client_bag[s.name]])
						# Add a QoS profile to the client
						if s.qos is not None:
							client_bag[s.name].qosprofile = qos_bag[s.qos.name]
						
						
					# Action Server implement
					aserver_bag = {}
					for s in n.hasActionServers:
						aserver_bag[s.name] = metageneros.ActionServer(name = s.name)
						node_bag[n.name].hasActionServers.extend([aserver_bag[s.name]])
						aserver_bag[s.name].actioninterface = actions_bag[s.actioninterface.name]
						# Add dependencies
						depname = p.name+ actions_bag[s.actioninterface.name]._container.name
						if  depname not in dependencies_bag:
							dependencies_bag[depname] = metageneros.PackageDependency()
							package_bag[p.name].hasDependencies.extend([dependencies_bag[depname]])
							dependencies_bag[depname].package = package_bag[actions_bag[s.actioninterface.name]._container.name]
						# Create action link in graph
						if aserver_bag[s.name].actioninterface.name not in actionlinks:
							actionlinks.append(aserver_bag[s.name].actioninterface.name)
							actionlinks_bag[aserver_bag[s.name].actioninterface.name] = metageneros.ActionLink(name = aserver_bag[s.name].actioninterface.name)
							graph.hasActionLinks.extend([actionlinks_bag[aserver_bag[s.name].actioninterface.name]])
						# Append action server to the graph
						actionlinks_bag[aserver_bag[s.name].actioninterface.name].actionserver = aserver_bag[s.name]
						
					# Action Client implement
					aclient_bag = {}
					for s in n.hasActionClients:
						aclient_bag[s.name] = metageneros.ActionClient(name = s.name)
						node_bag[n.name].hasActionClients.extend([aclient_bag[s.name]])
						aclient_bag[s.name].actioninterface = actions_bag[s.actioninterface.name]
						# Add dependencies
						depname = p.name+ actions_bag[s.actioninterface.name]._container.name
						if  depname not in dependencies_bag:
							dependencies_bag[depname] = metageneros.PackageDependency()
							package_bag[p.name].hasDependencies.extend([dependencies_bag[depname]])
							dependencies_bag[depname].package = package_bag[actions_bag[s.actioninterface.name]._container.name]
						# Create service link in graph
						if aclient_bag[s.name].actioninterface.name not in actionlinks:
							actionlinks.append(aclient_bag[s.name].actioninterface.name)
							actionlinks_bag[aclient_bag[s.name].actioninterface.name] = metageneros.ActionLink(name = aclient_bag[s.name].actioninterface.name)
							graph.hasActionLinks.extend([actionlinks_bag[aclient_bag[s.name].actioninterface.name]])
						# Append action client to the graph
						actionlinks_bag[aclient_bag[s.name].actioninterface.name].actionclient.extend([aclient_bag[s.name]])
							
							
						
		# Second pass to all created packages
		for p in model.commands:
			if p.__class__.__name__ == "CustomPackage" or p.__class__.__name__ == "RosPackage":
				# Dependencies
				dependency_bag = {}
				for dep in p.hasDependencies:
					dependency_bag[dep.name] = metageneros.PackageDependency()
					package_bag[p.name].hasDependencies.extend([dependency_bag[dep.name]])
					dependency_bag[dep.name].package = package_bag[dep.package.name]
					
		# Build the Deployment part
		# Build Hosts
		for p in model.commands:
			if p.__class__.__name__ == "Host":
				# Hosts
				exec('hosts_bag["'+p.name+'"] = metageneros.Host(name ="'+p.name+'", architecture = metageneros.AritectureTypes.'+p.architecture+', OS = metageneros.OSType.'+p.OS+', hardDisk = '+str(p.hardDisk)+', memory = '+str(p.memory)+', rosVersion = metageneros.ROSVersion.'+p.rosVersion+')')
				self.platform.hasHost.extend([hosts_bag[p.name]])
				# Build the package for the Host
				packName = 'launch_'+p.name
				package_bag[packName] = metageneros.CustomPackage(name = packName, rosVersion = 0, packagePath = "")
				self.rosystem.hasSoftware.hasPackages.extend([package_bag[packName]])
				# Add dependencies
				for d in p.hasDependencies:
					depname = packName+d.package.name
					if  depname not in dependencies_bag:
						dependencies_bag[depname] = metageneros.PackageDependency()
						package_bag[packName].hasDependencies.extend([dependencies_bag[depname]])
						dependencies_bag[depname].package = package_bag[d.package.name]
				# Add Launchers into the package graph
				packagegraph.package.extend([package_bag[packName]])
				# Build Network Interfaces
				for n in p.hasNetworkInterfaces:
					networkinterfaces_bag[n.name] = metageneros.NetworkInterface(name = n.name, gateway = n.gateway, subnetMask = n.subnetMask, ip = n.ip)
					hosts_bag[p.name].hasNetworkInterfaces.extend([networkinterfaces_bag[n.name]])
				
					
		# Build Local Network
		for p in model.commands:
			if p.__class__.__name__ == "LocalNetwork":
				# Local Network
				self.rosystem.hasDeployment.topology.network = metageneros.LocalNetwork(name = p.name, gateway = p.gateway, subnetMask = p.subnetMask, ip = p.ip)
		
		
		# Build Deployments (Launch files)
		for p in model.commands:
			if p.__class__.__name__ == "Deployment":
				# Deployment file create
				deployments_bag[p.name] = metageneros.Deployment(name = p.name)
				# Attach to package
				package_bag['launch_'+p.host.name].hasDeployments.extend([deployments_bag[p.name]])
				# refer to host
				deployments_bag[p.name].host = hosts_bag[p.host.name]
				# Add nodes to the file
				for n in p.nodes:
					deployments_bag[p.name].nodes.append(nodes_bag[n.name])
					# Add dependencies
					depname = 'launch_'+p.host.name+nodes_bag[n.name]._container.name
					if  depname not in dependencies_bag:
						dependencies_bag[depname] = metageneros.PackageDependency()
						package_bag['launch_'+p.host.name].hasDependencies.extend([dependencies_bag[depname]])
						dependencies_bag[depname].package = package_bag[nodes_bag[n.name]._container.name]
		
		
def main(debug=False):
	# Go to working directory
	if str(os.path.dirname(__file__)) != '':
		os.chdir(str(os.path.dirname(__file__)))
	# Count arguments
	if len(sys.argv) < 2 or  len(sys.argv) > 3:
		print ('Please give at least an GRS file name (input model) and optionaly an XMI file name (output model)')
		sys.exit(0)
	# Obtain GRS model filename
	# ~ grs_filename = os.path.relpath(sys.argv[1], str(os.getcwd()))
	grs_filename = os.path.relpath(sys.argv[1], str(os.getcwd()))
	# Obtain XMI model filename
	if len(sys.argv) == 3:
		xmi_filename = sys.argv[2]
	else:
		xmi_filename = '../models/generos.xmi'	
	# Load Grammar
	dsl_metamodel = metamodel_from_file('generos.tx', debug=False)
	
	# Convert importURI string (if needed)
	def conv(i):
		return i.replace(".", "/") + ".grs"
	# Scope Providers
	dsl_metamodel.register_scope_providers({"*.*": scoping_providers.FQNImportURI(importAs=True)})
	
	
	# Recursive function that loads the commands of the imported models to the main model
	def resolve_imports(current_model):
		# Load imported models
		imports = get_children_of_type("Import", current_model)
		for i in imports:
			for m in i._tx_loaded_models:
				# Recursively attach commands of more deep imports
				m = resolve_imports(m)
				# Attach commands of the submodels (imports) to the main model
				current_model.commands.extend(m.commands)
		return current_model
	
	
	# Load Model
	model = dsl_metamodel.model_from_file(grs_filename)
	resolve_imports(model)
	
	# Fire up the generation
	system = RosSystem()
	system.interpret(model)
	#create rset
	global_registry[Ecore.nsURI] = Ecore  
	rset = ResourceSet()
	rset.metamodel_registry[metageneros.nsURI] = metageneros
	model_res = rset.create_resource(URI(xmi_filename))
	# Save
	model_res.append(system.rosystem)
	model_res.save()

if __name__ == "__main__":
	main()
