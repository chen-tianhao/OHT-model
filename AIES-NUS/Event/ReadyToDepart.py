from OverHeadTransportation import OverHeadTransportation as OHT


def ready_to_depart(self):
    print("Custom Method ready_to_depart")


OHT.ready_to_depart = ready_to_depart
