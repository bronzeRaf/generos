{# 
#This is a jinja2 template of a ROS2 Node
#
# Written in 13/3/2020
# Written by Rafael Brouzos
#}

node: {{node.name}}

{%for p in publishers %}
publisher name {{ p.name }}
publisher path {{p.topicPath}}
{%endfor%}


# TODO messages

import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class {{node.name}}(Node):

    def __init__(self):
        super().__init__({{node.name}})
        # Publishers
        #____________________________________________
        {%for p in publishers %}
        self.{{p.name}}= self.create_publisher(String, {{p.topicPath}}, 10)
		
        timer_period = 0.5  # seconds
        
        self.timer{{loop.index}} = self.create_timer(timer_period, self.timer_callback{{loop.index}})
        self.i = 0
		
		
    def timer_callback{{loop.index}}(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.{{p.name}}.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

		{%endfor%}
		
		# Subscribers
        #____________________________________________
        {%for s in subscribers %}
        self.{{s.name}}= self.create_subscription(String, s.topicPath, self.listener{{loop.index}}, 10)
		self.{{s.name}} 
		
        timer_period = 0.5  # seconds
        
        def listener{{loop.index}}(self, msg):
			self.get_logger().info('I heard: "%s"' % msg.data)

		{%endfor%}
		

def main(args=None):
    rclpy.init(args=args)

    newnode = {{node.name}}()

    rclpy.spin(newnode)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    newnode.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
