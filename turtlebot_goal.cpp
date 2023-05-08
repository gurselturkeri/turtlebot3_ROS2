#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/pose_stamped.hpp"

class goalNode : public rclcpp::Node
{
public:
    goalNode() : Node("set_goal")
    {
        goal_pub = this->create_publisher<geometry_msgs::msg::PoseStamped>("/goal_pose",10);
        timer_ = this->create_wall_timer(std::chrono::milliseconds(1000),
                                         std::bind(&goalNode::publishPoints, this));
        RCLCPP_INFO(this->get_logger(),"Node has been started");
        rclcpp::Time time = this->now();
    }


private:
    void publishPoints(){
        auto msg = geometry_msgs::msg::PoseStamped();
       //msg.header.stamp = time;
        msg.header.frame_id = "map";
        msg.pose.position.x = 3.5273448698503023;
        msg.pose.position.y = 0.9133635579860595;
        msg.pose.position.z = 0.0;

        msg.pose.orientation.x = 0.0;
        msg.pose.orientation.y = 0.0;
        msg.pose.orientation.z = -0.28452206059830654;
        msg.pose.orientation.w = 0.9586694931168372;

        goal_pub -> publish(msg);

    }



    rclcpp::Publisher<geometry_msgs::msg::PoseStamped>::SharedPtr goal_pub;
    rclcpp::TimerBase::SharedPtr timer_;
};


int main(int argc, char **argv){
    rclcpp::init(argc, argv);
    auto node = std::make_shared<goalNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;

}