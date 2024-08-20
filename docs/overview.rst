.. _overview:   

Overview
========

Physicals Components
--------------------

the demonstration consist of the following components: 

- **Sphero bolt robots**: the robots used in the demonstration are Sphero bolt robots. These robots are small, spherical robots that can move in any direction. They are equipped with a variety of sensors and can be controlled using a smartphone or a computer. The robots are lightweight and durable, making them ideal for use in the demonstration. they can run this specific demonstration for an hour on a single charge. 
More details about the robots can be found in the `Sphero website <https://www.sphero.com/>`_. 


- **Computer**: the computer is needed to launch the demonstration and subjacent process. A fondamental concept in swarm robotics is the decentralization, meaning that each robot is autonomous and can make decisions independently without a central entity. However, in some case like ours, robots need to communicated with each other, but sphero bolt specificly does only has limited communication capabilities. Ultimately, the computer is used as a communication hub between the robots and the arena. Called "Master" in the code, the computer is responsible of receiving each robots messages, process if needed and send back the appropriate message to corresponding robots, all through the ROS framework.
Any ubuntu computer with ROS noetic installed can be used to run the demonstration. Optionally, they pc could need a bluetooth adapter to communicate with the robots.
More on configuration and installation can be found in the `installation <installation>`_ section.


- **Odroids**: the odroids are small computers that are used to control the robots. Sphero Bolt robots are not able to run code on their own, and their shape does not allow to add any additional hardware. Therefore a computer is needed to do the processing and send the appropriate commands to the robots. Since a bluetooth adapter can only handle 5 robots at the same time in a stable way, we use up to 3 odroids to control up to 15 robots.


- **Arena**: the arena is trapezoidal in shape and is made of 16 blocks and 4 corners. each block contains a led strip that can be controlled individually. the blocks are link together through magnets and wire. the arena is controller by an arduino board that is connected to a computer, and powered by a AC adapter block. 
More details about the arena, the materials needed and the assembly can be found in the `arena technical report <arena>`_.

- **Camera**: the camera is used to detect the robots and to track their position. the camera is connected to a computer through a ROS topicand is used to provide a live feed of the demonstration. The camera also served in the demonstration, to detect sufficient aggregated robots in a specific area since bolt robots are not equipped with a camera or any other sensors to detect the number of robots in a specific area.


Software Components
-------------------

The main software components associeted with this repository are just listed below and are described in more details in the corresponding sections.

- **Visualization**: A front end that displays the robots as drone in a Brussels replica 3D environment. The front end is use to visualize the mission and intereaction of robot and support the explanation of the demonstration to the audience.
More details about the visualization can be found in the `frontend github repository <loreipsum.com>`_.

- **Camera**: the camera is linked to an image recognition software that is able to detect the robots and to track their position. The camera publish on a ROS topic the position of al the robots detected. 
More details about the camera can be found in the `camera github repository <loreipsum.com>`_.

- **Arena**: the arena is not impact the robots mission, it is mainly used to provide a visual feedback of the robots behaviour to the audience. The master computer is responsible of launching the arena controller taht will managed the led strip of the arena through a ROS topic messages.

- **Controller**: the controller is the main package that is used to control the robots. The controller is responsible for sending the appropriate commands to the robots based on their position and the mission. The controller is also responsible for receiving the robots messages and to process them if needed.

- **Driver**: the driver is the package that is used to communicate with the robots. The driver is responsible for sending the appropriate commands to the robots and to receive their messages. The driver is also responsible for handling the communication between the robots and the master computer. the driver is based on an non official sphero bolt python library `spheroV2 <loreipsum.com>`_. Despite the impressive capabilities of this library, to have a satble working system, we had to make some modification to the library. More details about the driver can be found in the library fork: `repository <loreipsum.com>`_.
