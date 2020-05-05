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
	message_data['objects'] = objects
	allmsg.append(message_data)
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
	service_data['requests'] = request
	
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
	service_data['responses'] = response
	allsrv.append(service_data)
	
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
for t in model_root.hasCustomActionInterfaces:
	action_data = {}
	action_data['name'] = t.name
	action_data['description'] = t.description
	goal = []
	for o in t.hasGoal.hasObjectProperties:
		g = {}
		g['name'] = o.name
		g['type'] = o.datatype.type
		g['default'] = o.default
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
		r['description'] = o.description
		if o.datatype.__class__.__name__=="ROSData":
			r['package'] = o.datatype.package
		else:
			r['package'] = "no"
		feedback.append(r)
	action_data['feedback'] = feedback
	
	allactions.append(action_data)
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
for t in model_root.hasCustomMessages:
	tmessages.append(t.name)
	for tt in t.hasObjectProperties:
		# Find packages and add dependencies from ros datatypes
		if tt.datatype.__class__.__name__=="ROSData":
			if tt.datatype.package not in depend:
				depend.append(tt.datatype.package)
# Custom service interfaces
for t in model_root.hasCustomServices:
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
for t in model_root.hasCustomActionInterfaces:
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
		# In Publishers using Ros Messages
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
				#TODO append the Ros client parameters
			
			cli['goal'] = cgoalObj
			cli['result'] = cresultObj
			cli['feedback'] = cfeedbackObj
			action_clients.append(cli)
		node_data['action_clients'] = action_clients
		allnodes.append(node_data)
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
	# Go to the workspace/src for the next package
	
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
