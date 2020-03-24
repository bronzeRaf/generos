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
from jinja2 import Environment, FileSystemLoader


# We load the Ecore metamodel first
global_registry[Ecore.nsURI] = Ecore  
rset = ResourceSet()
resource = rset.get_resource(URI('metamodel.ecore'))
# ~ rset.resource_factory['json'] = lambda uri: JsonResource(uri)
root = resource.contents[0]  # We get the root (an EPackage here)
# Register the metamodel (in case we open an XMI model later)
rset.metamodel_registry[root.nsURI] = root



# We obtain the model from an XMI
model_root = rset.get_resource(URI('models/test.xmi')).contents[0]

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

	# Generate interfaces*************************
	# ___________________________________________
	# Load the Template of the msg
	template = env.get_template('temp_msg.msg')
	
	
	# Build the msg data to pass to the Template
	for t in package.hasTopicMessages:
		objects = []
		obj = {}
		for o in t.hasCommunicationObjects:
			obj['name'] = o.name
			obj['type'] = o.type
			objects.append(obj)
	
		# Fire up the rendering proccess
		output = template.render(objects = objects)
		
		# Write the generated file
		dest='../interfaces/msg/'+t.name+'.msg'
		with open(dest, 'w') as f:
			f.write(output)
			
	# ___________________________________________
	# Load the Template of the srv
	template = env.get_template('temp_srv.srv')
	# Build the srv data to pass to the Template
	for t in package.hasServiceMessages:
		request = []
		for o in t.hasRequest.hasCommunicationObjects:
			req = {}
			req['name'] = o.name
			req['type'] = o.type
			request.append(req)
		
		response = []
		for o in t.hasResponse.hasCommunicationObjects:
			res = {}
			res['name'] = o.name
			res['type'] = o.type
			response.append(res)
	
		# Fire up the rendering proccess
		output = template.render(request = request, response = response)
		
		# Write the generated file
		dest='../interfaces/srv/'+t.name+'.srv'
		with open(dest, 'w') as f:
			f.write(output)
			
	# Generate interface package
	# ___________________________________________
	# Load the Template of the CMakeLists.txt
	template = env.get_template('temp_CMakeLists.txt')
	# Build the msg data to pass to the Template
	tmessages = []
	smessages = []
	for t in package.hasTopicMessages:
		tmessages.append(t.name)
	for t in package.hasServiceMessages:
		smessages.append(t.name)
	# Fire up the rendering proccess
	output = template.render(smessages=smessages, tmessages=tmessages)
	# Write the generated file
	dest='../interfaces/'+'CMakeLists.txt'
	with open(dest, 'w') as f:
		f.write(output)
			
	
	# Load the Template of the CMakeLists.txt
	template = env.get_template('temp_cpppackage.xml')
	# Fire up the rendering proccess
	output = template.render()
	# Write the generated file
	dest='../interfaces/'+'package.xml'
	with open(dest, 'w') as f:
		f.write(output)
	
			
			
	# Generate nodes
	# ___________________________________________
	for node in package.hasNodes:
		# Load the Template of a node
		template = env.get_template('temp_node.py')
		# Build the node data to pass to the Template
		node_data = {}
		node_data['name'] = node.name
		# Build the publisher/subscriber data to pass to the Template
		subscribers = []
		publishers = []
		for s in node.hasSubscribers:
			sub = {}
			sub['name'] = s.name
			sub['topicPath'] = s.topicPath
			sub['qos'] = 10
			sub['type'] = s.smsg.name
			subscribers.append(sub)
		for p in node.hasPublishers:
			pub = {}
			pub['name'] = p.name
			pub['topicPath'] = p.topicPath
			pub['publishRate'] = p.publishRate
			pub['qos'] = 10
			pub['type'] = p.pmsg.name
			publishers.append(pub)
		
		# Build the servers/clients data to pass to the Template
		ser = {}
		cli = {}
		servers = []
		clients = []
		for s in node.hasServers:
			ser['name'] = s.name
			ser['servicePath'] = s.servicePath
			ser['type'] = s.servicemessage.name
			servers.append(ser)
		for c in node.hasClients:
			cli['name'] = c.name
			cli['servicePath'] = c.servicePath
			cli['publishRate'] = c.publishRate
			cli['qos'] = 10
			cli['type'] = c.servicemessage.name
			clients.append(cli)
			
		# Fire up the rendering proccess
		output = template.render(pack = pack_data, node = node_data, publishers = publishers, subscribers = subscribers, objects = objects, smessages=smessages, tmessages=tmessages)
		
		# Write the generated file
		dest=package.name+'/'+node.name+'_node.py'
		with open(dest, 'w') as f:
			f.write(output)

		# Give execution permissions to the generated python file
		os.chmod(dest, 509)
		
	# Go to the workspace/src for the next package
	os.chdir('..')
