from pyecore.resources import ResourceSet, URI
from pyecore.ecore import EClass, EAttribute
from pyecore.utils import DynamicEPackage
import pyecore.behavior as behavior
import metamodel

# Read the metamodel first
rset = ResourceSet()
mm_root = rset.get_resource(URI('/home/raf/Desktop/Thesis Project/ecoreWork/metamodel.ecore')).contents[0]

# Register the metamodel (in case we open an XMI model later)
rset.metamodel_registry[mm_root.nsURI] = mm_root
# Get the metamodel helper
helper = DynamicEPackage(mm_root)





#Behavior build
rosystem = EClass('ROSSystem')
rospackage = EClass('Package')




@rospackage.behavior
def greeting(self):
	print('Hello from package: ', self.name)

@behavior.main
@helper.rosystem.behavior
def entry_point(self):
	print('Hello World and', self.name)




# We obtain the model from an XMI
model_root = rset.get_resource(URI('/home/raf/Desktop/Thesis Project/ecoreWork/test.xmi')).contents[0]
behavior.run(model_root)
