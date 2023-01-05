import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

class NavigationNode(Node):
    def __init__(self):
        super().__init__('navigation_node')
        self.publisher = self.create_publisher(
            PoseStamped,
            '/move_base_simple/goal',
            10)

    def publish_goal(self, x, y, theta):
        goal_msg = PoseStamped()
        goal_msg.header.frame_id = 'map'
        goal_msg.pose.position.x = x
        goal_msg.pose.position.y = y
        goal_msg.pose.orientation.z = sin(theta/2)
        goal_msg.pose.orientation.w = cos(theta/2)
        self.publisher.publish(goal_msg)

def main(args=None):
    rclpy.init(args=args)
    node = NavigationNode()

    # Publish three goals
    node.publish_goal(1, 0, 0)
    node.publish_goal(1, 1, 0)
    node.publish_goal(0, 1, 0)

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
