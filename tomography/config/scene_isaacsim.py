from .scene import ScenePCD, SceneMap, SceneTrav


class SceneIsaacsim():
    pcd = ScenePCD()
    pcd.file_name = 'utlidar_test_downsampled.pcd'

    map = SceneMap()
    map.resolution = 0.20
    map.ground_h = -0.5
    map.slice_dh = 1.0

    trav = SceneTrav()
    trav.kernel_size = 3
    trav.interval_min = 0.40
    trav.interval_free = 0.50
    trav.slope_max = 0.50
    trav.step_max = 0.40
    trav.standable_ratio = 0.20
    trav.cost_barrier = 50.0
    trav.safe_margin = 0.2
    trav.inflation = 0.1
