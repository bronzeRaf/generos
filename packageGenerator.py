# This File reads the metamodel, reads the model and renders the code
# to be generated to for the ROS2 package. Actually implements the 
# MDE transformation part, for model to code.
#
# Written in 14/2/2020
# Written by Rafael Brouzos
#
# After generating the code from the model go to the workspace root 
# (folder named "workspace") in terminal and run the comands:
# $ colcon build
# $ . install/setup.bash
# $ ros2 run <package_name> <node_name>_exec


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

# Create the workspace directory tree
os.system('mkdir workspace')
os.chdir('workspace')
os.system('mkdir src')
os.chdir('src')
# Build the packages
for package in model_root.hasPackages:
	# Create the package directory tree
	os.system('mkdir '+package.name)
	os.chdir(package.name)
	os.system('mkdir '+package.name)
	os.system('mkdir resource')
	os.chdir(package.name)
	os.system('touch __init__.py')
	os.chdir('../resource')
	os.system('touch '+package.name)
	os.chdir('../..')
	os.system('mkdir interfaces')
	os.chdir('interfaces')
	os.system('mkdir srv')
	os.system('mkdir msg')
	# Now the working directory is workspace/src/interfaces
	os.chdir('../'+package.name)
	# Now the working directory is workspace/src/package_name
	
	# Load the templates
	file_loader = FileSystemLoader('../../../templates')
	env = Environment(loader=file_loader,trim_blocks=True, lstrip_blocks=True)
	
	
	# Jinja2 Code
	# Generate Setup.py 
	# ___________________________________________
	# Load the Template of the setup.py
	template = env.get_template('temp_setup.py')

	# Build the package data to pass to the Template
	pack_data = {}
	pack_data['packageName'] = package.name
	pack_data['maintainer'] = 'raf'
	pack_data['email'] = 'rnm1816@gmail.com'
	pack_data['description'] = 'The description is ....'
	pack_data['license'] = 'The license is ...'
	# Build the entry points data to pass to the Template
	entry_data = []
	for n in package.hasNodes:
		entry_data.append(n.name+'_exec = '+package.name+'.'+n.name+'_node:main'),

	# Fire up the rendering proccess
	output = template.render(pack=pack_data, entry_points=entry_data)

	# Write the generated file
	dest='setup.py'
	with open(dest, 'w') as f:
		f.write(output)

	# Give execution permissions to the generated python file
	os.chmod(dest, 509)

	# Generate package.xml 
	# ___________________________________________
	# Load the Template of the package.xml
	template = env.get_template('temp_package.xml')
	
	# Fire up the rendering proccess
	output = template.render(pack=pack_data)
	
	# Write the generated file
	dest='package.xml'
	with open(dest, 'w') as f:
		f.write(output)

	# Give execution permissions to the generated python file
	os.chmod(dest, 509)
	
	# Generate setup.cfg
	# ___________________________________________
	# Load the Template of the setup.cfg
	template = env.get_template('temp_setup.cfg')
	
	# Fire up the rendering proccess
	output = template.render(pack=pack_data)
	
	# Write the generated file
	dest='setup.cfg'
	with open(dest, 'w') as f:
		f.write(output)

	# Give execution permissions to the generated python file
	os.chmod(dest, 509)

	# Generate nodes
	# ___________________________________________
	for node in package.hasNodes:
		# Load the Template of a node
		template = env.get_template('temp_node.py')
		# Build the node data to pass to the Template
		node_data = {}
		node_data['name'] = node.name
		# Build the publisher/subscriber data to pass to the Template
		sub = {}
		pub = {}
		subscribers = []
		publishers = []
		for s in node.hasSubscribers:
			sub['name'] = s.name
			sub['topicPath'] = s.topicPath
			sub['qos'] = 10
			subscribers.append(sub)
		for p in node.hasPublishers:
			pub['name'] = p.name
			pub['topicPath'] = p.topicPath
			pub['publishRate'] = p.publishRate
			pub['qos'] = 10
			publishers.append(pub)
		
		# Build the servers/clients data to pass to the Template
		ser = {}
		cli = {}
		servers = []
		clients = []
		for s in node.hasServers:
			ser['name'] = s.name
			ser['servicePath'] = s.servicePath
			ser['type'] = 'theType'
			servers.append(ser)
		for c in node.hasClients:
			cli['name'] = c.name
			cli['servicePath'] = c.servicePath
			cli['publishRate'] = c.publishRate
			cli['qos'] = 10
			clients.append(cli)
			
		# Fire up the rendering proccess
		output = template.render(pack = pack_data, node = node_data, publishers = publishers, subscribers = subscribers)
		
		# Write the generated file
		dest=package.name+'/'+node.name+'_node.py'
		with open(dest, 'w') as f:
			f.write(output)

		# Give execution permissions to the generated python file
		os.chmod(dest, 509)
		
	# Go to the workspace/src for the next package
	os.chdir('..')
