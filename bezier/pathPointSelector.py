from .controlPointHandler import ControlPointHandler

class PathPointSelector():
    def __init__(self, controlPointQuartetCollection):
        self.controlPointQuartetCollection = controlPointQuartetCollection
        self.pathPointMapping = {}

    def createKey(self, quartetIndex, controlPointIndex):
        return f'Q{quartetIndex}/P/{controlPointIndex}'

    def isPathPoint(self, controlPointHandler: ControlPointHandler):
        if controlPointHandler.controlPointIndex == 0 or controlPointHandler.controlPointIndex == 3:
            return True
        return False

    def createPathPointMapping(self):
        nrQuartets = self.controlPointQuartetCollection.numQuartets()

        for index in range(nrQuartets):
            mappedFirstQuarteteIndex = 0
            if index == 0:
                mappedFirstQuarteteIndex = nrQuartets - 1
            else:
                mappedFirstQuarteteIndex = index - 1

            mappedLastQuartetIndex = 0
            if index < nrQuartets - 1:
                mappedLastQuartetIndex = index + 1
            else:
                mappedLastQuartetIndex = 0

            self.pathPointMapping[self.createKey(index, 0)] = ControlPointHandler(mappedFirstQuarteteIndex, 3)
            self.pathPointMapping[self.createKey(index, 3)] = ControlPointHandler(mappedLastQuartetIndex, 3)

    def findRelatedPathPoint(self, controlPointHandler : ControlPointHandler):
        if self.isPathPoint(controlPointHandler):
            key = self.createKey(controlPointHandler.quartetIndex, controlPointHandler.controlPointIndex)
            return self.pathPointMapping[key]
        else:
            print("error")
            exit(1)

    def findRelatedControlPoint(self, controlPointHandler : ControlPointHandler):
        relatedControlPoint = ControlPointHandler(-1, -1)
        lastQuartetIndex = self.controlPointQuartetCollection.numQuartets() - 1

        if controlPointHandler.controlPointIndex == 1:
            relatedControlPoint.controlPointIndex = 2
            if controlPointHandler.quartetIndex == 0:
                relatedControlPoint.quartetIndex = lastQuartetIndex
            elif controlPointHandler.quartetIndex > 0:
                relatedControlPoint.quartetIndex = controlPointHandler.quartetIndex - 1

        elif controlPointHandler.controlPointIndex == 2:
            relatedControlPoint.controlPointIndex = 1
            if controlPointHandler.quartetIndex < lastQuartetIndex:
                relatedControlPoint.quartetIndex = controlPointHandler.quartetIndex + 1
            else:
                relatedControlPoint.quartetIndex = 0

        return relatedControlPoint

    def getLastQuartetIndex(self):
        return self.controlPointQuartetCollection.numQuartets() - 1

    def getNumQuartets(self):
        return self.controlPointQuartetCollection.numQuartets()

    def findPathPointOfControlPoint(self, controlPointHandler: ControlPointHandler):
        relatedControlPoint = ControlPointHandler(-1, -1)

        if controlPointHandler.controlPointIndex == 1:
            relatedControlPoint.controlPointIndex = 0
        elif controlPointHandler.controlPointIndex == 2:
            relatedControlPoint.controlPointIndex = 3

        relatedControlPoint.quartetIndex = controlPointHandler.quartetIndex

        return relatedControlPoint

    def findControlPointsOfPathPoint(self, pathPointHandler: ControlPointHandler):
        relatedControlPoints = []
        numberOfQuartets = self.controlPointQuartetCollection.numQuartets
        lastQuartetIndex = numberOfQuartets - 1

        if pathPointHandler.controlPointIndex == 0:
            relatedControlPoints.append(ControlPointHandler(pathPointHandler.quartetIndex, 1))
            if pathPointHandler.quartetIndex == 0:
                relatedControlPoints.append(ControlPointHandler(lastQuartetIndex, 2))
            else:
                relatedControlPoints.append(ControlPointHandler(pathPointHandler.quartetIndex - 1, 2))

        elif pathPointHandler.controlPointIndex == 3:
            relatedControlPoints.append(ControlPointHandler(pathPointHandler.quartetIndex, 2))
            if pathPointHandler.quartetIndex == 0 and numberOfQuartets > 1:
                relatedControlPoints.append(ControlPointHandler(pathPointHandler.quartetIndex + 1, 1))
            else:
                if pathPointHandler.quartetIndex == lastQuartetIndex:
                    relatedControlPoints.append(ControlPointHandler(0, 1))
                else:
                    relatedControlPoints.append(ControlPointHandler(pathPointHandler.quartetIndex + 1, 1))

        else:
            print("error")
            exit(1)

        return relatedControlPoints

    def getControlPointPairs(self):
        lineList = []

        controlPoint1 = self.controlPointQuartetCollection.getControlPoint(ControlPointHandler(0, 1))
        lastQuartetIndex = self.getLastQuartetIndex()
        controlPoint2 = self.controlPointQuartetCollection.getControlPoint(ControlPointHandler(lastQuartetIndex, 2))
        lineList.append(((controlPoint1.x, controlPoint2.y), (controlPoint2.x, controlPoint2.y)))

        if self.getNumQuartets() > 1:
            for index in range(lastQuartetIndex):
                controlPoint1 = self.controlPointQuartetCollection.getControlPoint(ControlPointHandler(index, 2))
                controlPoint2 = self.controlPointQuartetCollection.getControlPoint(ControlPointHandler(index + 1, 1))
                lineList.append(((controlPoint1.x, controlPoint1.y), (controlPoint2.x, controlPoint2.y)))

        return lineList
