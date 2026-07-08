import sys
import argparse
import numpy as np

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, DurabilityPolicy, HistoryPolicy
from nav_msgs.msg import Path

from utils import *
from planner_wrapper import TomogramPlanner

sys.path.append('../')
from config import Config

parser = argparse.ArgumentParser()
parser.add_argument('--scene', type=str, default='Spiral', help='Name of the scene. Available: [\'Spiral\', \'Building\', \'Plaza\']')
args = parser.parse_args()

cfg = Config()

if args.scene == 'Spiral':
    tomo_file = 'spiral0.3_2'
    start_pos = np.array([-16.0, -6.0], dtype=np.float32)
    #end_pos = np.array([-26.0, -5.0], dtype=np.float32)
    end_pos = np.array([-35.0, -25.0], dtype=np.float32)
    start_layer = 0  # layer 0-4 for Spiral (5 layers total)
    end_layer = 3
elif args.scene == 'Building':
    tomo_file = 'building2_9'
    start_pos = np.array([5.0, 5.0], dtype=np.float32)
    end_pos = np.array([-6.0, -1.0], dtype=np.float32)
    start_layer = 0
    end_layer = 0
elif args.scene == 'Isaacsim':
    tomo_file = 'utlidar_test_downsampled'
    start_pos = np.array([-9.3, -20.7], dtype=np.float32)
    end_pos = np.array([-23.5, 23.7], dtype=np.float32)
    start_layer = 0
    end_layer = 0
elif args.scene == 'Openmind':
    tomo_file = 'scans_20260708_140737_ds37'
    start_pos = np.array([3.8, 6.9], dtype=np.float32)
    end_pos = np.array([1.1, -9.0], dtype=np.float32)
    start_layer = 5
    end_layer = 5
else:
    tomo_file = 'plaza3_10'
    start_pos = np.array([0.0, 0.0], dtype=np.float32)
    end_pos = np.array([23.0, 10.0], dtype=np.float32)
    start_layer = 0
    end_layer = 0


class PlannerNode(Node):
    def __init__(self):
        super().__init__('pct_planner')
        latched_qos = QoSProfile(
            depth=1,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
        )
        self.path_pub = self.create_publisher(Path, '/pct_path', latched_qos)
        self.planner = TomogramPlanner(cfg)

    def pct_plan(self):
        self.planner.loadTomogram(tomo_file)
        traj_3d = self.planner.plan(start_pos, end_pos, start_layer, end_layer)
        if traj_3d is not None:
            self.path_pub.publish(traj2ros(traj_3d))
            print("Trajectory published")


if __name__ == '__main__':
    rclpy.init()
    node = PlannerNode()
    node.pct_plan()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()