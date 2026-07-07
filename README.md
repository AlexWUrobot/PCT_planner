# PCT Planner

## Overview

This is an implementation of paper **Efficient Global Navigational Planning in 3-D Structures Based on Point Cloud Tomography** (accepted by TMECH).
It provides a highly efficient and extensible global navigation framework based on a tomographic understanding of the environment to navigate ground robots in multi-layer structures.

**Demonstrations**: [pct_planner](https://byangw.github.io/projects/tmech2024/)

![demo](rsc/docs/demo.png)

## Citing

If you use PCT Planner, please cite the following paper:

[Efficient Global Navigational Planning in 3-D Structures Based on Point Cloud Tomography](https://ieeexplore.ieee.org/document/10531813)

```bibtex
@ARTICLE{yang2024efficient,
  author={Yang, Bowen and Cheng, Jie and Xue, Bohuan and Jiao, Jianhao and Liu, Ming},
  journal={IEEE/ASME Transactions on Mechatronics}, 
  title={Efficient Global Navigational Planning in 3-D Structures Based on Point Cloud Tomography}, 
  year={2024},
  volume={},
  number={},
  pages={1-12}
}
```

## Prerequisites

### Environment

- Ubuntu >= 20.04
- ROS2 Humble with desktop-full installation (`ros-humble-desktop`)
- CUDA >= 11.7

### Python

- Python >= 3.10 (bundled with Ubuntu 22.04)
- [CuPy](https://docs.cupy.dev/en/stable/install.html) matching your CUDA version
- Open3d

## Setup

### 1. Source ROS2 Humble

Add this to your `~/.bashrc` (run once):

```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

### 2. Create Virtual Environment

ROS2 Humble requires **Python 3.10**. The venv must use `--system-site-packages` so that ROS2 Python packages (`rclpy`, `sensor_msgs_py`, etc.) remain accessible:

```bash
python3.10 -m venv pct_env --system-site-packages
source pct_env/bin/activate
```

To activate the environment in future sessions:

```bash
source pct_env/bin/activate
```

### 3. Install Python Dependencies

```bash
pip install open3d numpy
# Install CuPy matching your CUDA version (check with: nvidia-smi)
# CUDA 12.x:
# pip install cupy-cuda12x
# CUDA 13.x:
pip install cupy-cuda13x
```

## Build & Install

Inside the package, there are two modules: the point cloud tomography module for tomogram reconstruction (in **tomography/**) and the planner module for path planning and optimization (in **planner/**).
You only need to build the planner module before use.
In **planner/**, run **build_thirdparty.sh** first and then run **build.sh**. 

```bash
cd planner/
./build_thirdparty.sh
./build.sh
```

## Run Examples

Three example scenarios are provided: **"Spiral"**, **"Building"**, and **"Plaza"**.
- **"Spiral"**: A spiral overpass scenario released in the [3D2M planner](https://github.com/ZJU-FAST-Lab/3D2M-planner).
- **"Building"**: A multi-layer indoor scenario with various stairs, slopes, overhangs and obstacles.
- **"Plaza"**: A complex outdoor plaza for repeated trajectory generation evaluation.

### Tomogram Construction

To plan in a scenario, first you need to construct the scene tomogram using the pcd file.
- Unzip the pcd files in **rsc/pcd/pcd_files.zip** to **rsc/pcd/**.
- For scene **"Spiral"**, you can download the pcd file from [3D2M planner spiral0.3_2.pcd](https://github.com/ZJU-FAST-Lab/3D2M-planner/tree/main/planner/src/read_pcd/PCDFiles).
- Start **RViz2** with the provided config:

```bash
rviz2 -d rsc/rviz/pct_ros.rviz
```

- Activate your virtual environment and, in **tomography/scripts/**, run **tomography.py** with the **--scene** argument:

```bash
source pct_env/bin/activate
cd tomography/scripts/
python3 tomography.py --scene Spiral
```

- The generated tomogram is visualized as ROS2 PointCloud2 message in RViz2 and saved in **rsc/tomogram/**.

### Trajectory Generation 

After the tomogram is constructed, you can run the trajectory generation example.
- In **planner/scripts/**, run **plan.py** with the **--scene** argument:

```bash
source pct_env/bin/activate
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/YOUR/DIRECTORY/TO/PCT_planner/planner/lib/3rdparty/gtsam-4.1.1/install/lib
cd planner/scripts/
python3 plan.py --scene Spiral
```

- The generated trajectory is visualized as ROS2 Path message in RViz2.

## License

The source code is released under [GPLv2](http://www.gnu.org/licenses/) license.

For commercial use, please contact Bowen Yang [byangar@connect.ust.hk](mailto:byangar@connect.ust.hk).




In termianl 1

~/PCT_planner$ source ~/.bashrc
source /home/lifan/PCT_planner/pct_env/bin/activate
cd /home/lifan/PCT_planner/tomography/scripts
python3 tomography.py --scene Spiral


In termianl 2

~/PCT_planner$ rviz2 -d rsc/rviz/pct_ros.rviz
