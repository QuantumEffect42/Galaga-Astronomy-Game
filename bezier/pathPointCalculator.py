from .controlPointQuartet import ControlPointQuartet
from .pathPoint import PathPoint

class PathPointCalculator:
     @staticmethod
     def calculatePathPoint(controlPointQuartet : ControlPointQuartet, timeToCalculate: float):
         time: float = timeToCalculate - int(timeToCalculate)
         cx: float = 3.0 * (controlPointQuartet.getPoint(1).x - controlPointQuartet.getPoint(0).x)
         cy: float = 3.0 * (controlPointQuartet.getPoint(1).y - controlPointQuartet.getPoint(0).y)
         bx: float = 3.0 * (controlPointQuartet.getPoint(2).x - controlPointQuartet.getPoint(1).x) - cx
         by: float = 3.0 * (controlPointQuartet.getPoint(2).y - controlPointQuartet.getPoint(1).y) - cy
         ax: float = controlPointQuartet.getPoint(3).x - controlPointQuartet.getPoint(0).x - cx - bx
         ay: float = controlPointQuartet.getPoint(3).y - controlPointQuartet.getPoint(0).y - cy - by

         cube: float = time * time * time
         square: float = time * time

         resx: float = (ax * cube) + (bx * square) + (cx * time) + controlPointQuartet.getPoint(0).x
         resy: float = (ay * cube) + (by * square) + (cy * time) + controlPointQuartet.getPoint(0).y

         return PathPoint(resx, resy)