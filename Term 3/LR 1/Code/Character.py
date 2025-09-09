import abc

class Character(abc.ABC):

    def __init__(self):
        pass

    @abc.abstractmethod
    def attack(self):
        pass
    
    @abc.abstractmethod
    def defend(self):
        pass
