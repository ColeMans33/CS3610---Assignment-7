from abc import ABC, abstractmethod

class Subject(ABC):
    def __init__(self):
        self.__observers = set()
        self.__version = ""
        self.__nextID = 1000

    def attach(self, observer):
        self.__observers.add(observer)
        observer.appVersion = None

    def _notify_observers(self, newVersion):
        for observer in self.__observers:
            observer.update(newVersion)


    def pushUpdate(self, update):
        self.__version = update
        self.__notify_observers(update)

    def getVersion(self):
        return self.__version


    def getNextID(self):
        self.__nextID += 1
        return self.__nextID
