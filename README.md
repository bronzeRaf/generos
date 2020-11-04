
# Generos
A Domain Specific Language for easy and fast generation of ROS2 packages. Create complex ROS2 systems in minutes.

Generos provides:
- ROS2 systems with unlimited packages at once
- Convenience on coding with a powerful easy-to-learn DSL
- A component based approach for readable, reusable, maintainable and functional models
- Instructions into the generated packages to make the functionality additions a piece of cake
- High quality code and comments into the packages 
- High quality documentation into the packages
- Communication Graph in every system
- Package Graph in every system
- Automatically deals with all the dependencies
- Automatically deals with all the imports
- Automatically generates host packages and their launch files for an easy deployment
- Supports system topology modeling
- Supports modeling of pre-existing packages
- Supports modeling of QoS profiles 
- Supports all the ROS packages
- Generates and documents Custom Messages, Services, Actions with zero effort


______________________________________________________________________________

## Installing Generos:

### Automatic Install
In order to install and to run Generos with its full capabilities you have to install some software that Generos uses. It is highly recommended to use the official bash installer of Generos to make sure all your libraries are set and up to date. Inside the folder you would like to install Generos run:

```
$ wget https://raw.githubusercontent.com/bronzeRaf/generos/master/install.bash
$ sudo bash install.bash
```

You are done!

REMEMBER! You will also need to install a ROS2 in your system to test your generated packages, but you still can generate them...
You can find ROS2 [here](https://index.ros.org/doc/ros2/Installation/Crystal/Linux-Install-Binary/ "Install ROS2").


### Manual Install
If you still want to manually install Generos make sure that you know what you are doing!
A Linux distribution is required to use Generos but Ubuntu 18.04 is recommended.
Install:
- [Python 3](https://www.python.org/downloads/ "Install Python 3")
- [Pyecore](https://pyecore.readthedocs.io/en/latest/user/install.html "Install Pyecore")
- [Pyecoregen](https://pypi.org/project/pyecoregen/ "Install Pyecoregen")
- [Jinja2](https://pypi.org/project/Jinja2/ "Install Jinja2")
- [TextX](https://textx.github.io/textX/stable/#installation "Install TextX")
- [NetworkX](https://networkx.github.io/documentation/stable/install.html "Install NetworkX")
- [Matplotlib](https://matplotlib.org/users/installing.html "Install Matplotlib")
- [Weasyprint](https://weasyprint.readthedocs.io/en/latest/install.html "Install Weasyprint")
- [Ros2](https://index.ros.org/doc/ros2/Installation/Crystal/Linux-Install-Binary/ "Install ROS2")

All this software is free and available in the links above. After installing this software you can download the latest Generos [here](https://github.com/bronzeRaf/generos/archive/master.zip "Download the latest Generos").
Unzip Generos and you are done!


## Running Generos:
To run Generos you will need a GRS file, with the model representing the system you would like to generate. To learn how to write GRS files take a look [here](#writing-grs-files "GRS Files").

After saving the GRS file that represents your awesome ROS2 System run:

```
$ sudo bash path-to-generos-installation/generos.bash path-to-GRS/model.grs path-to-output

```
Replacing:
- "path-to-generos-installation" with the absolute path to the installation folder of Generos
- "path-to-GRS/model.grs" with the absolute path to the GRS file
- "path-to-output" with the path you would like to save the generated system

Find your awesome ROS2 System in "path-to-output"/workspace

*NOTICE! Generos run script works with absolute paths. 

That's it, Enjoy Package Generating!

______________________________________________________________________________

## Writing GRS files:
GRS files are models that represent ROS2 Systems. GRS is actually a DSL to describe what Generos you would like to generate for you. 

First of all import old models into your model. Generos provides a python-like import system, on the top of your models. Multiple or Nested imports work perfectly. Just add one of the following lines:

```
import path-to/old_model.grs
import path-to/older_model.grs as older
```

Replacing:
- "path-to" with the absolute or the relative path to the old model
- "old_model.grs" with the name of the old model

And use:
- Any component of "old_model.grs" with its name
- Any component of "older_model.grs" with "older.name", where name is the component's name

A GRS model consists of *Commands*. A *Command* could be:  
Package | Node | Parameter | Publisher | Subscriber | Client | Server | ActionServer | ActionClient | Dependency | Message | ServiceMessage | ActionInterface | QoSProfile | Host | Deployment | NetworkInterface | LocalNetwork

*Commands* could be placed in any order. Every *Command* defines a *Component* with a unique name and every *Component* consists of some special *Attributes*, based on its type, inside an *Attribute Block* { }.

Below you can see the accepted *Attributes* per *Component*. In these examples, in the comments you can see for any *Attribute*, its datatype, if it is optional or required and if it is single or multiple valued. For example a ROS2 package could have many nodes, but only one maintainer. Multiple values in *Attributes* are separated by commas (,) and could be unlimited. 

Anything between double asterisks ``(**anything**)`` means that you need to replace it with your code and without the asterisks. The order of the *Attributes* inside a *Component* is critical and could not be changed. But the optional *Attributes* could always be skipped.

### Comments
In GRS comments start with // and takes all the rest of the line. Comment can be placed anywhere, even inside *Attribute Blocks*.

For example
```
This is code // This is comment
//This is another comment
```

### Packages
To create a [Package](https://index.ros.org/doc/ros2/Tutorials/Creating-Your-First-ROS2-Package/ "ROS2 Packages") you can write:

```
package **pack1** {
	description = "**describe it**"	//string, required, single
	path = "**packagePath**"	//string, required, single
	license = "**license**"		//string, required, single
	maintainer = "**maintainer**"	//string, required, single
	email = "**email**"		//string, required, single
	version = "**Foxy_Fitzroy**"	//string, required, single
	builtin = **True**		//bool, optional, single 
	hasNodes = **n1** **n2**	//node, optional, many
	hasDependencies = **dep1**	//dependency, optional, many
}
```
*NOTICE! Declaring a package with the special identifier  "ros" as ``ros package **pack1**{...}`` will skip the package generation. Use this identifier for pre-existing ROS 2 packages to model, include, document and install them without regenerating them.

### Nodes
To create a [Node](https://index.ros.org/doc/ros2/Tutorials/Understanding-ROS2-Nodes/ "ROS2 Nodes") you can write:

```
node **n1** {
	namespace = "**namespace**"	//string, optional, single
	hasParameters = **pr1**		//parameter, optional, many
	hasPublishers = **pub1**	//publisher, optional, many
	hasSubscribers = **sub1**	//subscriber, optional, many
	hasServers = **sr1**		//server, optional, many
	hasClients = **c1**		//client, optional, many
	hasActionServers = **asr1**	//actionServer, optional, many
	hasActionClients = **ac1**	//actionClient, optional, many
}
```

### Parameter
To create a [Parameter](https://index.ros.org/doc/ros2/Tutorials/Parameters/Understanding-ROS2-Parameters/ "ROS2 Parameters") you can write:

```
parameter **pr1** {
	type = **type**			//string, required, single
	value = "**value**"		//string, required, single
	description = "**description**"	//string, optional, single
}
```

### Publisher
To create a [Publisher](https://index.ros.org/doc/ros2/Tutorials/Topics/Understanding-ROS2-Topics/ "ROS2 Topics") you can write:

```
publisher **pub1** {
	topicPath = "**path**"		//string, required, single
	publishRate = **2.45**		//float, required, single
	message = **mes1**		//message, required, single
	qos = **qos1**			//qosprofile or presetqos, optional, single
}
```

### Subscriber
To create a [Subscriber](https://index.ros.org/doc/ros2/Tutorials/Topics/Understanding-ROS2-Topics/ "ROS2 Topics") you can write:

```
subscriber **sub1** {
	topicPath = "**path**"		//string, required, single
	message = **Header**		//message, required, single
	qos = **SENSOR_DATA**		//qosprofile or presetqos, optional, single
}
```

### Client
To create a [Client](https://index.ros.org/doc/ros2/Tutorials/Services/Understanding-ROS2-Services/ "ROS2 Services") you can write:

```
client **c1** {
	servicePath = "**path**"	//string, required, single
	serviceName = "**name**"	//string, required, single
	service = **srv1**		//service, required, single
	qos = **qos1**			//qosprofile or presetqos, optional, single
}
```

### Server
To create a [Server](https://index.ros.org/doc/ros2/Tutorials/Services/Understanding-ROS2-Services/ "ROS2 Services") you can write:

```
server **sr1** {
	servicePath = "**path**"	//string, required, single
	serviceName = "**name**"	//string, required, single
	service = **Set_Bool**		//service, required, single
	qos = **qos1**			//qosprofile or presetqos, optional, single
}
```

### Action Server
To create an [Action Server](https://index.ros.org/doc/ros2/Tutorials/Understanding-ROS2-Actions/ "ROS2 Actions") you can write:

```
actionServer **asr1** {
	action = **action1**		//action, required, single
}
```

### Action Client
To create an [Action Client](https://index.ros.org/doc/ros2/Tutorials/Understanding-ROS2-Actions/ "ROS2 Actions") you can write:

```
actionClient **ac1** {
	action = **action1**		//action, required, single
}
```

### Dependency
To create a Dependency to a package you can write:

```
dependency **dep1** {
	package = **pack2**		//package, required, single
}
```

### Message
A Message is either a [Custom Msg](https://index.ros.org/doc/ros2/Tutorials/Custom-ROS2-Interfaces/ "ROS2 Custom Interfaces") or a [ROS Msg](https://index.ros.org/packages/page/1/time/ "ROS2 Bultin Packages"). So you can follow one of the following examples:

```
message **mes1** {
	datatype **int64**, **a**, description = "**description...**"
	datatype **bool**, **b**, description = "**description...**", constant = **True**, default = "**False**"
	rostype **Header**, **h**, **std_msgs**
	datatype **string**, **s**, description = "**another description...**" default = "**Value**"
}

message **Header** package = "**std_msgs**"	//just give the name of a ROS Msg and its package
```

A Custom Message consist of several Primitive datatypes and/or ROS datatypes. 
- Primitive Dataypes follow the formula:
	- ```datatype type, name, description (string, optional), constant (bool, optional), default (string, optional)```
- ROS Data Types follow the formula:
	- ```rostype type, name, package (string, required)```

A Ros Message consist of a type and a package.

### Service
A Service is either a [Custom Srv](https://index.ros.org/doc/ros2/Tutorials/Custom-ROS2-Interfaces/ "ROS2 Custom Interfaces") or a [ROS Srv](https://index.ros.org/packages/page/1/time/ "ROS2 Bultin Packages"). So you can follow one of the following examples:

```
service **srv1** {
	request:
		datatype **int64**, **a**, description = "**description...**"
		datatype **bool**, **b**, description = "**description...**", constant = **True**, default = "**False**"
	response:
		datatype **string**, **s**, description = "**another description...**" default = "**Value**"
}

service **SetBool** package = "**std_srvs**"	//just give the name of a ROS Srv and its package

```

A Custom Service consist of a Request and a Response. Both of them follow the formula of the Custom Messages.

The ROS Services also follow the formula of the ROS Messages.

### Action
To create an [Action](https://index.ros.org/doc/ros2/Tutorials/Understanding-ROS2-Actions/ "ROS2 Actions") you can write:

```
service **action1** {
	goal:
		datatype **int64**, **a**, description = "**description...**"
	result:
		datatype **string**, **s**, description = "**another description...**" default = "**Value**"
	feedback:
		datatype **bool**, **b**, description = "**description...**", constant = **True**, default = "**False**"
}
```
An Action consist of a Goal, a Result and a Feedback. All of them follow the formula of the Custom Messages.

### QoS Profile
A QoS Profile is either a [Custom QoS Profile](https://index.ros.org/doc/ros2/Tutorials/Ros2bag/Overriding-QoS-Policies-For-Recording-And-Playback/ "ROS2 QoS Overriding") or a [ROS Preset QoS Profile](https://index.ros.org/doc/ros2/Concepts/About-Quality-of-Service-Settings/ "ROS2 About Qos"). So you can follow one of the following examples:

```
qosprofile **qos1** {
	history = "**KEEP_LAST**"			//string, optional, single
	depth = **10**					//int, optional, single
	reliability = "**RELIABLE**"			//string, optional, single
	durability = "**VOLATILE**"			//string, optional, single
	livelines = "**AUTOMATIC**"			//string, optional, single
	deadlineSec = "**2**"				//int, optional, single
	deadlineNSec = "**3**"				//int, optional, single
	lifespanSec = "**4**"				//int, optional, single
	lifespanNSec = "**5**"				//int, optional, single
	liveliness_lease_durationSec = "**6**"		//int, optional, single
	liveliness_lease_durationNSec = "**7**"		//int, optional, single
	avoid_ros_namespace_conventions = **False**	//bool, optional, single
}

presetqos **SENSOR_DATA**	//just give the name of a QoS preset profile
```

### Host
To create a Host device in the system topology you can write:

```
host **h1** {
	architecture = "**KEEP_LAST**"			//string, required, single
	os = "**Ubuntu_18**"				//string, required, single
	hardDisk = **2048.32**				//float, required, single
	memory = **1024.68**				//float, required, single
	rosVersion = "**Foxy_Fitzroy**"			//string, required, single
	hasNetworkInterfaces = **netw1**		//networkinterface, optional, many
	hasDependencies = **dep1**			//dependency, optional, many
}
```

### NetworkInterface
To create a NetworkInterface in the system you can write:

```
networkinterface **netw1** {
	gateway = "**192.168.1.254**"			//string, required, single
	subnetMask = "**255.255 255.0**"		//string, required, single
	ip = "**192.168.1.88**"				//string, required, single
}
```

### LocalNetwork
To create a LocalNetwork in the system you can write:

```
localnetwork **ln1** {
	gateway = "**192.168.1.254**"			//string, required, single
	subnetMask = "**255.255 255.0**"		//string, required, single
	ip = "**192.168.1.88**"				//string, required, single
}
```

### Deployment
To create a Deployment configuration ([launch file](https://index.ros.org/doc/ros2/Tutorials/Launch-Files/Creating-Launch-Files/)) in a host package you can write:

```
deployment **dpl1** {
	arguments = "**__log_level:=debug**"		//string, optional, many
	nodes = **node1**				//node, optional, many
	host = **h1**					//host, required, single
}
```
______________________________________________________________________________

## Understanding Generos:
Lets take a further look inside Generos to understand how it works...

### dsl:
This folder contains all the related to the dsl language programs. The "generos.tx" implements the grammar of the dsl containing all the rules the language should fulfill written in [TextX](https://textx.github.io/textX/stable/ "TextX"). The "run_generos_model.py" is the interpreter that obtains a model, parses it, validates it and creates the "generos.xmi" file in the "models" directory to pass it through the Generos ROS2 package generator engine.


### metamodelLib:
This folder contains python module called "metageneros" implementing the metamodel of the [ROS2](https://index.ros.org/doc/ros2/Tutorials/ "ROS2") world. The module contains all the EClasses and the behavior, to build powerful models. The folder contains also the ecore implementation of the metamodel in the file "metageneros.ecore". Anyone can import the python module or the ecore implementation of the metamodel to build models almost the same way. The file named "metamodelGenerator.py" reeds the ecore implementation of the "metageneros.ecore" and generates the python module "metageneros", using [pyecoregen](https://github.com/pyecore/pyecoregen "Pyecoregen"). The folder "partial metamodels" contains the partial metamodels, that combined produce the complete one, as long as their images, visualize by the Eclipse Modeling Framework.


### models:
This folder contain  some kind of models that could be generated into ROS2 package from the system. The "generos.xmi" is an xmi model generated by the GRS model through a Model to Model transformation before the Generos fire up the generator engine. Any xmi or json file with this format (created or generated) could work as an input in the ROS2 package generator engine of Generos.


### templates:
This folder contains all the [jinja2](https://buildmedia.readthedocs.org/media/pdf/jinja/latest/jinja.pdf "Jinja2") templates that the ROS2 package generator engine loads to build the ROS2 package. 

- The temp_CMakeLists.txt is a template of the CMakeLists.txt file, needed to build a ROS2 package called "interfaces" implementing all the interfaces (custom Srv, Msg and Actions) created by the user.

- The temp_cpppaackage.xml is a template of the package.xml file, needed to build the "interfaces" package.

- The temp_msg.msg is a template of the custom msg type, created by the user in the "interfaces" package.

- The temp_srv.srv is a template of the custom srv type, created by the user in the "interfaces" package.

- The temp_action.action is a template of the custom action type, created by the user in the "interfaces" package.

- The temp_node.py is a template of the node implementation. In every node all the callbacks, the Publishers, Subscribers, Services, Clients, Action Servers and Action Clients are working in the generated executable named "{Node's name}_exec". For every Client in the node, another executable is generated, named "{Node's name}_{Client's name}", so it can be called separately. This extra executable run once, until the Server's response is obtained and exits.

- The temp_package.xml is a template of the package.xml file of the generated package. It contains the package and the maintainer information, as long as the dependencies.

- The temp_setup.cfg is a template of the setup.cfg file of the generated package

- The temp_setup.py is a template of the setup.py file of the generated package. It contains one enrty point per node, an executable called "{Node's name}_exec" to the function called "main" inside the nodes. For every client into a node, it creates another entry point named "{Node's name}_{Client's name}" to the function called "{Client's name}".

- The temp_documentation.html is a template of the documentation for every one of the generated packages in an html format. It contains all the information about the package as well as the nodes, servers, clients, action servers, action clients, publishers and subscribers that belong to the package.

- The temp_interfaces_documentation.html is a template of the documentation of the generated package "interfaces". It contains all the information about the custom Msgs, Srvs and Actions that the user created.

- The temp_main.css is a template of the css used in the html documentation of every package. It contains all the classes for an easy to read documentation.

- The temp_pdf.css is a template of the css used in the pdf documentation of every package. It contains all the classes for an easy to read documentation.

- The temp_launch.py is a template of deployment configuration (launch file) used in host's packages.

- The temp_launchsetup.py is a template of the setup.py file of a host's package to declare launch files.


### examples:
This folder contains examples of generated ROS2 system, with their models. For every example there is a folder containing the model (or models) that Generos received as input and a workspace folder, generated by Generos as output. Every workspace contains the "src" folders with the package "interfaces", the packages of every host and all the created by the user packages. The package "interfaces" is a Cpp package, implementing all the custom action, srv and msg that the user created. The packages of the hosts are packages automatically generated by Generos, one for each host created in the model. These packages contain the deployment configuration of each host. The rest of the packages, are those the a user created, generated in Python. In the packages there is one entry point per node, an executable called "{Node's name}_exec" to the function called "main" inside the nodes. For every Client into a node, there is another entry point named "{Node's name}_{Client's name}" to the function called "{Client's name}". In addition, the "System Graph.png" image contains a representation of the generated system's communications. It represents all the Nodes, the Topics (Publishers and Subscribers), the Services (Clients and Servers) and the Actions (Action Clients and Action Server) that the system contains independent of their packages. It is a communication diagram that demonstrates all the flow of the information inside the ROS2 system. The "Package Graph.png" is a UML-like package graph, shopwing the packages of the ROS2 system as long as their dependencies. Both graphs have been created from [NetworkX](https://networkx.github.io/ "NetworkX") and [Matplotlib](https://matplotlib.org/ "Matplotlib").

To run the executables After generating the code from the model go to the workspace root in terminal and run the commands:
```
$ colcon build
$ . install/setup.bash
$ ros2 run {package_name} {executable_name}
```

You can now open multiple terminals from the workspace root (folder named "example/workspace") and run executables simultaneously. You don't need to build the packages again, just to locate the ROS2. So run the commands:
```
$ . install/setup.bash
$ ros2 run {package_name} {executable_name}
```

*NOTICE! After any change into the package you need to build the packages once (with ```$ colcon build```). But every time you need to locate ROS2 before running an executable (with ```$ . install/setup.bash```)


### packageGenerator.py:
This file is the ROS2 package generator engine of Generos. It is able to read the "metageneros" python module or the "metageneros.ecore" and any xmi model of the system (basically the "generos.xmi"), it validates the model from the metamodel, and it generates the ROS2 packages inside the target workspace directory using jinja2. It should be called once, for a single metamodel and a single xmi model. It is able to generate multiple packages, with multiple containments.

### generos.bash:
This file is a bash script, able to fire up the whole Generos procedure. It receives the model and the target workspace folder as an input and makes the proper calls, to get the final ROS2 system generated. It requires sudo rights to be able to generate, edit and move files.

### install.bash:
This file is a bash script, able to install the whole Generos softwrae and its dependencies. It doesn't need any arguments. It installs and updates all the required by Generos tools, except ROS2. It requires sudo rights to be able to download, install and update software.

______________________________________________________________________________


