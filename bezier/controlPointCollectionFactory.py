from .controlPointQuartet import ControlPointQuartet
from .controlPointQuartetCollection import ControlPointQuartetCollection

class ControlPointCollectionFactory:

    @staticmethod
    def createCollection1():
        controlPointQuartetCollection = ControlPointQuartetCollection()

        controlPointQuartetCollection.add(ControlPointQuartet(513, -15, 700, 151, 888, 650, 501, 648))
        controlPointQuartetCollection.add(ControlPointQuartet(501, 648, 114, 646, 208, 488, 235, 343))
        controlPointQuartetCollection.add(ControlPointQuartet(235, 343, 262, 198, 326, -181, 513, -15))

        return controlPointQuartetCollection

    @staticmethod
    def createCollection2():
        controlPointQuartetCollection = ControlPointQuartetCollection()

        controlPointQuartetCollection.add(ControlPointQuartet(513, -15, 430, 649, 420, 388, 525, 654))
        controlPointQuartetCollection.add(ControlPointQuartet(516, 654, 828, 649, 420, 388, 525, 375))
        controlPointQuartetCollection.add(ControlPointQuartet(525, 375, 630, 362, 596, -41, 513, -15))

        return controlPointQuartetCollection

    @staticmethod
    def createCollection3():
        controlPointQuartetCollection = ControlPointQuartetCollection()

        controlPointQuartetCollection.add(ControlPointQuartet(513, -15, 365, 16, 663, 556, 516, 654))
        controlPointQuartetCollection.add(ControlPointQuartet(516, 654, 269, 652, 476, 535, 528, 393))
        controlPointQuartetCollection.add(ControlPointQuartet(528, 393, 480, 251, 461, 14, 513, -15))

        return controlPointQuartetCollection

    @staticmethod
    def createCollection4():
        controlPointQuartetCollection = ControlPointQuartetCollection()

        controlPointQuartetCollection.add(ControlPointQuartet(513, -15, 330, 11, 204, 659, 516, 654))
        controlPointQuartetCollection.add(ControlPointQuartet(516, 654, 528, 649, 220, 388, 525, 375))
        controlPointQuartetCollection.add(ControlPointQuartet(525, 375, 530, 362, 396, -41, 513, -15))

        return controlPointQuartetCollection