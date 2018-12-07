# ROS - Mitsubish Robotic Arm
ROS communnication with robot Mitsubish Melfa RV-2AJ 


### Commands to use ros_mitsubishi package


- Command to perform joint movement:
```
rosrun ros_mitsubishi JointMovementListener.py
``` 

- Command to perform cartesian movement:
```
rosrun ros_mitsubishi CartesianMovementListener.py
```

- Command to execute kinect xbox 360 package:
```
roslaunch freenect_launch freenect.launch
```

- Command to visualize one of many types of image that the freenect returns in topics:
```
rosrun image_view image_view image:=camera/rgb/image_color
```
