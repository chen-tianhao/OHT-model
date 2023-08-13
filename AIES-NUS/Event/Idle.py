from OverHeadTransportation import OverHeadTransportation as OHT


def idle(self):
    print("Custom Method idle")


OHT.idle = idle
