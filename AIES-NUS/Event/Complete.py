from OverHeadTransportation import OverHeadTransportation as OHT


def travel_complete(self):
    print("Custom Method travel_complete")


OHT.travel_complete = travel_complete
