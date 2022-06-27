from .controlPointQuartet import ControlPointQuartet
from .controlPointHandler import ControlPointHandler

class ControlPointQuartetCollection():
    def __init__(self):
        self.controlPointQuartets = []

    def add(self, controlPointQuartet : ControlPointQuartet):
        self.controlPointQuartets.append(controlPointQuartet)

    def numQuartets(self):
        return len(self.controlPointQuartets)

    def getQuartet(self, index):
        return self.controlPointQuartets[index]

    def getQuartetFromTime(self, time: float):
        return self.controlPointQuartets[int(time)]

    def givePositionIsInsideControlPoint(self, x, y, image_width):
        for quartetIndex in range(len(self.controlPointQuartets)):
            result = self.controlPointQuartets[quartetIndex].isInControlPoint(x, y, image_width)
            if result[0]:
                return quartetIndex, result[1], True

        return -1, -1, False

    def getControlPoint(self, controlPointHandler : ControlPointHandler):
        index = controlPointHandler.quartetIndex
        controlPointIndex = controlPointHandler.controlPointIndex
        return self.controlPointQuartets[index].points[controlPointIndex]

    def saveControlPoints(self):
        with open('controlPoints.txt', w) as file:
            for quartet in self.controlPointQuartets:
                file.write('\n  controlPointQuartetCollection.add(ControlPointQuartet(')
                for index,  point in enumerate(quartet.points):
                    if index == 3:
                        file.write(f'\n     {point.x}, {point.y}')
                    else:
                        file.write(f'\n    {point.x}, {point.y},')
                file.write('))')