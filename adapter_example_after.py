#chcemy poprawic implementacje Rectangle.draw, 
#ale nie chcemy usuwac
#ani modyfikowac Rectangle.draw - dlaczego? (bo moga byc miejsca w kodzie ktore uzywaja starej implementacji Rectangle.draw  i nie chcemy tego zmieniac )

from abc import ABC, abstractmethod

class Line:
    
    def __init__(self, color):
        self.__color = color
        
    def draw(self, x1, y1, x2, y2):
        return f"Line from ({x1}, {y1}) to ({x2}, {y2})"
    
    
class Rectangle:
    
    def __init__(self, lineColor, backgroundColor):
        self.__lineColor = lineColor
        self.__backgroundColor = backgroundColor
        
    def draw(self, x1, y1, width, height):
        return f"Rectangle from ({x1}, {y1}). Width = {width} Height = {height})"
    
class Shape(ABC):
    
    @abstractmethod
    def draw(self, a, b, c, d):
        pass
    
class LinneAdapter(Shape):
    
    def __init__(self, line:Line):
        self.__line = line
        
    def draw(self, x1, y1, x2, y2):
        return self.__line.draw(x1, y1, x2, y2)
    
class RectangleAdapter(Shape):
    
    def __init__(self, rectangle:Rectangle):
        self.__rectangle = rectangle
        
    def draw(self, x1, y1, x2, y2):
        #ponizej znajdue sie przyklad adoptowania
        x = min(x1, x2)
        y = min(y1, y2)
        w = abs(x1 - x2)
        h = abs(y1 - y2)
        
        return self.__rectangle.draw(x, y, w, h)
    

def main():
    oldShapes = [Line("red"), Rectangle("black", "blue")]  
    
    newShapes = [LinneAdapter(oldShapes[0]), RectangleAdapter(oldShapes[1])]  
    
    x1 = 1.0
    y1 = 2.0
    x2 = 3.0
    y2 = 4.0
    
    for shape in newShapes:
        print(shape.draw(x1, y1, x2, y2))

if __name__ == "__main__":
   main()
   

