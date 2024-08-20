.. _installation:

Installation
============

The installation below describes the steps to install THe Controller and the driver on the central computer and the Odroids. The installations of the other components are described in their respective technical reports and github repositories, see the `overview <overview>`_ for more details.

Requirements
------------

You will need the following:

Ubuntu 20.04 Focal Fossa installed on the central computer and each Odroid ( or Raspberry Pi) device.

ROS Noetic installed on the central computer and each Raspberry Pi device.

Python libraries: spherov2.py, bleak

Installation & Setup
--------------------

Installing Ubuntu 20.04 Focal Fossa on the PC and each raspberry pi: Detailed instructions and troubleshooting on: https://phoenixnap.com/kb/install-ubuntu-20-04 For the Raspberry Pi, you can use the Raspberry Pi Imager software to flash the SD card. Detailed instructions and troubleshooting on: https://www.yodeck.com/docs/how-to-articles/how-to-flash-an-sd-card-using-pi-imager/

Installing Python 3.x: • Open a terminal window on the Ubuntu computer • Run the following command to update the package list: sudo apt-get update • Run the following command to install Python 3.x: sudo apt-get install python3

Installing ROS Noetic: • Open a terminal window on the Ubuntu computer • Follow the instructions on the official ROS Noetic installation guide: http://wiki.ros.org/noetic/Installation/Ubuntu

Installing this package: • Clone this project repository containing the controller software and the driver. • Open a terminal window and navigate to the spherov2.py folder in the package directory • Run the following command to get the submodule spherov2.py : git submodule update --init --recursive • Install the spherov2 dependencies, specifically bleak with: pip install bleak

Setting Up the Raspberry Pi: • Install Ubuntu 20.04 Focal Fossa on each Raspberry Pi (following the steps in subsections 1) • Install Python 3.x and ROS Noetic on each Raspberry Pi (following the steps in subsections 2 and 3) • Clone the driver and controller software (following the steps in subsection 4)