from setuptools import setup

package_name = 'auto_turret'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='IoT User',
    maintainer_email='iot@raspberrypi.com',
    description='Arjuna Auto Turret ROS2 nodes',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'camera_node = auto_turret.camera_node:main',
            'detection_node = auto_turret.detection_node:main',
            'tracking_node = auto_turret.tracking_node:main',
            'turret_control_node = auto_turret.turret_control_node:main',
            'web_stream_node = auto_turret.web_stream_node:main',
        ],
    },
)
