from OverHeadTransportation import OverHeadTransportation as OHT


def start_unload(self):
    print("Custom Method start_unload")


OHT.start_unload = start_unload
