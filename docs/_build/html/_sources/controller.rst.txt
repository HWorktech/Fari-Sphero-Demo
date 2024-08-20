.. _controller:


Sphero Bolt Control Module
==========================

This module contains the scripts and launch files necessary for controlling the Sphero Bolt in various scenarios.

Launch Files
------------

The module contains the 2 launch files: 
- **launch/multi_sphero_control.launch**:
- **launch/single_sphero_control.launch**:

As the name suggest, the first launch file is used to launch control for multiple robots at the same time, by sequentially launching the single_sphero_control.launch file.

Scripts
-------
The module contains the following scripts:
- **scripts/sphero_bolt_control_node.py**: This script is the main script that is used to control the robots. The script is responsible for sending the appropriate commands to the robots based on their position and the mission. The script is also responsible for receiving the robots messages and to process them if needed.
- **scripts/sphero_arena_control_node.py**: This script is used to control the arena. The script is responsible for sending the appropriate commands to the arena based on the robots position and the mission. The script is also responsible for receiving the arena messages and to process them if needed.

API Documentation
-----------------

.. automodule:: sphero_bolt_control_node
   :members:
   :no-undoc-members:
   :show-inheritance:
   :no-value:

.. automodule:: sphero_arena_control_node
    :members:
    :undoc-members:
    :show-inheritance:
    :no-value:
