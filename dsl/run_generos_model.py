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
from textx import metamodel_from_file
from textx.export import metamodel_export, model_export

 
class RosSystem(object):
	def __init__(self):
		#init
		self.rosystem = metamodel.ROSSystem(name = "My_dsl_ROS_system")
	
	def interpret(self, model):
		# Initialize
		package_bag = {}
		messages_bag = {}
		services_bag = {}
		actions_bag = {}
		builtins = []
		# Create Interfaces package
		package_bag['interfaces'] = metamodel.Package(name = "interfaces", rosVersion = 0, packagePath = "")
		self.rosystem.hasPackages.extend([package_bag['interfaces']])
		# Create custom and ros interfaces
		for p in model.commands:
			if p.__class__.__name__ == "CustomMessage":
				# Custom Messages
				messages_bag[p.name] = metamodel.CustomMessage(name=p.name, description = p.description)
				package_bag['interfaces'].hasTopicMessages.extend([messages_bag[p.name]])
				for o in p.hasObjects:
					tempobj = metamodel.ObjectProperty(name=o.name, description = o.description, constant = o.constant, default = o.default)
					messages_bag[p.name].hasObjectProperties.extend([tempobj])
					# Create object based on its type
					if o.type.startswith('int'):
						exec("tempobj.datatype = metamodel.Int(type = metamodel.IntType."+o.type+")")
					elif o.type.startswith('uint'):
						exec("tempobj.datatype = metamodel.Uint(type = metamodel.UIntType."+o.type+")")
					elif o.type.startswith('float'):
						exec("tempobj.datatype = metamodel.Float(type = metamodel.FloatType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metamodel.IntArray(type = metamodel.IntArrayType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metamodel.UintArray(type = metamodel.UIntArrayType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metamodel.FloatArray(type = metamodel.FloatArrayType."+o.type+")")
					elif o.type.startswith('bool'):
						tempobj.datatype = metamodel.Bool(type = "bool")
					elif o.type.startswith('string'):
						tempobj.datatype = metamodel.String(type = "string")
					elif o.__class__.__name__ == "ROSData":
						tempobj.datatype = metamodel.ROSData(type = o.type, package = o.package)
			# Ros Messages
			elif p.__class__.__name__ == "RosMessage":
				messages_bag[p.name] = metamodel.RosMessage(name=p.name, package = p.package)
				if p.package not in builtins:
					builtins.append(p.package)
					package_bag[p.package] = metamodel.Package(name = p.package, rosVersion = 0, packagePath = "", builtin = True)
					self.rosystem.hasPackages.extend([package_bag[p.package]])
				package_bag[p.package].hasTopicMessages.extend([messages_bag[p.name]])
			# Custom Services
			elif p.__class__.__name__ == "CustomServiceMessage":
				# Custom message
				services_bag[p.name] = metamodel.CustomService(name=p.name, description = p.description)
				package_bag['interfaces'].hasServiceMessages.extend([services_bag[p.name]])
				services_bag[p.name].hasRequest = metamodel.Request()
				services_bag[p.name].hasResponse = metamodel.Response()
				# Build the request of the service
				for o in p.request.hasObjects:
					tempobj = metamodel.ObjectProperty(name=o.name, description = o.description, constant = o.constant, default = o.default)
					services_bag[p.name].hasRequest.hasObjectProperties.extend([tempobj])
					# Create object based on its type
					if o.type.startswith('int'):
						exec("tempobj.datatype = metamodel.Int(type = metamodel.IntType."+o.type+")")
					elif o.type.startswith('uint'):
						exec("tempobj.datatype = metamodel.Uint(type = metamodel.UIntType."+o.type+")")
					elif o.type.startswith('float'):
						exec("tempobj.datatype = metamodel.Float(type = metamodel.FloatType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metamodel.IntArray(type = metamodel.IntArrayType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metamodel.UintArray(type = metamodel.UIntArrayType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metamodel.FloatArray(type = metamodel.FloatArrayType."+o.type+")")
					elif o.type.startswith('bool'):
						tempobj.datatype = metamodel.Bool(type = "bool")
					elif o.type.startswith('string'):
						tempobj.datatype = metamodel.String(type = "string")
					elif o.__class__.__name__ == "ROSData":
						tempobj.datatype = metamodel.ROSData(type = o.type, package = o.package)
				# Build the response of the service
				for o in p.response.hasObjects:
					tempobj = metamodel.ObjectProperty(name=o.name, description = o.description, constant = o.constant, default = o.default)
					services_bag[p.name].hasResponse.hasObjectProperties.extend([tempobj])
					# Create object based on its type
					if o.type.startswith('int'):
						exec("tempobj.datatype = metamodel.Int(type = metamodel.IntType."+o.type+")")
					elif o.type.startswith('uint'):
						exec("tempobj.datatype = metamodel.Uint(type = metamodel.UIntType."+o.type+")")
					elif o.type.startswith('float'):
						exec("tempobj.datatype = metamodel.Float(type = metamodel.FloatType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metamodel.IntArray(type = metamodel.IntArrayType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metamodel.UintArray(type = metamodel.UIntArrayType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metamodel.FloatArray(type = metamodel.FloatArrayType."+o.type+")")
					elif o.type.startswith('bool'):
						tempobj.datatype = metamodel.Bool(type = "bool")
					elif o.type.startswith('string'):
						tempobj.datatype = metamodel.String(type = "string")
					elif o.__class__.__name__ == "ROSData":
						tempobj.datatype = metamodel.ROSData(type = o.type, package = o.package)
			# Ros Services
			elif p.__class__.__name__ == "RosServiceMessage":
				services_bag[p.name] = metamodel.RosService(name=p.name, package = p.package)
				if p.package not in builtins:
					builtins.append(p.package)
					package_bag[p.package] = metamodel.Package(name = p.package, rosVersion = 0, packagePath = "", builtin = True)
					self.rosystem.hasPackages.extend([package_bag[p.package]])
				package_bag[p.package].hasServiceMessages.extend([services_bag[p.name]])
			
			# Custom Action Interface
			elif p.__class__.__name__ == "CustomActionInterface":
				print("hi")
				# Custom Action Interfaces
				actions_bag[p.name] = metamodel.CustomActionInterface(name=p.name, description = p.description)
				package_bag['interfaces'].hasActionInterfaces.extend([actions_bag[p.name]])
				actions_bag[p.name].hasGoal = metamodel.Goal()
				actions_bag[p.name].hasResult = metamodel.Result()
				actions_bag[p.name].hasFeedback = metamodel.Feedback()
				# Build the goal of the action
				for o in p.goal.hasObjects:
					tempobj = metamodel.ObjectProperty(name=o.name, description = o.description, constant = o.constant, default = o.default)
					actions_bag[p.name].hasGoal.hasObjectProperties.extend([tempobj])
					# Create object based on its type
					if o.type.startswith('int'):
						exec("tempobj.datatype = metamodel.Int(type = metamodel.IntType."+o.type+")")
					elif o.type.startswith('uint'):
						exec("tempobj.datatype = metamodel.Uint(type = metamodel.UIntType."+o.type+")")
					elif o.type.startswith('float'):
						exec("tempobj.datatype = metamodel.Float(type = metamodel.FloatType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metamodel.IntArray(type = metamodel.IntArrayType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metamodel.UintArray(type = metamodel.UIntArrayType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metamodel.FloatArray(type = metamodel.FloatArrayType."+o.type+")")
					elif o.type.startswith('bool'):
						tempobj.datatype = metamodel.Bool(type = "bool")
					elif o.type.startswith('string'):
						tempobj.datatype = metamodel.String(type = "string")
					elif o.__class__.__name__ == "ROSData":
						tempobj.datatype = metamodel.ROSData(type = o.type, package = o.package)
				# Build the result of the action
				for o in p.result.hasObjects:
					tempobj = metamodel.ObjectProperty(name=o.name, description = o.description, constant = o.constant, default = o.default)
					actions_bag[p.name].hasResult.hasObjectProperties.extend([tempobj])
					# Create object based on its type
					if o.type.startswith('int'):
						exec("tempobj.datatype = metamodel.Int(type = metamodel.IntType."+o.type+")")
					elif o.type.startswith('uint'):
						exec("tempobj.datatype = metamodel.Uint(type = metamodel.UIntType."+o.type+")")
					elif o.type.startswith('float'):
						exec("tempobj.datatype = metamodel.Float(type = metamodel.FloatType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metamodel.IntArray(type = metamodel.IntArrayType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metamodel.UintArray(type = metamodel.UIntArrayType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metamodel.FloatArray(type = metamodel.FloatArrayType."+o.type+")")
					elif o.type.startswith('bool'):
						tempobj.datatype = metamodel.Bool(type = "bool")
					elif o.type.startswith('string'):
						tempobj.datatype = metamodel.String(type = "string")
					elif o.__class__.__name__ == "ROSData":
						tempobj.datatype = metamodel.ROSData(type = o.type, package = o.package)
				# Build the feeedback of the action
				for o in p.feedback.hasObjects:
					tempobj = metamodel.ObjectProperty(name=o.name, description = o.description, constant = o.constant, default = o.default)
					actions_bag[p.name].hasFeedback.hasObjectProperties.extend([tempobj])
					# Create object based on its type
					if o.type.startswith('int'):
						exec("tempobj.datatype = metamodel.Int(type = metamodel.IntType."+o.type+")")
					elif o.type.startswith('uint'):
						exec("tempobj.datatype = metamodel.Uint(type = metamodel.UIntType."+o.type+")")
					elif o.type.startswith('float'):
						exec("tempobj.datatype = metamodel.Float(type = metamodel.FloatType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metamodel.IntArray(type = metamodel.IntArrayType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metamodel.UintArray(type = metamodel.UIntArrayType."+o.type+")")
					elif o.type.startswith('int'):
						exec("tempobj.datatype = metamodel.FloatArray(type = metamodel.FloatArrayType."+o.type+")")
					elif o.type.startswith('bool'):
						tempobj.datatype = metamodel.Bool(type = "bool")
					elif o.type.startswith('string'):
						tempobj.datatype = metamodel.String(type = "string")
					elif o.__class__.__name__ == "ROSData":
						tempobj.datatype = metamodel.ROSData(type = o.type, package = o.package)
						
						
						
		
		
		for p in model.commands:
			if p.__class__.__name__ == "Package":
				package_bag[p.name] = metamodel.Package(name = p.name, builtin = p.builtin)
				self.rosystem.hasPackages.extend([package_bag[p.name]])
				# Documentation implement
				package_bag[p.name].hasDocumentation = metamodel.Documentation()
				# Node implement
				node_bag = {}
				for n in p.hasNodes:
					node_bag[n.name] = metamodel.Node(name=n.name, namespace=n.namespace)
					package_bag[p.name].hasNodes.extend([node_bag[n.name]])
					# Parameters implement
					parameter_bag = {}
					for pr in n.hasParameters:
						parameter_bag[pr.name] = metamodel.Parameter(name = pr.name,  value = pr.value, type=metamodel.DataTypes.INTEGER_ARRAY, description= pr.description)
						node_bag[n.name].hasParameters.extend([parameter_bag[pr.name]])
					# Subscriber implement
					subscriber_bag = {}
					for s in n.hasSubscribers:
						subscriber_bag[s.name] = metamodel.Subscriber(name = s.name,  topicPath = s.topicPath)
						node_bag[n.name].hasSubscribers.extend([subscriber_bag[s.name]])
						subscriber_bag[s.name].smsg = messages_bag[s.message.name]
					# Publisher implement
					publisher_bag = {}
					for s in n.hasPublishers:
						publisher_bag[s.name] = metamodel.Publisher(name = s.name,  topicPath = s.topicPath, publishRate = s.publishRate)
						node_bag[n.name].hasPublishers.extend([publisher_bag[s.name]])
						publisher_bag[s.name].pmsg = messages_bag[s.message.name]
							
							
						
		# Second pass to all created packages
		for p in model.commands:
			if p.__class__.__name__ == "Package":
				# Dependencies
				dependency_bag = {}
				for dep in p.hasDependencies:
					dependency_bag[dep.name] = metamodel.PackageDependency()
					package_bag[p.name].hasDependencies.extend([dependency_bag[dep.name]])
					dependency_bag[dep.name].package = package_bag[dep.package.name]
		
		
def main(debug=False):
	dsl_metamodel = metamodel_from_file('generos.tx', debug=False)
	model = dsl_metamodel.model_from_file('model.grs')
	system = RosSystem()
	system.interpret(model)
	#create rset
	global_registry[Ecore.nsURI] = Ecore  
	rset = ResourceSet()
	rset.metamodel_registry[metamodel.nsURI] = metamodel
	model_res = rset.create_resource(URI('../models/generos.xmi'))
	model_res.append(system.rosystem)
	model_res.save()

if __name__ == "__main__":
	main()
