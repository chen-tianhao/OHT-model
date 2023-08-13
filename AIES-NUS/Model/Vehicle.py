import Path
import PathMoverStatistics


class Phase:
    IDLE = 0
    LOADING = 1
    UNLOADING = 2
    RETRIEVE = 3
    TRANSPORT = 4
    IDLE_TRIP = 5


class Vehicle:

    def __init__(self):
        self.Id = ''
        self.initial_speed = 0
        self.current_speed = 0
        self.average_speed = 0
        self.current_phase = Phase.IDLE
        self.current_path = Path()
        self.next_path = Path()
        self.target_list = []
        self.path_mover_statictics = PathMoverStatistics()
        self.path_index = 0
        self.estimatedCompleteTime = 0
        self.idle = True
