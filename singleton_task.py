# -*- coding: utf-8 -*-
"""
Zadanie 2
Napisz klase User(login, address, password, logged) oraz implementacje singletona dla klasy (dobierz dobra nazwe)
 ktora pozwala na autentykacje uzytkownikow
Klasa powinna posiadac metody: add_user(user:User), login(login, password),   logout(login).
"""

class User:
    def __init__(self, login, address, password):
        self.__login = login
        self.__address = address
        self.__password = password
        self.__logged = False
        
    def get_login(self):
        return self.__login
    
    def get_password(self):
        return self.__password
    
    def log_in(self):
        self.__logged = True
        
    def log_out(self):
        self.__logged = False
    
class NonSingleObjectException(Exception):
    pass

class UserManager:
    #zawieranie obiektu w klasie - agregacja
    __users = dict()
    __instance = None
    
    def add_user(self, login, address, password):
        self.__users[login] = User(login, address, password)
        
    def log_in(self, login, password):
        if not login in self.__users:
            return False
        
        user = self.__users[login]
        
        if user != None and user.get_password() == password:
            self.__users[login].log_in()
            return True
        
        return False
            
    @staticmethod
    def get_instance():
        if UserManager.__instance == None:
            UserManager()
        
        return UserManager.__instance
    
    #tego konstruktora praktycznie nie wykonuje sie dla klasy Singletona
    def __init__(self):
        if UserManager.__instance != None:
            raise NonSingleObjectException
        else:
            UserManager.__instance = self
            
um = UserManager()
um.add_user("ala", "zielona 1", "123")

print(um.log_in("ala", "123")) #True
print(um.log_in("ala", "xyz")) #False
print(um.log_in("kasia", "123")) #False

um2 = UserManager()
   
