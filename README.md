# Generos
A Domain Specific Language to generate easilly ROS2 packages.

## metamodelLib:
This folder contains python module called "metamodel" implementing the metamodel of the [ROS2](https://index.ros.org/doc/ros2/Tutorials/) world. The module also contains all the EClasses and the behavior, to build powerfull models. The folder contains also the ecore implementation of the metamodel in the file "metamodel.ecore". Anyone can import the python module or the ecore impementation to build models almost the same way. Finally, the file named "metamodelGenerator.py" reeds the ecore implementation of the "metamodel.ecore" and generates the python module "metamodel", using [pyecoregen](https://github.com/pyecore/pyecoregen). The "metamodel.jpg" is the image of the metamodel diagram from the Eclipse Modeling Framework. You can see the diagram below.

![Metamodel](/metamodelLib/metamodel.jpg)

______________________________________________________________________________

## models:
This folder demenstrates some kind of models that could be generated into ROS2 package from the system. The "model.py" receives the ecore metamodel to validate and builds the "test.xmi" file using [pyecore](https://buildmedia.readthedocs.org/media/pdf/pyecore/latest/pyecore.pdf). The "model2.py" model receives the metamodel python module to validate and builds the "test2.xmi" file using [pyecore](https://buildmedia.readthedocs.org/media/pdf/pyecore/latest/pyecore.pdf). The "modelj.json" is an example of a json model. Any of the xmi or json file with this format (created or generated) could work as an input in the ROS2 package generator mechanism of Generos.
______________________________________________________________________________

## templates:
This folder contains all the [jinja2](https://buildmedia.readthedocs.org/media/pdf/jinja/latest/jinja.pdf) templates that the ROS2 package generator mechanism loads to build the ROS2 package. 

- The temp_CMakeLists.txt is a template of the CMakeLists.txt file, needed to build a ROS2 package called "interfaces" implementing all the interfaces (custom Srv, Msg and Actions) created by the user.

- The temp_cpppaackage.xml is a template of the package.xml file, needer to build the "interfaces" package.

- The temp_msg.msg is a template of the custom msg type, created by the user in the "interfaces" package.

- The temp_srv.srv is a template of the custom srv type, created by the user in the "interfaces" package.

- The temp_action.action is a template of the custom action type, created by the user in the "interfaces" package.

- The temp_node.py is a template of the node implementation. In every node all the callbacks, the Publishers, Subscribers, Services, Clients, Action Servers and Action Clients are working in the generated executable named "{Node's name}_exec". For every Client in the node, another executable is generated, named "{Node's name}_{Client's name}", so it can be called seperatelly. This extra executable run once, until the Server's response and exits.

- The temp_package.xml is a template of the package.xml file of the generated package. It contains the package and the maintainer information, as long as the dependencies.

- The temp_setup.cfg is a template of the setup.cfg file of the generated package

- The temp_setup.py is a template of the setup.py file of the generated package. It contains one enrty point per node, an executable called "{Node's name}_exec" to the function called "main" inside the nodes. For every client into a node, it creates another entry point named "{Node's name}_{Client's name}" to the function called "{Client's name}".

______________________________________________________________________________
## workspace:
This folder is generated from the ROS2 package generator mechanism. It contains the "src" folder with the package "interfaces" and all the created by the user packages. The package "interfaces" is a Cpp package, implementing all the custom action, srv and msg that the user created. The rest of the packages, are those the user created, generated in Python. In the packages there is one enrty point per node, an executable called "{Node's name}_exec" to the function called "main" inside the nodes. For every Client into a node, there is another entry point named "{Node's name}_{Client's name}" to the function called "{Client's name}".

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

______________________________________________________________________________
## packageGenerator.py:
This file is the ROS2 package generator mechanism. It is able to reed the "metamodel" module or the "metamodel.ecore" and any xmi model of the system, it validates the model from the metamodel, and it generates the ROS2 packages inside the workspace directory using jinja2. It should be called once, for a single metamodel and a single xmi model. It is able to generate multiple packages, with multiple containments.
