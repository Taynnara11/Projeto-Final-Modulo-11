from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        pass

    @nome.setter
    def nome(self):              
        pass

    @property
    def idade(self):
        pass

    
    @idade.setter
    def idade(self):             
        pass

    @abstractmethod
    def exibir_informacoes(self):
        pass