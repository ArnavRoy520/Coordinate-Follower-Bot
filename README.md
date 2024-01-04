# Coordinate-Follower-Bot

CONCEPT OF THE ROBOT :

The Coordinate Following Robot uses image processing to reach the target location by taking the shortest path as per the location provided on the screen. We mainly make the use of Aruco Marker to achieve this. Software - Hardware interface is achieved by feeding live video of the surroundings to the software in which the required location is clicked which is then converted into coordinates by using software and then a command is sent to the robot to move the target location. The purpose is achieved by using various Hardware and Software components which are further described later.

Hardware Used:

The Hardware Components used in making of the robot are :

Camera - The Camera is a sensor component which is used to capture surroundings of the bot which is to be further processed for relative position estimation.

Motors - They comprise the Actuator part of the robot which helps in achieving movement and helps in manipulating its position and orientation.
Arduino UNO - We make use of the microprocessor namely Arduino UNO which essentially takes input from the sensors ,corrects it and controls the actuators so that the required result is obtained.

Batteries - They are the most basic components which provide power to sensors, actuators and microprocessor.

Aruco Marker – They are 2D encoded binary fiducial patterns designed to be quickly detected by Computer vision systems.

Software Used:

The Software mainly used are :

Python - It is a programming language which plays a crucial role in processing the live feed as it converts the clicked location to coordinates and changes the relative position in real time. This is achieved by using python libraries such as:

 OpenCV - It is a library which uses computer vision to achieve tasks like image capturing, color conversion. it helps us by taking input of the surroundings of robot for relative estimation of the desired location with respect to the current location of the robot.
 Numpy - It is a library which helps in complex mathematical calculations. It helps in faster processing of coordinate estimation by calculating the shortest distance between the current location and target location.
 Pyserial - It is a library which helps in serial communication between the Control System and python which is necessary for moving to the desired location.
Arduino IDE - This is a programming language which is used to program the Control systems by defining its working. It mainly tells the Microprocessor on how it should perform different actions on different commands.


Skills Used:

Image Processing

Mathematical logic Programming

Arduino Programming


Application :

The coordinate following robot has many real-world applications.

Coordinate following robot can play a very significant role in manufacturing industries. They can help in moving and transporting materials between warehouses in a very specific and precise manner as they are best used for more repeated movements.


The robot can also be used for delivery and Transport. As they can work in a very precise manner, we can automate the process of delivery and Transportation without compromising on accuracy and safety.

They can also be used in Military operations for surveillance of certain locations which are difficult to monitor like military checkpoints in high altitudes.

Future Developments:

We can further make it wireless by using other IOT components like Raspberry pi or making use of Wifi and Bluetooth modules for communication.
The coordinate following robot can be made more useful if we implement it to aerial systems. It can be used for several other operations like Crop Quality analysis and Regulating the usage of Pesticides.
Implementation of Swarm intelligence can make the coordinate following bot a more ready for industrial usage. Swarm intelligence makes use of complex AI and ML algorithms which makes the robot mimic an the collective behavior of social organisms like ants and uses this to its advantage to solve complex problems.

We can also implement Machine learning and fuzzy logic to the robot and train it such a way that it performs different actions on detecting different aruco markers.



https://github.com/ArnavRoy520/Coordinate-Follower-Bot/assets/143030580/97e4fda1-dec7-46a4-a568-34c8c739f3a8

