# This File reads the metamodel, reads the model and renders the code
# to be generated to for the ROS2 package. Actually implements the 
# MDE transformation part, for model to code.
#
# Written in 14/4/2020
# Written by Rafael Brouzos
#
# After generating the code from the model go to the workspace root 
# (folder named "workspace") in terminal and run the comands:
# $ colcon build
# $ . install/setup.bash
# $ ros2 run [package_name] [node_name]_exec

from weasyprint import HTML
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
import networkx as nx
import matplotlib.pyplot as plt 
sys.path.append(os.path.join(os.path.dirname(__file__),'metamodelLib'))
# ~ import metamodel
import metageneros

# Obtain Generos Install directory
install_dir = str(os.path.dirname(__file__))

# Count arguments
if len(sys.argv) < 2 or  len(sys.argv) > 4:
    print ('Please give at least an XMI file name (model) and optionaly an Ecore file name (metamodel)')
    sys.exit(0)
# Obtain model filename
model_filename = os.path.relpath(sys.argv[1], install_dir)
# Obtain output directory
if len(sys.argv) == 3:
	destination = os.path.relpath(sys.argv[2], install_dir)
	print(destination)
	metamodel_filename = 'metamodelLib/metageneros.ecore'
elif len(sys.argv) == 4:
	destination = os.path.relpath(sys.argv[2], install_dir)
	metamodel_filename = os.path.relpath(sys.argv[3], install_dir)
else:
	destination = 'workspace'
	metamodel_filename = 'metamodelLib/metageneros.ecore'
	
# Go to working directory
if install_dir != '':
	os.chdir(install_dir)
		
# Create rset and load Metamodel
global_registry[Ecore.nsURI] = Ecore  
rset = ResourceSet()
# If you work with python package metamodel uncomment following line
# ~ rset.metamodel_registry[metamodel.nsURI] = metamodel
# if you with .ecore file metamodel uncomment following 3 lines
resource = rset.get_resource(URI(metamodel_filename))
root = resource.contents[0]
rset.metamodel_registry[root.nsURI] = root

# We obtain the model from an XMI
model_root = rset.get_resource(URI(model_filename)).contents[0]

# Create the workspace directory tree
os.system('mkdir '+destination)
os.chdir(destination)
os.system('mkdir src')
os.chdir('src')
# Create interfaces package directory tree
os.system('mkdir interfaces')
os.chdir('interfaces')
os.system('mkdir srv')
os.system('mkdir msg')
os.system('mkdir action')
os.system('mkdir documentation')
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
allmsg = []
objects = []
# Build the msg data to pass to the Template
for t in model_root.hasSoftware.hasPackages[0].hasTopicMessages:
	message_data = {}
	message_data['name'] = t.name
	message_data['description'] = t.description
	objects = []
	for o in t.hasObjectProperties:
		obj = {}
		obj['name'] = o.name
		obj['type'] = o.datatype.type
		obj['default'] = o.default
		obj['constant'] = o.constant
		obj['description'] = o.description
		if o.datatype.__class__.__name__=="ROSData":
			obj['package'] = o.datatype.package
		else:
			obj['package'] = "no"
		objects.append(obj)
	message_data['objects'] = objects
	allmsg.append(message_data)
	
	# Build msg only if it doesn't exist
	if t._container.__class__.__name__=="CustomPackage":
		# Fire up the rendering proccess
		output = template.render(objects = objects, message_data = message_data)
		
		# Write the generated file
		dest='interfaces/msg/'+t.name+'.msg'
		with open(dest, 'w') as f:
			f.write(output)

# Generate Service Messages	
# ___________________________________________
# Load the Template of the srv
template = env.get_template('temp_srv.srv')
# Build the srv data to pass to the Template
allsrv = []
for t in model_root.hasSoftware.hasPackages[0].hasServiceMessages:
	service_data = {}
	service_data['name'] = t.name
	service_data['description'] = t.description
	request = []
	for o in t.hasRequest.hasObjectProperties:
		req = {}
		req['name'] = o.name
		req['type'] = o.datatype.type
		req['default'] = o.default
		req['constant'] = o.constant
		req['description'] = o.description
		if o.datatype.__class__.__name__=="ROSData":
			req['package'] = o.datatype.package
		else:
			req['package'] = "no"
		request.append(req)
	service_data['requests'] = request
	
	response = []
	for o in t.hasResponse.hasObjectProperties:
		res = {}
		res['name'] = o.name
		res['type'] = o.datatype.type
		res['default'] = o.default
		res['constant'] = o.constant
		res['description'] = o.description
		if o.datatype.__class__.__name__=="ROSData":
			res['package'] = o.datatype.package
		else:
			res['package'] = "no"
		response.append(res)
	service_data['responses'] = response
	allsrv.append(service_data)
	
	# Build srv only if it doesn't exist
	if t._container.__class__.__name__=="CustomPackage":
		# Fire up the rendering proccess
		output = template.render(request = request, response = response, service_data = service_data)
		
		# Write the generated file
		dest='interfaces/srv/'+t.name+'.srv'
		with open(dest, 'w') as f:
			f.write(output)
	
# Generate Action Messages	
# ___________________________________________
# Load the Template of the action
template = env.get_template('temp_action.action')
# Build the srv data to pass to the Template
allactions = []
for t in model_root.hasSoftware.hasPackages[0].hasActionInterfaces:
	action_data = {}
	action_data['name'] = t.name
	action_data['description'] = t.description
	goal = []
	for o in t.hasGoal.hasObjectProperties:
		g = {}
		g['name'] = o.name
		g['type'] = o.datatype.type
		g['default'] = o.default
		g['constant'] = o.constant
		g['description'] = o.description
		if o.datatype.__class__.__name__=="ROSData":
			g['package'] = o.datatype.package
		else:
			g['package'] = "no"
		goal.append(g)
	action_data['goal'] = goal
	
	result = []
	for o in t.hasResult.hasObjectProperties:
		r = {}
		r['name'] = o.name
		r['type'] = o.datatype.type
		r['default'] = o.default
		r['constant'] = o.constant
		r['description'] = o.description
		if o.datatype.__class__.__name__=="ROSData":
			r['package'] = o.datatype.package
		else:
			r['package'] = "no"
		result.append(r)
	action_data['result'] = result
	
	feedback = []
	for o in t.hasFeedback.hasObjectProperties:
		r = {}
		r['name'] = o.name
		r['type'] = o.datatype.type
		r['default'] = o.default
		r['constant'] = o.constant
		r['description'] = o.description
		if o.datatype.__class__.__name__=="ROSData":
			r['package'] = o.datatype.package
		else:
			r['package'] = "no"
		feedback.append(r)
	action_data['feedback'] = feedback
	allactions.append(action_data)
	
	# Build action only if it doesn't exist
	if t._container.__class__.__name__=="CustomPackage":
		# Fire up the rendering proccess
		output = template.render(goal = goal, result = result, feedback = feedback, action_data = action_data)
		
		# Write the generated file
		dest='interfaces/action/'+t.name+'.action'
		with open(dest, 'w') as f:
			f.write(output)

# Generate interface package CMkakeLists.txt
# ___________________________________________
# Load the Template of the CMakeLists.txt
template = env.get_template('temp_CMakeLists.txt')
# Build the msg data to pass to the Template
tmessages = []
smessages = []
amessages = []
depend = []
# Custom message interfaces
for t in model_root.hasSoftware.hasPackages[0].hasTopicMessages:
	tmessages.append(t.name)
	for tt in t.hasObjectProperties:
		# Find packages and add dependencies from ros datatypes
		if tt.datatype.__class__.__name__=="ROSData":
			if tt.datatype.package not in depend:
				depend.append(tt.datatype.package)
# Custom service interfaces
for t in model_root.hasSoftware.hasPackages[0].hasServiceMessages:
	smessages.append(t.name)
	for tt in t.hasResponse.hasObjectProperties:
		# Find packages and add dependencies from ros datatypes
		if tt.datatype.__class__.__name__=="ROSData":
			if tt.datatype.package not in depend:
				depend.append(tt.datatype.package)
	for tt in t.hasRequest.hasObjectProperties:
		# Find packages and add dependencies from ros datatypes
		if tt.datatype.__class__.__name__=="ROSData":
			if tt.datatype.package not in depend:
				depend.append(tt.datatype.package)
# Custom action interfaces
for t in model_root.hasSoftware.hasPackages[0].hasActionInterfaces:
	amessages.append(t.name)
	for tt in t.hasGoal.hasObjectProperties:
		# Find packages and add dependencies from ros datatypes
		if tt.datatype.__class__.__name__=="ROSData":
			if tt.datatype.package not in depend:
				depend.append(tt.datatype.package)
	for tt in t.hasResult.hasObjectProperties:
		# Find packages and add dependencies from ros datatypes
		if tt.datatype.__class__.__name__=="ROSData":
			if tt.datatype.package not in depend:
				depend.append(tt.datatype.package)
	for tt in t.hasFeedback.hasObjectProperties:
		# Find packages and add dependencies from ros datatypes
		if tt.datatype.__class__.__name__=="ROSData":
			if tt.datatype.package not in depend:
				depend.append(tt.datatype.package)
# Fire up the rendering proccess
output = template.render(smessages=smessages, tmessages=tmessages, amessages = amessages, depend=depend)
# Write the generated file
dest='interfaces/'+'CMakeLists.txt'
with open(dest, 'w') as f:
	f.write(output)

# Generate documentation.html 
	# ___________________________________________
	# Load the Template of the documentation.html
	template = env.get_template('temp_interfaces_documentation.html')
	
	# Fire up the rendering proccess
	output = template.render(allmsg = allmsg, allsrv = allsrv, allactions = allactions)
	# Build the pdf of the Documentation
	HTML(string=output).write_pdf("interfaces/documentation/report.pdf", stylesheets=["../../templates/temp_pdf.css"])
	
	# Write the generated file
	dest='interfaces/documentation/documentation.html'
	with open(dest, 'w') as f:
		f.write(output)

	# Give execution permissions to the generated python file
	os.chmod(dest, 509)
	# Go to the workspace/src for the next package
	
	# Generate main.css 
	# ___________________________________________
	# Load the Template of the main.css
	template = env.get_template('temp_main.css')
	
	# Fire up the rendering proccess
	output = template.render()
	
	# Write the generated file
	dest='interfaces/documentation/main.css'
	with open(dest, 'w') as f:
		f.write(output)

	# Give execution permissions to the generated python file
	os.chmod(dest, 509)

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
for package in model_root.hasSoftware.hasPackages:
	if package.name == "interfaces" or package.name.startswith('launch') or package.builtin == True:
		continue
	# Now the working directory is workspace/src
	# Create the package directory tree
	os.system('mkdir '+package.name)
	os.chdir(package.name)
	# RosPackages should not be implemented
	if package.__class__.__name__!="RosPackage":
		# Now the working directory is workspace/src/package_name
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
	pack_data['maintainer'] = package.maintainer
	pack_data['email'] = package.email
	pack_data['description'] = package.description
	pack_data['license'] = package.license
	
	# Build the package dependencies data to pass to the Template
	# Registered Dependencies
	pack_depend = []
	pack_depend.append("rclpy")
	pack_depend.append("interfaces")
	for d in package.hasDependencies:
		if d.package.name not in pack_depend:
			pack_depend.append(d.package.name)
	# Dependencies for every node in the package
	for n in package.hasNodes:
		# In Subscribers using Ros Messages
		for s in n.hasSubscribers:
			if s.smsg.__class__.__name__=="CustomMessage":
				for o in s.smsg.hasObjectProperties:
					if o.datatype.__class__.__name__=="ROSData":
						if o.datatype.package not in pack_depend:
							pack_depend.append(o.datatype.package)
			else:
				if s.smsg.package not in pack_depend:
					pack_depend.append(s.smsg.package)
		# In Publishers using Ros Messages
		for p in n.hasPublishers:
			if p.pmsg.__class__.__name__=="CustomMessage":
				for o in p.pmsg.hasObjectProperties:
					if o.datatype.__class__.__name__=="ROSData":
						if o.datatype.package not in pack_depend:
							pack_depend.append(o.datatype.package)
			else:
				if p.pmsg.package not in pack_depend:
					pack_depend.append(p.pmsg.package)
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
			else:
				if s.servicemessage.package not in pack_depend:
					pack_depend.append(s.servicemessage.package)
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
			else:
				if c.servicemessage.package not in pack_depend:
					pack_depend.append(c.servicemessage.package)
		# In Action Clients using Action Interfaces
		for c in n.hasActionClients:
			if c.actioninterface.__class__.__name__=="CustomActionInterface":
				for o in c.actioninterface.hasGoal.hasObjectProperties:
					if o.datatype.__class__.__name__=="ROSData":
						if o.datatype.package not in pack_depend:
							pack_depend.append(o.datatype.package)
				for o in c.actioninterface.hasResult.hasObjectProperties:
					if o.datatype.__class__.__name__=="ROSData":
						if o.datatype.package not in pack_depend:
							pack_depend.append(o.datatype.package)
				for o in c.actioninterface.hasFeedback.hasObjectProperties:
					if o.datatype.__class__.__name__=="ROSData":
						if o.datatype.package not in pack_depend:
							pack_depend.append(o.datatype.package)
		# In Action Servers using Action Interfaces
		for c in n.hasActionServers:
			if c.actioninterface.__class__.__name__=="CustomActionInterface":
				for o in c.actioninterface.hasGoal.hasObjectProperties:
					if o.datatype.__class__.__name__=="ROSData":
						if o.datatype.package not in pack_depend:
							pack_depend.append(o.datatype.package)
				for o in c.actioninterface.hasResult.hasObjectProperties:
					if o.datatype.__class__.__name__=="ROSData":
						if o.datatype.package not in pack_depend:
							pack_depend.append(o.datatype.package)
				for o in c.actioninterface.hasFeedback.hasObjectProperties:
					if o.datatype.__class__.__name__=="ROSData":
						if o.datatype.package not in pack_depend:
							pack_depend.append(o.datatype.package)
		
	# Build the entry points data to pass to the Template
	entry_data = []
	for n in package.hasNodes:
		entry_data.append(n.name+'_exec = '+package.name+'.'+n.name+'_node:main'),
		for c in n.hasClients:
			entry_data.append(n.name+'_'+c.name+' = '+package.name+'.'+n.name+'_node:'+'run_'+c.name),
	
	# RosPackages should not be implemented
	if package.__class__.__name__!="RosPackage":
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
	
	# RosPackages should not be implemented
	if package.__class__.__name__!="RosPackage":
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
	
	# RosPackages should not be implemented
	if package.__class__.__name__!="RosPackage":
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
	allnodes = []
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
			param['type2'] = p.type.value
			param['description'] = p.description
			params.append(param)
			
		node_data['param'] = params
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
			# Add QoS profile
			if s.qosprofile.__class__.__name__=="CustomQosProfile":
				profile = {}
				profile['history'] = s.qosprofile.history
				profile['reliability'] = s.qosprofile.reliability
				profile['durability'] = s.qosprofile.durability
				profile['depth'] = s.qosprofile.depth
				profile['liveliness'] = s.qosprofile.liveliness
				profile['deadlineSec'] = s.qosprofile.deadlineSec
				profile['deadlineNSec'] = s.qosprofile.deadlineNSec
				profile['lifespanSec'] = s.qosprofile.lifespanSec
				profile['lifespanNSec'] = s.qosprofile.lifespanNSec
				profile['liveliness_lease_durationSec'] = s.qosprofile.liveliness_lease_durationSec
				profile['liveliness_lease_durationNSec'] = s.qosprofile.liveliness_lease_durationNSec
				profile['avoid_ros_namespace_conventions'] = s.qosprofile.avoid_ros_namespace_conventions
			elif s.qosprofile.__class__.__name__=="RosQosProfile":
				profile = {}
				profile['history'] = "standart"
				profile['name'] = s.qosprofile.name
			else:
				profile = {}
				profile['history'] = "default"
			
			sub['profile'] = profile
			# Add msg objects
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
				smsgObj.append(s.smsg.name)
				sub['package'] = s.smsg.package
				#TODO append the Ros subscriber parameters
			
			sub['msg'] = smsgObj
			subscribers.append(sub)
		node_data['subscribers'] = subscribers
		
		for p in node.hasPublishers:
			pmsgObj = []
			pub = {}
			pub['name'] = p.name
			pub['topicPath'] = p.topicPath
			pub['publishRate'] = p.publishRate
			pub['qos'] = 10
			# Add QoS profile
			if p.qosprofile.__class__.__name__=="CustomQosProfile":
				profile = {}
				profile['history'] = p.qosprofile.history
				profile['reliability'] = p.qosprofile.reliability
				profile['durability'] = p.qosprofile.durability
				profile['depth'] = p.qosprofile.depth
				profile['liveliness'] = p.qosprofile.liveliness
				profile['deadlineSec'] = p.qosprofile.deadlineSec
				profile['deadlineNSec'] = p.qosprofile.deadlineNSec
				profile['lifespanSec'] = p.qosprofile.lifespanSec
				profile['lifespanNSec'] = p.qosprofile.lifespanNSec
				profile['liveliness_lease_durationSec'] = p.qosprofile.liveliness_lease_durationSec
				profile['liveliness_lease_durationNSec'] = p.qosprofile.liveliness_lease_durationNSec
				profile['avoid_ros_namespace_conventions'] = p.qosprofile.avoid_ros_namespace_conventions
			elif p.qosprofile.__class__.__name__=="RosQosProfile":
				profile = {}
				profile['history'] = "standart"
				profile['name'] = p.qosprofile.name
			else:
				profile = {}
				profile['history'] = "default"
				
			pub['profile'] = profile
			# Add msg objects
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
				pmsgObj.append(p.pmsg.name)
				pub['package'] = p.pmsg.package
				#TODO append the Ros publisher parameters
			
			pub['msg'] = pmsgObj
			publishers.append(pub)
		node_data['publishers'] = publishers
		
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
			# Add QoS profile
			if s.qosprofile.__class__.__name__=="CustomQosProfile":
				profile = {}
				profile['history'] = s.qosprofile.history
				profile['reliability'] = s.qosprofile.reliability
				profile['durability'] = s.qosprofile.durability
				profile['depth'] = s.qosprofile.depth
				profile['liveliness'] = s.qosprofile.liveliness
				profile['deadlineSec'] = s.qosprofile.deadlineSec
				profile['deadlineNSec'] = s.qosprofile.deadlineNSec
				profile['lifespanSec'] = s.qosprofile.lifespanSec
				profile['lifespanNSec'] = s.qosprofile.lifespanNSec
				profile['liveliness_lease_durationSec'] = s.qosprofile.liveliness_lease_durationSec
				profile['liveliness_lease_durationNSec'] = s.qosprofile.liveliness_lease_durationNSec
				profile['avoid_ros_namespace_conventions'] = s.qosprofile.avoid_ros_namespace_conventions
			elif s.qosprofile.__class__.__name__=="RosQosProfile":
				profile = {}
				profile['history'] = "standart"
				profile['name'] = s.qosprofile.name
			else:
				profile = {}
				profile['history'] = "default"
				
			ser['profile'] = profile
			# Add srv objects
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
				srequestObj.append(s.servicemessage.name)
				ser['package'] = s.servicemessage.package
				#TODO append the Ros service parameters
			ser['requests'] = srequestObj
			ser['responses'] = sresponseObj
			
			servers.append(ser)
		node_data['servers'] = servers
		
		for c in node.hasClients:
			crequestObj = []
			cresponseObj = []
			cli = {}
			cli['name'] = c.name
			cli['servicePath'] = c.servicePath
			cli['serviceName'] = c.serviceName
			# Add QoS profile
			if c.qosprofile.__class__.__name__=="CustomQosProfile":
				profile = {}
				profile['history'] = c.qosprofile.history
				profile['reliability'] = c.qosprofile.reliability
				profile['durability'] = c.qosprofile.durability
				profile['depth'] = c.qosprofile.depth
				profile['liveliness'] = c.qosprofile.liveliness
				profile['deadlineSec'] = c.qosprofile.deadlineSec
				profile['deadlineNSec'] = c.qosprofile.deadlineNSec
				profile['lifespanSec'] = c.qosprofile.lifespanSec
				profile['lifespanNSec'] = c.qosprofile.lifespanNSec
				profile['liveliness_lease_durationSec'] = c.qosprofile.liveliness_lease_durationSec
				profile['liveliness_lease_durationNSec'] = c.qosprofile.liveliness_lease_durationNSec
				profile['avoid_ros_namespace_conventions'] = c.qosprofile.avoid_ros_namespace_conventions
			elif c.qosprofile.__class__.__name__=="RosQosProfile":
				profile = {}
				profile['history'] = "standart"
				profile['name'] = c.qosprofile.name
			else:
				profile = {}
				profile['history'] = "default"
				
			cli['profile'] = profile
			# Add srv objects
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
				crequestObj.append(c.servicemessage.name)
				cli['package'] = c.servicemessage.package
				#TODO append the Ros client parameters
			
			cli['requests'] = crequestObj
			cli['responses'] = cresponseObj
			clients.append(cli)
		node_data['clients'] = clients
		
		# Build the action servers/clients data to pass to the Template
		action_servers = []
		action_clients = []
		for s in node.hasActionServers:
			sgoalObj = []
			sresultObj = []
			sfeedbackObj = []
			ser = {}
			ser['name'] = s.name
			if s.actioninterface.name in types:
				ser['unique'] = 0
			else:
				ser['unique'] = 1
			ser['type'] = s.actioninterface.name
			types.append(s.actioninterface.name)
			if s.actioninterface.__class__.__name__=="CustomActionInterface":
				ser['package'] = 'interfaces'
				for r in s.actioninterface.hasGoal.hasObjectProperties:
					sgoalObj.append(r.name)
					if r.datatype.__class__.__name__=="ROSData" and r.datatype.type not in types:
						imp = {}
						imp['type'] = r.datatype.type
						imp['package'] = r.datatype.package
						extra_imports.append(imp)
						types.append(r.datatype.type)
				for r in s.actioninterface.hasResult.hasObjectProperties:
					sresultObj.append(r.name)
					if r.datatype.__class__.__name__=="ROSData" and r.datatype.type not in types:
						imp = {}
						imp['type'] = r.datatype.type
						imp['package'] = r.datatype.package
						extra_imports.append(imp)
						types.append(r.datatype.type)
				for r in s.actioninterface.hasFeedback.hasObjectProperties:
					sfeedbackObj.append(r.name)
					if r.datatype.__class__.__name__=="ROSData" and r.datatype.type not in types:
						imp = {}
						imp['type'] = r.datatype.type
						imp['package'] = r.datatype.package
						extra_imports.append(imp)
						types.append(r.datatype.type)
			else:
				ser['package'] = s.actioninterface.package
				#TODO append the Ros action parameters
			ser['goal'] = sgoalObj
			ser['result'] = sresultObj
			ser['feedback'] = sfeedbackObj
			action_servers.append(ser)
		node_data['action_servers'] = action_servers
		
		for c in node.hasActionClients:
			cgoalObj = []
			cresultObj = []
			cfeedbackObj = []
			cli = {}
			cli['name'] = c.name
			
			if c.actioninterface.name in types:
				cli['unique'] = 0
			else:
				cli['unique'] = 1
			
			cli['type'] = c.actioninterface.name
			types.append(c.actioninterface.name)
			if c.actioninterface.__class__.__name__=="CustomActionInterface":
				cli['package'] = 'interfaces'
				for r in c.actioninterface.hasGoal.hasObjectProperties:
					cgoalObj.append(r.name)
					if r.datatype.__class__.__name__=="ROSData" and r.datatype.type not in types:
						imp = {}
						imp['type'] = r.datatype.type
						imp['package'] = r.datatype.package
						extra_imports.append(imp)
						types.append(r.datatype.type)
				for r in c.actioninterface.hasResult.hasObjectProperties:
					cresultObj.append(r.name)
					if r.datatype.__class__.__name__=="ROSData" and r.datatype.type not in types:
						imp = {}
						imp['type'] = r.datatype.type
						imp['package'] = r.datatype.package
						extra_imports.append(imp)
						types.append(r.datatype.type)
				for r in c.actioninterface.hasFeedback.hasObjectProperties:
					cfeedbackObj.append(r.name)
					if r.datatype.__class__.__name__=="ROSData" and r.datatype.type not in types:
						imp = {}
						imp['type'] = r.datatype.type
						imp['package'] = r.datatype.package
						extra_imports.append(imp)
						types.append(r.datatype.type)
			else:
				cli['package'] = c.actioninterface.package
				#TODO append the Ros action parameters
			
			cli['goal'] = cgoalObj
			cli['result'] = cresultObj
			cli['feedback'] = cfeedbackObj
			action_clients.append(cli)
		node_data['action_clients'] = action_clients
		allnodes.append(node_data)
		
		# RosPackages should not be implemented
		if package.__class__.__name__!="RosPackage":
			# Fire up the rendering proccess
			output = template.render(pack = pack_data, node = node_data, publishers = publishers, 
			subscribers = subscribers, objects = objects, smessages=smessages, tmessages=tmessages, 
			servers = servers, clients=clients, params = params,extra_imports=extra_imports, 
			action_clients = action_clients, action_servers = action_servers)
			
			# Write the generated file
			dest=package.name+'/'+node.name+'_node.py'
			with open(dest, 'w') as f:
				f.write(output)

			# Give execution permissions to the generated python file
			os.chmod(dest, 509)
	
	# Generate documentation.html 
	# ___________________________________________
	# Load the Template of the documentation.html
	template = env.get_template('temp_documentation.html')
		
	# Fire up the rendering proccess
	output = template.render(pack=pack_data, allmsg = allmsg, allnodes = allnodes)
	os.system('mkdir documentation')
	
	# Build the pdf of the Documentation
	HTML(string=output).write_pdf("documentation/report.pdf", stylesheets=["../../../templates/temp_pdf.css"])
	
	# Write the generated file
	dest='documentation/documentation.html'
	with open(dest, 'w') as f:
		f.write(output)

	# Give execution permissions to the generated python file
	os.chmod(dest, 509)
	
	# Generate main.css 
	# ___________________________________________
	# Load the Template of the main.css
	template = env.get_template('temp_main.css')
	
	# Fire up the rendering proccess
	output = template.render()
	
	# Write the generated file
	dest='documentation/main.css'
	with open(dest, 'w') as f:
		f.write(output)

	# Give execution permissions to the generated python file
	os.chmod(dest, 509)
	# Go to the workspace/src for the next package
	os.chdir('..')

# Generate the Deployment package
# Jinja2 Code
# Generate Host packages
# ___________________________________________

# Generate package.xml 
# ___________________________________________
# Go to launchers package directory


for package in model_root.hasSoftware.hasPackages:
	if not package.name.startswith('launch'):
		continue

	# Now the working directory is workspace/src
	# Create the package directory tree
	os.system('mkdir '+package.name)
	os.chdir(package.name)
	# RosPackages should not be implemented
	if package.__class__.__name__!="RosPackage":
		# Now the working directory is workspace/src/package_name
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


	# Load the Template of the package.xml
	template = env.get_template('temp_package.xml')
	# Build the package data to pass to the Template
	pack_data = {}
	pack_data['packageName'] = package.name
	pack_data['maintainer'] = "Generos"
	pack_data['email'] = "rnm1816@gmail.com"
	pack_data['description'] = "This is a package, generated from Generos to contain the Deployment configuration of a Host. This package contains all the Launch Files that the user created in the model."
	pack_data['license'] = "Inherited from Repository"

	# Build the package dependencies data to pass to the Template
	# Registered Dependencies
	pack_depend = []
	pack_depend.append("rclpy")
	pack_depend.append("interfaces")
	
	
	for d in package.hasDependencies:
		if d.package.name not in pack_depend:
			pack_depend.append(d.package.name)

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

	output = template.render(pack=pack_data)

	# Write the generated file
	dest='setup.cfg'
	with open(dest, 'w') as f:
		f.write(output)

	# Give execution permissions to the generated python file
	os.chmod(dest, 509)

	# Generate Setup.py 
	# ___________________________________________
	# Load the Template of the setup.py
	template = env.get_template('temp_launchsetup.py')

	# Fire up the rendering proccess
	output = template.render(pack=pack_data)
	# Write the generated file
	dest='setup.py'
	with open(dest, 'w') as f:
		f.write(output)

	# Give execution permissions to the generated python file
	os.chmod(dest, 509)
	
	launchers_data = []
	host_data = {}
	# Generate each launch.py 
	for launch in package.hasDeployments:
		# Build the node data to pass to the Template
		nodes_data = []	
		launch_data = {}
		launch_data['name'] = launch.name
		launch_data['nodes'] = ""
		launch_data['executables'] = ""
		for node in launch.nodes:
			node_data = {}
			node_data['package'] = node._container.name
			node_data['namespace'] = node.namespace
			node_data['name'] = node.name
			node_data['executable'] = node.name+"_exec"
			node_data['version'] = launch.host.rosVersion.value
			#TODO add arguments
			nodes_data.append(node_data)
			launch_data['nodes'] = launch_data['nodes']+node.name+" | "
			launch_data['executables'] = launch_data['executables']+node.name+"_exec"+" | "
		launchers_data.append(launch_data)
		# Build Host data
		host_data['name'] = launch.host.name
		host_data['architecture'] = launch.host.architecture
		host_data['os'] = launch.host.OS
		host_data['hardDisk'] = launch.host.hardDisk
		host_data['memory'] = launch.host.memory
		host_data['rosVersion'] = launch.host.rosVersion
		# Build Network Interface data
		nis_data = []
		for ni in launch.host.hasNetworkInterfaces:
			ni_data = {}
			ni_data['gateway'] = ni.gateway
			ni_data['ip'] = ni.ip
			ni_data['subnetMask'] = ni.subnetMask
		
		# Load the Template of the setup.py
		template = env.get_template('temp_launch.py')

		# Fire up the rendering proccess
		output = template.render(nodes=nodes_data)
		# Write the generated file
		dest=package.name+'/'+launch.name+'.launch.py'
		with open(dest, 'w') as f:
			f.write(output)

		# Give execution permissions to the generated python file
		os.chmod(dest, 509)
	
	# Generate documentation.html 
	# ___________________________________________
	# Load the Template of the documentation.html
	template = env.get_template('temp_host_documentation.html')
		
	# Fire up the rendering proccess
	output = template.render(pack=pack_data, host = host_data, networks = nis_data, launchs = launchers_data)
	os.system('mkdir documentation')
	
	# Build the pdf of the Documentation
	HTML(string=output).write_pdf("documentation/report.pdf", stylesheets=["../../../templates/temp_pdf.css"])
	
	# Write the generated file
	dest='documentation/documentation.html'
	with open(dest, 'w') as f:
		f.write(output)

	# Give execution permissions to the generated python file
	os.chmod(dest, 509)
	
	# Generate main.css 
	# ___________________________________________
	# Load the Template of the main.css
	template = env.get_template('temp_main.css')
	
	# Fire up the rendering proccess
	output = template.render()
	
	# Write the generated file
	dest='documentation/main.css'
	with open(dest, 'w') as f:
		f.write(output)

	# Give execution permissions to the generated python file
	os.chmod(dest, 509)
	
	# Go to the workspace/src
	os.chdir('..')
	
# Generate communication graph 
# ___________________________________________	
# Go to the workspace
os.chdir('..')
G = nx.DiGraph()
node_nodes = []
node_services = []
node_actions = []
node_topics = []
edge_labels = {}
node_labels = {}
# Nodes
for n in model_root.hasSystemGraph.graph.nodes:
	# Node nodes
	G.add_node(n.name)
	node_labels[n.name] = n.name
	node_nodes.append(n.name)
# Services	
for n in model_root.hasSystemGraph.graph.hasServiceLinks:
	# Service nodes
	G.add_node(n.name)
	node_labels[n.name] = n.name
	node_services.append(n.name)
	# Service edges
	G.add_edge(n.server._container.name, n.name)
	edge_labels[n.server._container.name, n.name] = n.server.name
	for c in n.client:
		G.add_edge(n.name, c._container.name)
		edge_labels[n.name, c._container.name] = c.name
# Actions	
for n in model_root.hasSystemGraph.graph.hasActionLinks:
	# Action nodes
	G.add_node(n.name)
	node_labels[n.name] = n.name
	node_actions.append(n.name)
	# Action edges
	G.add_edge(n.actionserver._container.name, n.name)
	edge_labels[n.actionserver._container.name, n.name] = n.actionserver.name
	for c in n.actionclient:
		G.add_edge(n.name, c._container.name)
		edge_labels[n.name, c._container.name] = c.name
# Topics
for n in model_root.hasSystemGraph.graph.hasTopics:
	# Topic nodes
	G.add_node(n.topicPath)
	node_labels[n.topicPath] = n.topicPath
	node_topics.append(n.topicPath)
	# Topic edges
	G.add_edge(n.publisher._container.name, n.topicPath)
	edge_labels[n.publisher._container.name, n.topicPath] = n.publisher.name
	for c in n.subscriber:
		G.add_edge(n.topicPath, c._container.name)
		edge_labels[n.topicPath, c._container.name] = c.name
	
# Make plot
plt.subplots(1, figsize=(16,16))
# Obtain position
pos = nx.spiral_layout(G)
# Plot Nodes
nx.draw_networkx_nodes(G,pos=pos,nodelist=node_nodes, node_size=2300, node_color='skyblue', label='Nodes', with_labels = True, alpha = 0.5)
# Plot Services
nx.draw_networkx_nodes(G,pos=pos,nodelist=node_services, node_size=2300, node_color='pink', label='Services', with_labels = True, alpha = 0.5)
# Plot Actions
nx.draw_networkx_nodes(G,pos=pos,nodelist=node_actions, node_size=2300, node_color='red', label='Actions', with_labels = True, alpha = 0.5)
# Plot Topics
nx.draw_networkx_nodes(G,pos=pos,nodelist=node_topics, node_size=2300, node_color='lightgreen', label='Topics', with_labels = True, alpha = 0.5)
# Plot Labels on Nodes
nx.draw_networkx_labels(G,pos=pos, labels = node_labels, font_size = 8, alpha = 0.8)
# Plot Edges
nx.draw_networkx_edges(G, pos, width=1, arrows = True, min_source_margin = 30, min_target_margin = 30)
# Plot Labels on Edges
nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, font_size=8, margin = 180)
# Plot Legend
plt.legend(loc = 'best', scatterpoints=1, labelspacing=4.5, handletextpad = 3, borderpad = 3)
# Save figure as image
plt.savefig('System Graph.png')



# Generate package graph 
# ___________________________________________	
PG = nx.DiGraph()
package_nodes = []
edge_labels = {}
node_labels = {}
# Packages
for n in model_root.hasSystemGraph.packagegraph.package:
	# Package nodes
	PG.add_node(n.name)
	node_labels[n.name] = n.name
	package_nodes.append(n.name)
	
	
# Edges
for n in model_root.hasSystemGraph.packagegraph.package:
	# Dependencies Edges
	for d in n.hasDependencies:
		PG.add_edge(n.name, d.package.name)
		edge_labels[n.name, d.package.name] = "dep"
		

# Make plot
plt.subplots(1, figsize=(20,20))
# Obtain position
pos = nx.circular_layout(PG)
# Plot Packages
nx.draw_networkx_nodes(PG,pos=pos,nodelist=package_nodes, node_size=20000, node_color='skyblue', node_shape='s', label='Packages', with_labels = True, alpha = 0.5)
# Plot Labels on Packages
nx.draw_networkx_labels(PG,pos=pos, labels = node_labels, font_size = 18, alpha = 0.8)
# Plot Edges
nx.draw_networkx_edges(PG, pos=pos, width=1, arrows = True, min_source_margin = 30, min_target_margin = 30)

# Plot Legend
# ~ plt.legend(loc = 'best', scatterpoints=1, labelspacing=4.5, handletextpad = 3, borderpad = 3)
# Save figure as image
plt.savefig('Package Graph.png') 
