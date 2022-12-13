#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


from geometry_msgs.msg import PoseStamped

class SetGoal(Node): 

    def __init__(self):
        self.count = 0
        super().__init__("goal_node")
        self.publisher_ = self.create_publisher(PoseStamped,"/goal_pose",10)
        self.timer_ =self.create_timer(0.5,self.publish_news)
        self.get_logger().info("Gaol Target has been started")

    def publish_news(self):
        # Header Part
        self.msg = PoseStamped()
        self.msg.header.stamp = SetGoal.get_clock(self).now().to_msg()
        self.msg.header.frame_id = "map"

        # Pose Part
        self.msg.pose.position.x = 1.4523660013236623
        self.msg.pose.position.y = 1.5745374556755736
        self.msg.pose.position.z = 0.0

        self.msg.pose.orientation.x = 0.0
        self.msg.pose.orientation.y = 0.0
        self.msg.pose.orientation.z = 0.7850401615130306
        self.msg.pose.orientation.w = 0.6194448682583422

        if self.count == 0:   # publish the message just one time
            print("moving on to goal point...")
            self.publisher_.publish(self.msg)
            self.count += 1

def main(args=None):
    rclpy.init(args=args)
    node = SetGoal() # object
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()