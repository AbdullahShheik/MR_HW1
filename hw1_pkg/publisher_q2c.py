import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublisherNode(Node):
    def __init__(self):
        super().__init__('node_publisher')
        self.publisher_ = self.create_publisher(String, 'char_topic', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        char = input("Enter a character: ")
        if len(char) == 1:      
            msg = String()
            msg.data = char
            self.publisher_.publish(msg)
            self.get_logger().info(f'Publishing: {char}')
        else:
            self.get_logger().info('Please enter a single character only')

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()