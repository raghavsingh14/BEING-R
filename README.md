# BEING-R

This is a Robotic project. BEING-R is termed as _**Biological Equivalent Intelligence Naive Generation - Rover**._ It is an autonomous rover which can perform various tasks which are biologically similiar to the Human Activities. These activities performed with the help of intelligence modules embedded in it.

**Hardwares Required:**
1.) Raspberry Pi 3B+: It is a Microprocessor(or Mini CPU).
2.) Arduino Nano: It is a Microcontroller which gives the commands to different sensors and actuator to perfrom various tasks.
3.) Raspberry Pi Camera: For detecting the obstacle and capturing pictures.
4.) BMP Sensor: For measuring the Pressure in sorroundings.
5.) LDR Sensor: For detecting light sources in the sorroundings.
6.) DHT11 Sensor: For measuring the tempreature.
7.) Actuator and Wheels: Helps in motion.
8.) 3-Wheeled Chassis: It is the base of our rover on which all the other hardwares will be implemented. 

**Information Regarding its Embedded Intelligence:**

This rover consist of five modules of Embedded Intelligence.

1.) _Light Intensity Detector_: It detects the light intensity from various sources. So that, it can consume sunlight to recharge its battery. This module is basically based on                                 the OpenCV technology. 

2.) _QR Code detection and decoding_: We use this concept so that decoding of QR Code help the rover to navigate the path using QR Codes. This module is also based on                                                 the OpenCV technology. 

3.) _Target Identification_: Main aim to implement this module is to identify the assigned target and able to reach to the target. This whole module follows the concept of YOLO                              algorithm (i.e., You Only Look Once) 

4.) _Obstacle Detection and Identification_ : It helps in detecting obstacles in between the paths and then they navigate themselves for the proper path.  

5.) _Weather Predictor_: It is an amazing module of this project which is based on the Naive Bayes as well as on Machine Learning. It helps in weather forecasting of last seven                          days which helps in analyzing the weather of next days and alert for reserving power.   

