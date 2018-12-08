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

- Command to publish message to the cartesian movement topic:
```
rostopic pub /cartesianMovement ros_mitsubishi/CartesianMessage "{x: 0.0, y: 0.0, z: 0.0, a: 0.0, b: 0.0, speed: 0.0}"
```

- Command to publish message to the joint movement topic:
```
rostopic pub /jointMovement ros_mitsubishi/JointMessage "{j1: 0.0, j2: 0.0, j3: 0.0, j5: 0.0, j6: 0.0, speed: 0.0}"
```

- Command to execute kinect xbox 360 package:
```
roslaunch freenect_launch freenect.launch
```

- Command to visualize one of many types of image that the freenect returns in topics:
```
rosrun image_view image_view image:=camera/rgb/image_color
```
