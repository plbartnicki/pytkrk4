# -*- coding: utf-8 -*-
"""
Builder - stosujemy w przypadku konstrukcji
bardzo zlozonych obiektow

Celem wzorca jest separacja reprezentacji obiektu (model)
od jego konstrukcji (Budowniczy)
"""
from abc import ABC, abstractmethod

#skomplikowany obiekt
class Plane:
    def __init__(self):
        self.__engines = list()
        self.__wing1 = None
        self.__wing2 = None
        self.__hull = None
    
    def set_engines(self, engines):
        self.__engines = engines
        
    def set_hull(self, hull):
        self.__hull = hull
        
    def set_wing1(self, wing):
        self.__wing1 = wing
        
    def set_wing2(self, wing):
        self.__wing2 = wing
    
        
    def get_info(self):
        return f"Wing1: {self.__wing1.get_info()}  number of engines: {len(self.__engines)}"
    
class Engine:
    def __init__(self, power, v):
        self.__power = power
        self.__v = v
        
    def get_info(self):
        return f"power:  {self.__power}  v:  {self.__v}";
    
class Wing:
    def __init__(self, length):
        self.__length = length
        
    def get_info(self):
        return f"length: {self.__length}"
    
class Hull:
    def __init__(self, number_of_seats):
        self.number_of_seats = number_of_seats
        
    def get_info(self):
        return "number of seats: {self.number_of_seats}";
    
#zrobic klase abstr
class Builder(ABC):
    @abstractmethod
    def create_engines(self):
        pass
    
    @abstractmethod
    def create_wings(self):
        pass
    
    @abstractmethod
    def create_hull(self):
        pass
    
class SmallPlaneBuilder(Builder):
    def create_engines(self):
        engines = list()
        engines.append(Engine(2000, 1000))
        engines.append(Engine(2000, 1000))
        return engines
    
    def create_wings(self):
        wings = list()
        wings.append(Wing(20))
        wings.append(Wing(20))
        return wings
    
    def create_hull(self):
        return Hull(30)
    
class MilitaryPlaneBuilder(Builder):
    def create_engines(self):
        engines = list()
        engines.append(Engine(2000, 1000))
        engines.append(Engine(2000, 1000))
        engines.append(Engine(2000, 1000))
        engines.append(Engine(2000, 1000))
        return engines
    
    def create_wings(self):
        wings = list()
        wings.append(Wing(30))
        wings.append(Wing(30))
        return wings
    
    def create_hull(self):
        return Hull(30)

#ta klasa sluzy do produkowania roznych samolotow
class Producer:
    #producent samalotu jest w relacji ze sposobem budowania (z builderem)
    __builder = None
    
    def set_builder(self, builder):
        self.__builder = builder
       
    def produce_small_plane(self):
        plane = Plane();  #szkielet samolotu
    
        #nakazujemy builderowi wyprodukowanie czesci
        engines = self.__builder.create_engines()
        wings = self.__builder.create_wings()
        hull = self.__builder.create_hull()
       
        plane.set_engines(engines)
        plane.set_wing1(wings[0])
        plane.set_wing2(wings[1])
        plane.set_hull(hull)
       
        return plane

def main():
    smallPlaneBuilder = SmallPlaneBuilder()
    producer = Producer()
    producer.set_builder(smallPlaneBuilder)
    plane = producer.produce_small_plane()
    print(plane.get_info())
    
if __name__ == "__main__":
   main()

#zadanie - modyfikacja - dodaj kolejny komponent oraz inny sposob budowania
   
   
   
   
   
   
   

