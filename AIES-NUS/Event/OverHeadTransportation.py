
class OverHeadTransportation:

    def arrive(self):
        print('Event: arrive')

    def assign_new_job(self):
        print('Event: assign_new_job')

    def travel_complete(self):
        print('Event: travel_complete')

    def depart(self):
        print('Event: depart')

    def idel(self):
        print('Event: idel')

    def push_idle_vehicle(self):
        print('Event: push_idle_vehicle')

    def ready_to_depart(self):
        print('Event: ready_to_depart')

    def request_to_arrive(self):
        print('Event: request_to_arrive')

    def start_load(self):
        print('Event: start_load')

    def start_unload(self):
        print('Event: start_unload')
