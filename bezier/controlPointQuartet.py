from .controlPoint import ControlPoint

class ControlPointQuartet():
    def __init__(self, x0, y0, x1, y1, x2, y2, x3, y3):
        self.points = []
        self.points.append(ControlPoint(x0, y0))
        self.points.append(ControlPoint(x1, y1))
        self.points.append(ControlPoint(x2, y2))
        self.points.append(ControlPoint(x3, y3))

    def getPoint(self, pointIndex):
        return self.points[pointIndex]

    def length(self):
        return len(self.points)

    def isInControlPoint(self, x, y, rad):
        for point, index in enumerate(self.points):
            left = (point.x - x) * (point.x - x) + (point.y -y) * (point.y - y)

        if left < (rad * rad):
            return index, True

        return -1, False
