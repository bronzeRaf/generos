
node: Node_2



# TODO messages

import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class Node_2(Node):

    def __init__(self):
        super().__init__(Node_2)
        # Publishers
        #____________________________________________
		
		# Subscribers
        #____________________________________________
        self.suby1= self.create_subscription(String, s.topicPath, self.listener1, 10)
		self.suby1 
		
        timer_period = 0.5  # seconds
        
        def listener1(self, msg):
			self.get_logger().info('I heard: "%s"' % msg.data)

		

def main(args=None):
    rclpy.init(args=args)

    newnode = Node_2()

    rclpy.spin(newnode)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    newnode.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()