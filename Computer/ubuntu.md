# I. Ubuntu 18.04.2 LTS (Bionic Beaver)

## i. Install Nvidia Driver
```
$ sudo apt-get purge nvidia*
$ sudo add-apt-reository ppa:graphcs-drivers
$ sudo apt-get update
$ sudo apt-get install screen
$ screen
$ sudo apt-get install nvidia-390
$ sudo reboot
$ lsmod | grep nvidia
$ nvidia-smi
$ dpkg -L nvidia-driver-390
```
Reference: https://www.mvps.net/docs/install-nvidia-drivers-ubuntu-18-04-lts-bionic-beaver-linux/

# II. Ubuntu 16.04.6 LTS (Xenial Xerus)

# III. Ubuntu 14.04.6 LTS (Trusty Tahr)

## i. Install ROS Indigo
```
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
$ sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net --recv-key 0xB01FA116
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install ros-indigo-desktop-full
```
### If error occurs
```
$ sudo apt-get install libsdformat1
$ sudo rosdep init
$ rosdep update
$ echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc
$ sudo apt-get install python-rosinstall
```
### Initialize work space
```
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/src
$ catkin_init_workspace
```
### Test catkin make
```
$ cd ~/catkin_ws/
$ catkin_make
```
### Test ROS
```
$ roscore
```
Reference: https://dnddnjs.gitbooks.io/drone-autonomous-flight/content/ubuntuc5d0_ros_indigo_c124_ce58.html

## ii. Setting Gazebo simulation and SDKs
### Make test work space, package
```
$ mkdir ~/test_ws/src
$ cd ~/test_ws/src
$ catkin_create_pkg test_pkg std_msgs rospy roscpp
$ git clone https://github.com/AutonomyLab/ardrone_autonomy.git
$ git clone https://github.com/occomco/tum_simulator.git
$ cd ~/test_ws
$ rosdep install —from-paths src —ignore-src —rosdistro indigo -y
$ catkin_make
$ source devel/setup.bash
$ rospack depends test_pkg
```
### Put/Edit code in test_pkg
```
$ nano test.py
$ ctrl + x
$ y
$ chmod +x test.py
```
Reference: https://www.youtube.com/watch?v=zwTnY-ZqNcM
Reference: https://github.com/amroygaol/AR_Drone_Example_code

## iii. Execute simulation and code
### Terminal 1
```
$ roscore
```
### Terminal 2
```
$ cd ~/test_ws
$ roslaunch cvg_sim_gazebo ardrone_testworld.launch
```
### Terminal 3
```
$ cd ~/test_ws
$ rosrun test_pkg test.py
```
