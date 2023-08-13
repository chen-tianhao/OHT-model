import ControlPoint
import System


class Path:

    def __init__(self):
        self.start_point = ControlPoint()
        self.end_point = ControlPoint()
        self.length = 0
        self.total_capacity = self.length / (System.vehicle_length + System.safety_distance)
        self.remainingCapacity = self.total_capacity
        self.number_of_lane = 1
        self.go_through_time_stamp = 0
        self.enter_time_stamp = 0
        self.out_pending_list = []
        self.in_pending_list = []
        self.on_path_list = []
