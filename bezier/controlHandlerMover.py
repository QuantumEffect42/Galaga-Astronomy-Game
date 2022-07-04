from .controlPointQuartetCollection import ControlPointQuartetCollection
from .pathPointSelector import PathPointSelector
from .controlPointHandler import ControlPointHandler


class ControlHandlerMover():
    def __init__(self, controlPointQuartetCollection: ControlPointQuartetCollection, pathPointSelector: PathPointSelector):
        self.controlPointQuartetCollection = controlPointQuartetCollection
        self.pathpointSelector = pathPointSelector

    def moveControlHandler(self, controlPointHandler: ControlPointHandler, x : int, y : int):
        dx = self.controlPointQuartetCollection.getControlPoint(controlPointHandler).x - x
        dy = self.controlPointQuartetCollection.getControlPoint(controlPointHandler).y - y

        self.controlPointQuartetCollection.getControlPoint(controlPointHandler).x = x
        self.controlPointQuartetCollection.getControlPoint(controlPointHandler).y = y

        if self.pathpointSelector.isPathPoint(controlPointHandler):
            relatedPathPoint = self.pathpointSelector.findRelatedPathPoint(controlPointHandler)
            self.controlPointQuartetCollection.getControlPoint(relatedPathPoint).x = x
            self.controlPointQuartetCollection.getControlPoint(relatedPathPoint).y = y

            relatedControlPoints = self.pathpointSelector.findControlPointsOfPathPoint(controlPointHandler)
            self.controlPointQuartetCollection.getControlPoint(relatedControlPoints[0]).x -= dx
            self.controlPointQuartetCollection.getControlPoint(relatedControlPoints[0]).y -= dx
            self.controlPointQuartetCollection.getControlPoint(relatedControlPoints[1]).x -= dx
            self.controlPointQuartetCollection.getControlPoint(relatedControlPoints[1]).y -= dy

        else:
            relatedControlPoint = self.pathpointSelector.findRelatedControlPoint(controlPointHandler)
            relatedPathPoint = self.pathpointSelector.findPathPointOfControlPoint(controlPointHandler)

            xDist = self.controlPointQuartetCollection.getControlPoint(relatedPathPoint).x - x
            yDist = self.controlPointQuartetCollection.getControlPoint(relatedPathPoint).y - y

            self.controlPointQuartetCollection.getControlPoint(relatedControlPoint).x = self.controlPointQuartetCollection.getControlPoint(relatedPathPoint).x + xDist
            self.controlPointQuartetCollection.getControlPoint(relatedControlPoint).y = self.controlPointQuartetCollection.getControlPoint(relatedPathPoint).y + yDist

    def allignAll(self):
        for quartetIndex in range(self.controlPointQuartetCollection.numQuartets()):
            quartet = self.controlPointQuartetCollection.getQuartet(quartetIndex)
            for pointIndex in range(4):
                controlPointHandler = ControlPointHandler(quartetIndex, pointIndex)
                point = quartet.getPoint(pointIndex)
                self.moveControlHandler(controlPointHandler, point.x, point.y)