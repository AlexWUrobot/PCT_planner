from .scene import ScenePCD, SceneMap, SceneTrav


class SceneOpenmind():
    pcd = ScenePCD()
    pcd.file_name = 'scans_20260708_140737_ds37.pcd'

    map = SceneMap()
    map.resolution = 0.30
    map.ground_h = -9.0
    map.slice_dh = 2.0

    trav = SceneTrav()
    trav.kernel_size = 3
    trav.interval_min = 0.25
    trav.interval_free = 0.35
    trav.slope_max = 0.70
    trav.step_max = 0.60
    trav.standable_ratio = 0.10
    trav.cost_barrier = 50.0
    trav.safe_margin = 0.15
    trav.inflation = 0.05
