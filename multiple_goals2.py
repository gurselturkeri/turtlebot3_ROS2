import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from actionlib_msgs.msg import GoalStatus

class NavigationNode(Node):
    def __init__(self):
        super().__init__('navigation_node')
        self.publisher = self.create_publisher(
            PoseStamped,
            '/move_base_simple/goal',
            10)
        self.goal_status_sub = self.create_subscription(
            GoalStatus,
            '/move_base/status',
            self.goal_status_callback,
            10)
        self.goal_status_sub  # prevent unused variable warning
        self.goals = [[1, 0, 0], [1, 1, 0], [0, 1, 0]]
        self.current_goal_index = 0

    def publish_goal(self, goal):
        goal_msg = PoseStamped()
        goal_msg.header.frame_id = 'map'
        goal_msg.pose.position.x = goal[0]
        goal_msg.pose.position.y = goal[1]
        goal_msg.pose.orientation.z = sin(goal[2]/2)
        goal_msg.pose.orientation.w = cos(goal[2]/2)
        self.publisher.publish(goal_msg)

    def goal_status_callback(self, msg):
        if msg.status == GoalStatus.SUCCEEDED:
            self.current_goal_index += 1
            if self.current_goal_index < len(self.goals):
                self.publish_goal(self.goals[self.current_goal_index])
            else:
                self.get_logger().info('All goals reached!')

def main(args=None):
    rclpy.init(args=args)
    node = NavigationNode()

    # Publish first goal
    node.publish_goal(node.goals[0])

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
