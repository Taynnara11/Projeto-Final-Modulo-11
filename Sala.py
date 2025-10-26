from abc import ABC, abstractmethod
class Sala(ABC):
    def __init__(self, numero, capacidade):
        self.numero = numero
        self.capacidade = capacidade

    
    @property
    def numero(self):
        pass

    @numero.setter
    def numero(self):
        pass

   
    @property
    def capacidade(self):
        pass

    @capacidade.setter
    def capacidade(self):
        pass
    
    @abstractmethod
    def detalhes_Sala(self):
        pass