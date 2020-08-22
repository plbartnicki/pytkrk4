
"""
Adapter  - wzorzec strukturalny
Celem jest adaptacja istniejacych interfejsow
z nowym podejsciem

przed zastosowaniem wzorca:
"""

class Line:
    
    def __init__(self, color):
        self.__color = color
        
    def draw(self, x1, y1, x2, y2):
        return f"Line from ({x1}, {y1}) to ({x2}, {y2})";
    
    
class Rectangle:
    
    def __init__(self, lineColor, backgroundColor):
        self.__lineColor = lineColor
        self.__backgroundColor = backgroundColor
        
    def draw(self, x1, y1, width, height):
        return f"Rectangle from ({x1}, {y1}). Width = {width} Height = {height})";


def main():
    shapes = [Line("red"), Rectangle("black", "blue")]  
    
    x1 = 1.0
    y1 = 2.0
    x2 = 3.0
    y2 = 4.0
    
    width = 100
    height = 500
    
    for shape in shapes:
        if type(shape) == Line:
            print(shape.draw(x1,y1,x2,y2))
        elif type(shape) == Rectangle:
            print(shape.draw(x1,y1,width,height))
        #gdybysmy dodali kolejna figure (np. clas Triangle) to 
        #trzeba by bylo we wszystkich podobnych miejscach w kodzie
            #gdzie badamy typ obiektu, rozwazyc kolejny typ
    
#zadanie:
# Jakie błedy popełniono w projekcie klas?
# Jakie są wady takiego rozwiązania?
            
            

if __name__ == "__main__":
   main()