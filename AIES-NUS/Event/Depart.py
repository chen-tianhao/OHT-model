from OverHeadTransportation import OverHeadTransportation as OHT


def depart(self):
    print("Custom Method depart")


OHT.depart = depart
