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
import sys
from jinja2 import Environment, FileSystemLoader
sys.path.append('metamodelLib')
import metamodel


# Create rset and load Metamodel
global_registry[Ecore.nsURI] = Ecore  
rset = ResourceSet()
# If you work with python package metamodel uncomment following line
# ~ rset.metamodel_registry[metamodel.nsURI] = metamodel
# if you with .ecore file metamodel ncomment following 3 lines
resource = rset.get_resource(URI('metamodelLib/metamodel.ecore'))
root = resource.contents[0]
rset.metamodel_registry[root.nsURI] = root

# We obtain the model from an XMI
model_root = rset.get_resource(URI('models/test2.xmi')).contents[0]


# Create the workspace directory tree
os.system('mkdir workspace')
os.chdir('workspace')
os.system('mkdir src')
os.chdir('src')
os.system('mkdir interfaces')
os.chdir('interfaces')
os.system('mkdir srv')
os.system('mkdir msg')
# Now the working directory is workspace/src/interfaces
os.chdir('..')
# Now the working directory is workspace/src

# Load the templates
file_loader = FileSystemLoader('../../templates')
env = Environment(loader=file_loader,trim_blocks=True, lstrip_blocks=True)

# Generate the custom interfaces
# Jinja2 Code
# Generate Topic Messages
# ___________________________________________
# Load the Template of the msg
template = env.get_template('temp_msg.msg')

# Build the msg data to pass to the Template
for t in model_root.hasCustomMessages:
	message_data = {}
	message_data['name'] = t.name
	message_data['description'] = t.description
	objects = []
	for o in t.hasObjectProperties:
		obj = {}
		obj['name'] = o.name
		obj['type'] = o.datatype.type
		obj['default'] = o.default
		obj['description'] = o.description
		if o.datatype.__class__.__name__=="ROSData":
			obj['package'] = o.datatype.package
		else:
			obj['package'] = "no"
		objects.append(obj)
	
	# Fire up the rendering proccess
	output = template.render(objects = objects, message_data=message_data)
	
	# Write the generated file
	dest='interfaces/msg/'+t.name+'.msg'
	with open(dest, 'w') as f:
		f.write(output)

# Generate Service Messages	
# ___________________________________________
# Load the Template of the srv
template = env.get_template('temp_srv.srv')
# Build the srv data to pass to the Template
for t in model_root.hasCustomServices:
	service_data = {}
	service_data['name'] = t.name
	service_data['description'] = t.description
	request = []
	for o in t.hasRequest.hasObjectProperties:
		req = {}
		req['name'] = o.name
		req['type'] = o.datatype.type
		req['default'] = o.default
		req['description'] = o.description
		if o.datatype.__class__.__name__=="ROSData":
			req['package'] = o.datatype.package
		else:
			req['package'] = "no"
		request.append(req)
	
	response = []
	for o in t.hasResponse.hasObjectProperties:
		res = {}
		res['name'] = o.name
		res['type'] = o.datatype.type
		res['default'] = o.default
		res['description'] = o.description
		if o.datatype.__class__.__name__=="ROSData":
			res['package'] = o.datatype.package
		else:
			res['package'] = "no"
		response.append(res)
	
	# Fire up the rendering proccess
	output = template.render(request = request, response = response, service_data=service_data)
	
	# Write the generated file
	dest='interfaces/srv/'+t.name+'.srv'
	with open(dest, 'w') as f:
		f.write(output)
	
# Generate interface package CMkakeLists.txt
# ___________________________________________
# Load the Template of the CMakeLists.txt
template = env.get_template('temp_CMakeLists.txt')
# Build the msg data to pass to the Template
tmessages = []
smessages = []
depend = []
for t in model_root.hasCustomMessages:
	tmessages.append(t.name)
	for tt in t.hasObjectProperties:
		# Find packages and add dependencies from ros datatypes
		if tt.datatype.__class__.__name__=="ROSData":
			if tt.datatype.package not in depend:
				depend.append(tt.datatype.package)
for t in model_root.hasCustomServices:
	smessages.append(t.name)
	for tt in t.hasResponse.hasObjectProperties:
		# Find packages and add dependencies from ros datatypes
		if tt.datatype.__class__.__name__=="ROSData":
			if tt.datatype.package not in depend:
				depend.append(t.datatype.package)
	for tt in t.hasRequest.hasObjectProperties:
		# Find packages and add dependencies from ros datatypes
		if tt.datatype.__class__.__name__=="ROSData":
			if tt.datatype.package not in depend:
				depend.append(t.datatype.package)
# Fire up the rendering proccess
output = template.render(smessages=smessages, tmessages=tmessages, depend=depend)
# Write the generated file
dest='interfaces/'+'CMakeLists.txt'
with open(dest, 'w') as f:
	f.write(output)

# Generate interface package package.xml
# ___________________________________________
# Load the Template of the package.xml
template = env.get_template('temp_cpppackage.xml')
# Fire up the rendering proccess
output = template.render()
# Write the generated file
dest='interfaces/'+'package.xml'
with open(dest, 'w') as f:
	f.write(output)

# Build the packages
for package in model_root.hasPackages:
	# Now the working directory is workspace/src
	# Create the package directory tree
	os.system('mkdir '+package.name)
	os.chdir(package.name)
	os.system('mkdir '+package.name)
	os.system('mkdir resource')
	os.chdir(package.name)
	os.system('touch __init__.py')
	os.chdir('../resource')
	os.system('touch '+package.name)
	os.chdir('..')
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
	
	# Build the package dependencies data to pass to the Template
	pack_depend = []
	# In Ros Services
	for i in package.hasRosServices:
		pack_depend.append(i.package)
	# In Ros Messages
	for i in package.hasRosMessages:
		pack_depend.append(i.package)
	
	# Dependencies for every node in the package
	for n in package.hasNodes:
		# In Subscribers using Ros Messages
		for s in n.hasSubscribers:
			if s.smsg.__class__.__name__=="CustomMessage":
				for o in s.smsg.hasObjectProperties:
					if o.datatype.__class__.__name__=="ROSData":
						if o.datatype.package not in pack_depend:
							pack_depend.append(o.datatype.package)
		# In Publushers using Ros Messages
		for p in n.hasPublishers:
			if p.pmsg.__class__.__name__=="CustomMessage":
				for o in p.pmsg.hasObjectProperties:
					if o.datatype.__class__.__name__=="ROSData":
						if o.datatype.package not in pack_depend:
							pack_depend.append(o.datatype.package)
		# In Servers using Ros Messages
		for s in n.hasServers:
			if s.servicemessage.__class__.__name__=="CustomService":
				for o in s.servicemessage.hasRequest.hasObjectProperties:
					if o.datatype.__class__.__name__=="ROSData":
						if o.datatype.package not in pack_depend:
							pack_depend.append(o.datatype.package)
				for o in s.servicemessage.hasResponse.hasObjectProperties:
					if o.datatype.__class__.__name__=="ROSData":
						if o.datatype.package not in pack_depend:
							pack_depend.append(o.datatype.package)
		# In Clients using Ros Messages
		for c in n.hasClients:
			if c.servicemessage.__class__.__name__=="CustomService":
				for o in c.servicemessage.hasRequest.hasObjectProperties:
					if o.datatype.__class__.__name__=="ROSData":
						if o.datatype.package not in pack_depend:
							pack_depend.append(o.datatype.package)
				for o in c.servicemessage.hasResponse.hasObjectProperties:
					if o.datatype.__class__.__name__=="ROSData":
						if o.datatype.package not in pack_depend:
							pack_depend.append(o.datatype.package)
		
	# Build the entry points data to pass to the Template
	entry_data = []
	for n in package.hasNodes:
		entry_data.append(n.name+'_exec = '+package.name+'.'+n.name+'_node:main'),
		for c in n.hasClients:
			entry_data.append(n.name+'_'+c.name+' = '+package.name+'.'+n.name+'_node:'+'run_'+c.name),

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
	output = template.render(pack=pack_data, pack_depend=pack_depend)
	
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
		node_data['namespace'] = node.namespace
		
		# Build the parameter data to pass to the Template
		params = []
		for p in node.hasParameters:
			param = {}
			param['name'] = p.name
			param['value'] = p.value
			param['type'] = p.type
			params.append(param)
		
		# Build the publisher/subscriber data to pass to the Template
		subscribers = []
		publishers = []
		types = []
		extra_imports = []
		for s in node.hasSubscribers:
			smsgObj = []
			sub = {}
			sub['name'] = s.name
			sub['topicPath'] = s.topicPath
			sub['qos'] = 10
			if s.smsg.name in types:
				sub['unique'] = 0
			else:
				sub['unique'] = 1
			sub['type'] = s.smsg.name
			types.append(s.smsg.name)
			if s.smsg.__class__.__name__=="CustomMessage":
				sub['package'] = 'interfaces'
				for r in s.smsg.hasObjectProperties:
					smsgObj.append(r.name)
					if r.datatype.__class__.__name__=="ROSData" and r.datatype.type not in types:
						imp = {}
						imp['type'] = r.datatype.type
						imp['package'] = r.datatype.package
						extra_imports.append(imp)
						types.append(r.datatype.type)
					
			else:
				sub['package'] = s.smsg.package
				#TODO append the Ros subscriber parameters
			
			sub['msg'] = smsgObj
			subscribers.append(sub)
		
		for p in node.hasPublishers:
			pmsgObj = []
			pub = {}
			pub['name'] = p.name
			pub['topicPath'] = p.topicPath
			pub['publishRate'] = p.publishRate
			pub['qos'] = 10
			if p.pmsg.name in types:
				pub['unique'] = 0
			else:
				pub['unique'] = 1
			pub['type'] = p.pmsg.name
			types.append(p.pmsg.name)
			if p.pmsg.__class__.__name__=="CustomMessage":
				pub['package'] = 'interfaces'
				for r in p.pmsg.hasObjectProperties:
					pmsgObj.append(r.name)
					if r.datatype.__class__.__name__=="ROSData" and r.datatype.type not in types:
						imp = {}
						imp['type'] = r.datatype.type
						imp['package'] = r.datatype.package
						extra_imports.append(imp)
						types.append(r.datatype.type)
			else:
				pub['package'] = p.pmsg.package
				#TODO append the Ros publisher parameters
			
			pub['msg'] = pmsgObj
			publishers.append(pub)
		
		# Build the servers/clients data to pass to the Template
		servers = []
		clients = []
		for s in node.hasServers:
			srequestObj = []
			sresponseObj = []
			ser = {}
			ser['name'] = s.name
			ser['servicePath'] = s.servicePath
			ser['serviceName'] = s.serviceName
			if s.servicemessage.name in types:
				ser['unique'] = 0
			else:
				ser['unique'] = 1
			ser['type'] = s.servicemessage.name
			types.append(s.servicemessage.name)
			if s.servicemessage.__class__.__name__=="CustomService":
				ser['package'] = 'interfaces'
				for r in s.servicemessage.hasRequest.hasObjectProperties:
					srequestObj.append(r.name)
					if r.datatype.__class__.__name__=="ROSData" and r.datatype.type not in types:
						imp = {}
						imp['type'] = r.datatype.type
						imp['package'] = r.datatype.package
						extra_imports.append(imp)
						types.append(r.datatype.type)
				for r in s.servicemessage.hasResponse.hasObjectProperties:
					sresponseObj.append(r.name)
					if r.datatype.__class__.__name__=="ROSData" and r.datatype.type not in types:
						imp = {}
						imp['type'] = r.datatype.type
						imp['package'] = r.datatype.package
						extra_imports.append(imp)
						types.append(r.datatype.type)
			else:
				ser['package'] = s.servicemessage.package
				#TODO append the Ros service parameters
			ser['requests'] = srequestObj
			ser['responses'] = sresponseObj
			servers.append(ser)
		
		for c in node.hasClients:
			crequestObj = []
			cresponseObj = []
			cli = {}
			cli['name'] = c.name
			cli['servicePath'] = c.servicePath
			cli['serviceName'] = c.serviceName
			
			if c.servicemessage.name in types:
				cli['unique'] = 0
			else:
				cli['unique'] = 1
			
			cli['type'] = c.servicemessage.name
			types.append(c.servicemessage.name)
			if c.servicemessage.__class__.__name__=="CustomService":
				cli['package'] = 'interfaces'
				for r in c.servicemessage.hasRequest.hasObjectProperties:
					crequestObj.append(r.name)
					if r.datatype.__class__.__name__=="ROSData" and r.datatype.type not in types:
						imp = {}
						imp['type'] = r.datatype.type
						imp['package'] = r.datatype.package
						extra_imports.append(imp)
						types.append(r.datatype.type)
				for r in c.servicemessage.hasResponse.hasObjectProperties:
					cresponseObj.append(r.name)
					if r.datatype.__class__.__name__=="ROSData" and r.datatype.type not in types:
						imp = {}
						imp['type'] = r.datatype.type
						imp['package'] = r.datatype.package
						extra_imports.append(imp)
						types.append(r.datatype.type)
			else:
				cli['package'] = c.servicemessage.package
				#TODO append the Ros client parameters
			
			cli['requests'] = crequestObj
			cli['responses'] = cresponseObj
			clients.append(cli)
			
		# Fire up the rendering proccess
		output = template.render(pack = pack_data, node = node_data, publishers = publishers, 
		subscribers = subscribers, objects = objects, smessages=smessages, tmessages=tmessages, 
		servers = servers, clients=clients, params = params,extra_imports=extra_imports)
		
		# Write the generated file
		dest=package.name+'/'+node.name+'_node.py'
		with open(dest, 'w') as f:
			f.write(output)

		# Give execution permissions to the generated python file
		os.chmod(dest, 509)
		
	# Go to the workspace/src for the next package
	os.chdir('..')
