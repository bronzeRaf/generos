# Generos
A Domain Specific Language to generate easilly ROS2 packages. Create complex ROS2 systems in minutes.
Generos provides:
- ROS2 systems with unlimited packages at once
- Convenience on coding with a powerfull easy-to-learn DSL
- Instructions into the generated packages to make the functionality additions a piece of cake
- High quality code and comments into the packages 
- High quality documentation into the packages
- Communication Graph in every system
- Automatically deals with all the dependencies
- Automatically deals with all the imports
- Supports all the ROS packages
- Generates and documents Custom Messages, Services, Actions with zero efford

______________________________________________________________________________

## Installing Generos:

### Automatic Install
In order to install and to run Generos with its full capabilities you have to install some software that Generos uses. It is highly recomended to use the official bash installer of Generos to make sure all you libraries are set and up to date. Inside the folder you would like to install Generos run:

```
$ wget https://raw.githubusercontent.com/bronzeRaf/generos/master/install.bash
$ sudo bash install.bash
```

You are done!

REMEMBER! You will also need to install a ROS2 in your system to test your generated package, but you still can generate them...
You can find ROS2 [here](https://index.ros.org/doc/ros2/Installation/Crystal/Linux-Install-Binary/).


### Manual Install
If you want to manually install Generos make sure that you know what you are doing
A Linux distribution is required to use Generos but Ubuntu 18.04 is recommended.
Install:
- [Python 3](https://www.python.org/downloads/)
- [Pyecore](https://pyecore.readthedocs.io/en/latest/user/install.html)
- [Pyecoregen](https://pypi.org/project/pyecoregen/)
- [Jinja2](https://pypi.org/project/Jinja2/)
- [TextX](https://textx.github.io/textX/stable/#installation)
- [NetworkX](https://networkx.github.io/documentation/stable/install.html)
- [Matplotlib](https://matplotlib.org/users/installing.html)
- [Weasyprint](https://weasyprint.readthedocs.io/en/latest/install.html)
- [Ros2](https://index.ros.org/doc/ros2/Installation/Crystal/Linux-Install-Binary/)

All this software is free and available in the links above. After installing this software you can download the latest Generos [here](https://github.com/bronzeRaf/generos/archive/master.zip).
Unzip Generos and you are done!


## Running Generos:
To run Generos you will need a GRS file, with the model representing the system you would like to generate. To learn how to write GRS files take a look [here](#writing-grs-files).

After saving the GRS file that represents your awesome ROS2 System run:

```
$ sudo bash path-to-generos-installation/generos.bash path-to-GRS/model.grs

```
Replacing:
- "path-to-generos-installation" with the path to the installation folder of generos
- "path-to-GRS/model.grs" with the path to the GRS file

Generos works with both absolute and relative paths. 

That's it, Enjoy Package Generating!

______________________________________________________________________________

## Writing GRS files:
GRS files are models that represent ROS2 Systems. It is actually a DSL to describe what Generos you would like to generate for you. 

A GRS program consist of many Commands. A command could be:  
Package | Node | Parameter | Publisher | Subscriber | Client | Server | ActionServer | ActionClient | Dependency | Message | ServiceMessage | ActionInterface | QoSProfile

Commands could be placed in any order. Every Command consinst of some special Components, based on its type.
Below you can see the components per Command. In these examples, in the comments you can see the datatype of any Component, if this component is optional or reqiured and if it is single component or not. For example a ROS2 package could have many nodes, but only one maintainer. Multiple components are separated by spaces. Anything between double ssterisks ``(**anything**)`` means that you need to replace them with your code. The order of the Components inside a Command is critical and could not be changed.

### Comments
In GRS comments start with // and takes all the rest of the line.

For example
```
This is code // This is comment
//This is another comment
```

### Packages
To create a Package you can write:

```
package **pack1** {
	path = "**packagePath**"	//string, required, single
	license = "**license**"		//string, required, single
	maintainer = "**maintainer**"	//string, required, single
	email = "**email**"		//string, required, single
	builtin = **True**		//bool, optional, single 
	hasNode = **n1** **n2**		//node, optional, many
	hasDependency = **dep1**	//dependency, optional, many
}
```

### Nodes
To create a Node you can write:

```
node **n1** {
	namespace = "**namespace**"	//string, optional, single
	hasParameter = **pr1**		//parameter, optional, many
	hasPublisher = **pub1**		//publisher, optional, many
	hasSubscriber = **sub1**	//subscriber, optional, many
	hasServer = **sr1**		//server, optional, many
	hasClient = **c1**		//client, optional, many
	hasActionServer = **asr1**	//actionServer, optional, many
	hasActionClient = **ac1**	//actionClient, optional, many
}
```

### Parameter
To create a Parameter you can write:

```
parameter **pr1** {
	type = **type**			//string, required, single
	value = "**value**"		//string, required, single
	description = "**description**"	//string, optional, single
}
```

### Publisher
To create a Publisher you can write:

```
publisher **pub1** {
	topicPath = "**path**"		//string, required, single
	publishRate = **2.45**		//float, required, single
	message = **m1**		//message, required, single
	qos = **qos1**			//qosprofile or presetqos, optional, single
}
```

### Subscriber
To create a Subscriber you can write:

```
subscriber **sub1** {
	topicPath = "**path**"		//string, required, single
	message = **Header**		//message, required, single
	qos = **SENSOR_DATA**		//qosprofile or presetqos, optional, single
}
```

### Client
To create a Client you can write:

```
client **c1** {
	servicePath = "**path**"	//string, required, single
	serviceName = "**name**"	//string, required, single
	service = **srv1**		//service, required, single
	qos = **qos1**			//qosprofile or presetqos, optional, single
}
```

### Server
To create a Server you can write:

```
server **sr1** {
	servicePath = "**path**"	//string, required, single
	serviceName = "**name**"	//string, required, single
	service = **srv1**		//service, required, single
	qos = **qos1**			//qosprofile or presetqos, optional, single
}
```

### Action Server
To create an Action Server you can write:

```
actionServer **asr1** {
	action = **action1**		//action, required, single
}
```

### Action Client
To create an Action Client you can write:

```
actionClient **ac1** {
	action = **action1**		//action, required, single
}
```

### Dependency
To create a Dependency you can write:

```
dependency **dep1** {
	package = **pack2**		//package, required, single
}
```

### Message
To create a Message you can write:

```
message mes1 {
	
}

message **Header** package = "**std_msgs**"	//just give the name of a ROS Msg
```

### Service
To create a Service you can write:

```
service p1 {
	
}
```

### Action
To create an Action you can write:

```
service p1 {
	
}
```

### QoS Profile
A QoS Profile is either a Custom QoS Profile and a ROS Preset QoS Profile. So you can follow one of the following:

```
qosprofile qos1 {
	
}

presetqos **SENSOR_DATA**	//just give the name of a QoS preset profile
```
______________________________________________________________________________

## Understanding Generos:
Lets take a further look inside Generos to understand how it works...

### dsl:
This folder contains all the related to the dsl languange programms. The "generos.tx" implements the grammar of the dsl containing all the rules the language should fullfil written in [TextX](https://textx.github.io/textX/stable/). The "model.grs" is an example model created in Generos DSL and models a specific ROS System with some packages, nodes etc. The "run_generos_model.py" is the interpreter that obtains the "model.grs" parses it, validates it and creates the "generos.xmi" file form the "models" directory to pass it through the Generos ROS2 package generator mechanism.


### metamodelLib:
This folder contains python module called "metamodel" implementing the metamodel of the [ROS2](https://index.ros.org/doc/ros2/Tutorials/) world. The module contains all the EClasses and the behavior, to build powerfull models. The folder contains also the ecore implementation of the metamodel in the file "metamodel.ecore". Anyone can import the python module or the ecore impementation of the metamodel to build models almost the same way. Finally, the file named "metamodelGenerator.py" reeds the ecore implementation of the "metamodel.ecore" and generates the python module "metamodel", using [pyecoregen](https://github.com/pyecore/pyecoregen). The "metamodel.jpg" is the image of the metamodel diagram from the Eclipse Modeling Framework. You can see the diagram below.

![Metamodel](/metamodelLib/metamodel.jpg)


### models:
This folder demenstrates some kind of models that could be generated into ROS2 package from the system. The "model.py" receives the ecore metamodel to validate and builds the "test.xmi" file using [pyecore](https://buildmedia.readthedocs.org/media/pdf/pyecore/latest/pyecore.pdf). The "model2.py" model receives the metamodel python module to validate and builds the "test2.xmi" file using [pyecore](https://buildmedia.readthedocs.org/media/pdf/pyecore/latest/pyecore.pdf). The "modelj.json" is an example of a json model. The "generos.xmi" is an xmi model generated by the Generos DSL. Any of the xmi or json file with this format (created or generated) could work as an input in the ROS2 package generator mechanism of Generos.


### templates:
This folder contains all the [jinja2](https://buildmedia.readthedocs.org/media/pdf/jinja/latest/jinja.pdf) templates that the ROS2 package generator mechanism loads to build the ROS2 package. 

- The temp_CMakeLists.txt is a template of the CMakeLists.txt file, needed to build a ROS2 package called "interfaces" implementing all the interfaces (custom Srv, Msg and Actions) created by the user.

- The temp_cpppaackage.xml is a template of the package.xml file, needer to build the "interfaces" package.

- The temp_msg.msg is a template of the custom msg type, created by the user in the "interfaces" package.

- The temp_srv.srv is a template of the custom srv type, created by the user in the "interfaces" package.

- The temp_action.action is a template of the custom action type, created by the user in the "interfaces" package.

- The temp_node.py is a template of the node implementation. In every node all the callbacks, the Publishers, Subscribers, Services, Clients, Action Servers and Action Clients are working in the generated executable named "{Node's name}_exec". For every Client in the node, another executable is generated, named "{Node's name}_{Client's name}", so it can be called seperatelly. This extra executable run once, until the Server's response is obtained and exits.

- The temp_package.xml is a template of the package.xml file of the generated package. It contains the package and the maintainer information, as long as the dependencies.

- The temp_setup.cfg is a template of the setup.cfg file of the generated package

- The temp_setup.py is a template of the setup.py file of the generated package. It contains one enrty point per node, an executable called "{Node's name}_exec" to the function called "main" inside the nodes. For every client into a node, it creates another entry point named "{Node's name}_{Client's name}" to the function called "{Client's name}".

- The temp_documentation.html is a template of the documentation for every one of the generated packages in an html format. It contains all the information about the package as well as the nodes, servers, clients, action servers, action clients, publishers and subscribers that belong to the package.

- The temp_interfaces_documentation.html is a template of the documentation of the generated package "interfaces". It contains all the information about the custom Msgs, Srvs and Actions that the user created.

- The temp_main.css is a template of the css used in the html documentation of every package. It contains all the classes for an easy to read documentation.

- The temp_pdf.css is a template of the css used in the pdf documentation of every package. It contains all the classes for an easy to read documentation.


### workspace:
This folder is generated from the ROS2 package generator mechanism of Generos. It contains the "src" folder with the package "interfaces" and all the created by the user packages. The package "interfaces" is a Cpp package, implementing all the custom action, srv and msg that the user created. The rest of the packages, are those the user created, generated in Python. In the packages there is one enrty point per node, an executable called "{Node's name}_exec" to the function called "main" inside the nodes. For every Client into a node, there is another entry point named "{Node's name}_{Client's name}" to the function called "{Client's name}". In addition, the "System Graph.png" image contains a representation of the generated system. It represents all the Nodes, the Topics (Publishers and Subscribers), the Services (Clients and Servers) and the Actions (Action Clients and Action Server) that the system contains independent of their packages. It is a comynication diagramm that demonstrates all the flow of the information inside the ROS system. It is created from [NetworkX](https://networkx.github.io/) and [Matplotlib](https://matplotlib.org/).

To run the executables After generating the code from the model go to the workspace root (folder named "workspace") in terminal and run the comands:
```
$ colcon build
$ . install/setup.bash
$ ros2 run {package_name} {executable_name}
```

You can now open multiple terminals from the workspace root (folder named "workspace") and run executables simultaneously. You don't need to build the packages again, just to locate the ROS2. so run the commands:
```
$ . install/setup.bash
$ ros2 run {package_name} {executable_name}
```

**After any change into the package you need to build the packages once (with ```$ colcon build```). But every time you need to locate ROS2 before running an executable (with ```$ . install/setup.bash```)


### packageGenerator.py:
This file is the ROS2 package generator mechanism of Generos. It is able to reed the "metamodel" python module or the "metamodel.ecore" and any xmi model of the system, it validates the model from the metamodel, and it generates the ROS2 packages inside the workspace directory using jinja2. It should be called once, for a single metamodel and a single xmi model. It is able to generate multiple packages, with multiple containments.

______________________________________________________________________________


