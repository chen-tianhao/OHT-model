from OverHeadTransportation import OverHeadTransportation as OHT


def request_to_arrive(self):
    print("Custom Method request_to_arrive")


OHT.request_to_arrive = request_to_arrive
