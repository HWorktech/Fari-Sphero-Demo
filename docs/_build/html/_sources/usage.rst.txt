.. _usage:

Usage
=====

Launch the control software on the central computer. This can be done by following these steps:

1. Open 6 terminal windows on the central computer.
2. In the first terminal window, launch the ROS master node by entering the following command: `roscore`
3. In the second terminal window, launch the `multi_sphero_control.launch` file located in the `sphero_bolt_controller/launch` directory, by entering the following command: `roslaunch sphero_bolt_controller multi_sphero_control.launch`
    Note: Any lines in the `multi_sphero_control.launch` file corresponding to unused robots should be commented out to prevent unnecessary errors.
4. In the third terminal window, launch the arena by navigating to the directory where the MoCA arena package was downloaded and built.
5. In the remaining four terminal windows, connect to each Raspberry Pi device via SSH by entering the following command (assuming "raspberry1" is the hostname used when saving the static IP address of the Raspberry Pi device): `ssh raspberry1`. Enter the password that was defined during the installation process. If a different hostname was used, substitute it for "raspberry1" in the command, or use the following syntax to connect using the IP address directly: `ssh <username>@<raspberry_ip_address>`.
6. In each Raspberry Pi terminal window, navigate to the `sphero_bolt_driver/launch` directory within the project folder and execute the `multi_sphero_driver.launch` file by entering the following command: `roslaunch sphero_bolt_driver multi_sphero_driver.launch`
7. Once these steps are complete, the Sphero Bolt robots should be connected and waiting for a first shake to switch from Idle mode to random walking mode.