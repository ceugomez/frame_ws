#!/bin/bash
# cgf cego6160@colorado.edu  11.22.23
# overwrite stock depth_cam model for FRAME sim
cp -r gazebo_env/models/sf45b ~/.gazebo/models/
cp gazebo_env/iris_depth_camera.sdf src/PX4-Autopilot-Frame/Tools/simulation/gazebo-classic/sitl_gazebo-classic/models/iris_depth_camera/
