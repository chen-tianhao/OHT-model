from OverHeadTransportation import OverHeadTransportation as OHT


def arrive(self):
    print("Custom Method arrive")


OHT.arrive = arrive
