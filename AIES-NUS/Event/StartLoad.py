from OverHeadTransportation import OverHeadTransportation as OHT


def start_load(self):
    print("Custom Method start_load")


OHT.start_load = start_load
