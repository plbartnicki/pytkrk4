

from datetime import datetime

class Logger:
    
    def __current_date_and_time(self):
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    def log_error(self, message):
        dateAndTime = self.__current_date_and_time()
        print(f"ERROR {dateAndTime} {message}")
        
    def log_debug(self, message):
        dateAndTime = self.__current_date_and_time()
        print(f"DEBUG {dateAndTime} {message}")
        
    def log_info(self, message):
        dateAndTime = self.__current_date_and_time()
        print(f"INFO {dateAndTime} {message}")
        
#wada tego rozwiazania jest to ze mozna zrobic kolejna
#(niepotrzebna) instancje tej klasy
l1 = Logger()
l1.log_info("data migration has been completed")
l2 = Logger()

print(l1)
print(l2)

"""
Singleton - wzorzec kreacyjny

Cel: z pewnych powodow (np. oszczednsc pamieci RAM) nie chceby aby istniala > 1 instancja danej klasy

Uwaga!
Ponizszy przyklad implementacji Singletona
dotyczy sytuacji gdy wiemy ze instancji
tej klasy (singletona) nie będą inicjalizowały wątki
"""

class NoSingleObjectException(Exception):
    pass

class SimpleLogger:
    #informacja czy zostal juz zrobiony obiekt tej klasy
    __instance = None
    
    def __init__(self):
        #jesli ktos zrobil juz obiekt tej klasy to
        #rzucamy wyjatek
        if SimpleLogger.__instance != None:
            raise NoSingleObjectException
        else:
            SimpleLogger.__instance = self
            
    @staticmethod
    def get_instance():
        if SimpleLogger.__instance == None:
            SimpleLogger()
        
        return SimpleLogger.__instance
    
    def __current_date_and_time(self):
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    def log_error(self, message):
        dateAndTime = self.__current_date_and_time()
        print(f"ERROR {dateAndTime} {message}")
        
    def log_debug(self, message):
        dateAndTime = self.__current_date_and_time()
        print(f"DEBUG {dateAndTime} {message}")
        
    def log_info(self, message):
        dateAndTime = self.__current_date_and_time()
        print(f"INFO {dateAndTime} {message}")

#za pomoca ponizszej metody powinnsmy uzyskiwac
#reference na obiekt

logger1 = SimpleLogger.get_instance()
logger2 = SimpleLogger.get_instance()
logger3 = SimpleLogger.get_instance()
logger1.log_error("connection failed")

print(logger1)
print(logger2)
print(logger3)

try:
    lg2 = SimpleLogger()
except NoSingleObjectException:
    print("You can create only one instance of SimpleLogger")
    

        
        

