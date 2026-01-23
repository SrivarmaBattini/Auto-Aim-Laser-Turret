# __init__.py
#
# Marks this directory as a Python package.
# Optional: import classes/functions so they can be accessed as:
#   from auto_turret import DetectionNode
#   from auto_turret import TurretControlNode
#
# This is clean and minimal — recommended for ROS2 Python packages.

from .camera_node import CameraNode
from .detection_node import DetectionNode
from .tracking_node import TrackingNode
from .turret_control_node import TurretControlNode
from .web_stream_node import WebStreamNode

# Export Angles helper
from .Angles import turret as TurretAngles

__all__ = [
    "CameraNode",
    "DetectionNode",
    "TrackingNode",
    "TurretControlNode",
    "WebStreamNode",
    "TurretAngles",
]
