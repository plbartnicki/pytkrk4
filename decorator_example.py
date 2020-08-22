"""
Dekorator - wzorzec strukturalny

wrapper - kocepcja polegajaca na  rozszerzeniu
(opakowaniu) logiki pewnej klasy o dodatkowe 
elementy

Celem dekoratora jest rozszerzenie pewnej istniejace logiki (klasy albo funkcji) 
 o dodatkowe elementy (bez zmiany logiki rozszerzanej)

Dekorator jest przykladem zastosowania wrappera
"""
from datetime import datetime

def simple_logger_error(message:str):
    print(f"ERROR {message}")
    
def log_decorator(fun, message:str):
    def wrapper():
        print("------------------------")
        print("------", datetime.now(), "-------")
        fun(message)
        print("------------------------")
        
    return wrapper
    
def main():
    simple_logger_error("file doesn't exist\n")
    simple_logger_error("connection to DB failed\n")
    
    #chcemy wzbogacic zachowanie istniejacego logerra
    #(bez) zmiany kodu funkcji simple_logger_error
    decorated_function = log_decorator(simple_logger_error, "connection to DB failed" )
    decorated_function()
    
    
    
    
    
if __name__ == "__main__":
    main()
