from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    """Launch all mock sensor nodes and the MQTT bridge."""
    return LaunchDescription([
        Node(
            package='mock_gps',
            executable='mock_gps',
            name='mock_gps',
            output='screen',
        ),
        Node(
            package='mock_system',
            executable='mock_system',
            name='mock_system',
            output='screen',
        ),
        Node(
            package='ros_mqtt_bridge',
            executable='ros_mqtt_bridge',
            name='ros_mqtt_bridge',
            output='screen',
        ),
    ])
