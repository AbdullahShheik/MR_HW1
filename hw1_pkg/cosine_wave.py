import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

topic1 = '/turtle1/cmd_vel'
period = 10

def main(args=None):
    
    rclpy.init(args=args)
    
    controlVel = Twist()
    
    controlVel.linear.x = 2.0
    controlVel.linear.y = 0.0
    controlVel.linear.z = 0.0
    
    controlVel.angular.x = 0.0
    controlVel.angular.y = 0.0
    controlVel.angular.z = 0.0

    TestNode = Node("cosine_wave_node")
    
    publisher = TestNode.create_publisher(Twist, topic1, 1)
    
    rate = TestNode.create_rate(period)
    
    counter = 0
    
    while rclpy.ok():
        print("Sending control message")
        
        controlVel.angular.z = math.cos(counter * 0.2)
        counter += 1
        
        publisher.publish(controlVel)
        
        rclpy.spin_once(TestNode)
        rate.sleep()
    
    TestNode.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()