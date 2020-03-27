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
import os



# We load the Ecore metamodel first
global_registry[Ecore.nsURI] = Ecore  
rset = ResourceSet()
resource = rset.get_resource(URI('metamodel.ecore'))
# ~ rset.resource_factory['json'] = lambda uri: JsonResource(uri)
root = resource.contents[0]  # We get the root (an EPackage here)
# Register the metamodel (in case we open an XMI model later)
rset.metamodel_registry[root.nsURI] = root





# ~ model_root.hasPackages[0].package_init()
# ~ for x in model_root.hasPackages[0].allInstances():
	# ~ print(x) # display 2 instances 
# ~ os.chdir('/home/raf/Desktop/Thesis Project/ecoreWork')
generator = EcoreGenerator()
generator.generate(root,'')
