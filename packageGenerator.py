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
import subprocess
import os
import rclpy
from jinja2 import Environment, FileSystemLoader


# We load the Ecore metamodel first
global_registry[Ecore.nsURI] = Ecore  
rset = ResourceSet()
resource = rset.get_resource(URI('/home/raf/Desktop/Thesis Project/ecoreWork/metamodel.ecore'))
# ~ rset.resource_factory['json'] = lambda uri: JsonResource(uri)
root = resource.contents[0]  # We get the root (an EPackage here)
# Register the metamodel (in case we open an XMI model later)
rset.metamodel_registry[root.nsURI] = root



# We obtain the model from an XMI
model_root = rset.get_resource(URI('/home/raf/Desktop/Thesis Project/ecoreWork/test.xmi')).contents[0]

#Jinja2 Code
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

os.system('pwd')
os.system('ls')

template = env.get_template('packageTemplate.py')
package = {}
package['name'] = model_root.hasPackages[0].name
package['animal'] = 'dog'
 
output = template.render(data=package)
