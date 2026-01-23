from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    camera_node = Node(
        package='auto_turret',
        executable='camera_node',
        name='camera_node',
        output='screen',
        parameters=[
            {"cam_device": "/dev/video0"}
        ]
    )

    detection_node = Node(
        package='auto_turret',
        executable='detection_node',
        name='detection_node',
        output='screen'
    )

    tracking_node = Node(
        package='auto_turret',
        executable='tracking_node',
        name='tracking_node',
        output='screen'
    )

    turret_control_node = Node(
        package='auto_turret',
        executable='turret_control_node',
        name='turret_control_node',
        output='screen'
    )

    web_stream_node = Node(
        package='auto_turret',
        executable='web_stream_node',
        name='web_stream_node',
        output='screen'
    )

    return LaunchDescription([
        camera_node,
        detection_node,
        tracking_node,
        turret_control_node,
        web_stream_node
    ])
