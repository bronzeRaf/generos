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
		# Package implement
		package_bag = {}
		for p in model.packages:
			package_bag[p.name] = metamodel.Package(name = p.name, builtin = p.builtin)
			self.rosystem.hasPackages.extend([package_bag[p.name]])
			# Node implement
			node_bag = {}
			for n in p.hasNodes:
				node_bag[n.name] = metamodel.Node(name=n.name)
				package_bag[p.name].hasNodes.extend([node_bag[n.name]])
				# Parameters implement
				parameter_bag = {}
				for pr in n.hasParameters:
					parameter_bag[pr.name] = metamodel.Parameter(name = pr.name,  value = pr.value, type=metamodel.DataTypes.INTEGER_ARRAY, description= pr.description)
					node_bag[n.name].hasParameters.extend([parameter_bag[pr.name]])
		# Second pass to all created packages
		for p in model.packages:
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
