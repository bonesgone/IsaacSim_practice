import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/roboticsinnovatorytim/isaac_tutorial/examples/sim/IsaacSim-ros_workspaces/humble_ws/install/isaac_ros_navigation_goal'
