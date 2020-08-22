""" template method == abstract method 
wzorzec behawioralny/czynnosciowy - dotyczy pewnej dynamiki

Wzorzec zawiera w klasie abstrakcyjnej, w pewnej metodzie 
wspolna logike (np. log_in)
dla wszystkich klas pochodnych oraz dodatkowo ukonkretnia 
tę metodę o pewną implementację

Istnieje zwiazek pomiedzy zachowaniem klasy abstr.
oraz klasy pochodnej
 """

from abc import ABC, abstractmethod

class DataMigrator(ABC):

    def start(self, source_path, target_path):
        self.__log_in()
        
        #zakladajac ze autoryzacja przebiegla poprawnie
        #wywolujemy pewną implementacje ponizszej metody
        self.migrate_data(source_path, target_path)
        
    def __log_in(self):
        print("login in progress..")
        print("Logged")

    @abstractmethod
    def migrate_data(self, source_path, target_path):
        pass
    
class DataMigrationFromFileToDatabase(DataMigrator):
    
    def migrate_data(self, source_path, connection_string):
        print(f"Started data migration from file {source_path} to database {connection_string}");
    
class DataMigrationFromFileToFile(DataMigrator):
    
    def migrate_data(self, source_path, target_path):
        print(f"Started data migration from file {source_path} to database {target_path}");
    
def main():
    migrator1 = DataMigrationFromFileToFile()     
    migrator1.start("c:\source.txt", "d:\target.txt")
        
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    