
"""
Zadanie 1
Napisz funkcję read_from_files(filePaths)
której argumentem jest lista nazw/scieżek plików
Funkcja powinna zwrócić konkatenację zawartosci wszystkich plikowNastepnie udekoruj 
 tę funkcję (definiujac kolejna funkcje np. o nazwie file_reader_decorator)
W taki sposob że zwraca tekst będacy wynikiem nastepujacej konkatenacji:
    najpierw dowolny komunikat ktory jest argumentem/parametrem file_reader_decorator
    nastepnie komunikat: Reading from files has been started
    nastepnie konkatenacja zawartosci wczytanych plikow
    i na koncu komunikat Reading from files has been completed
    
    Zaleta dekoratora jest jego generycznosc oraz to 
    ze nie trzeba zmieniac dekorowanej funkcji woraz ielu miejsc w kodzie w ktorych
    w kotrych jest wywolywana dekorowana funkcja
"""

def read_from_files(filePaths):
    contents = ""
    for fp in filePaths:
        file = open(fp, "r")
        contents = contents + file.read() + "\n";
        file.close()
        
    return contents

def file_reader_decorator(fun, additionalMessage, filePaths):
    def wrapper():
        result = (additionalMessage
                  + "\nReading from files has been started\n"
                  + fun(filePaths)
                  + "Reading from files has been completed")
        return result
    
    return wrapper;
    

    
    
    
def main():
    print(read_from_files(["test1.txt", "test2.txt"]))
    cont = file_reader_decorator(read_from_files, "BEGIN", ["test1.txt", "test2.txt"])
    print(cont())
    
if __name__ == "__main__":
    main()

