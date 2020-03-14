# This File reads the metamodel, reads the model and renders the code
# to be generated to for the ROS2 package. Actually implements the 
# MDE transformation part, for model to code.
#
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

# Jinja2 Code
# Build the packages
for package in model_root.hasPackages:
	# Create the package directory
	os.system('mkdir '+package.name)
	
	# Generate Setup.py 
	# ___________________________________________
	# Load the Template of the Setup.py
	file_loader = FileSystemLoader('./templates')
	env = Environment(loader=file_loader,trim_blocks=True, lstrip_blocks=True)
	temp_setup = env.get_template('temp_setup.py')

	# Build the data to pass to the Template
	setup = {}
	setup['packageName'] = package.name
	setup['maintainer'] = 'raf'
	setup['email'] = 'rnm1816@gmail.com'
	setup['description'] = 'The description is ....'
	setup['license'] = 'The license is ...'
	entry = []
	entry.append('talker = py_pubsub.publisher_member_function:main'),
	entry.append('listener = py_pubsub.subscriber_member_function:main'),

	# Fire up the rendering proccess
	output = temp_setup.render(data=setup, entry_points=entry)

	# Write the generated file
	dest=package.name+'/setup.py'
	with open(dest, 'w') as f:
		f.write(output)

	# Give execution permissions to the generated python file
	os.chmod(dest, 509)

	# Generate package.xml 
	# ___________________________________________
	# Load the Template of the Setup.py
	file_loader = FileSystemLoader('./templates')
	env = Environment(loader=file_loader,trim_blocks=True, lstrip_blocks=True)
	temp_setup = env.get_template('temp_package.xml')
	
	# Fire up the rendering proccess
	output = temp_setup.render(data=setup)
	
	# Write the generated file
	dest=package.name+'/package.xml'
	with open(dest, 'w') as f:
		f.write(output)

	# Give execution permissions to the generated python file
	os.chmod(dest, 509)

