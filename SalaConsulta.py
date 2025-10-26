from Sala import Sala
from Medico import Medico

class SalaConsulta(Sala):
    
    def __init__(self, numero, capacidade, medico_responsavel):
        self._numero = numero
        self._capacidade = capacidade
        self._medico_responsavel = medico_responsavel
        self.pacientes = []  

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        if isinstance(valor, int) and valor > 0:
            self._numero = valor
        else:
            print("Erro: Número da sala deve ser um inteiro positivo")

    @property
    def capacidade(self):
        return self._capacidade

    @capacidade.setter
    def capacidade(self, valor):
        if isinstance(valor, int) and valor > 0:
            self._capacidade = valor
        else:
            print("Erro: Capacidade deve ser um número inteiro positivo")

    
    @property
    def medico_responsavel(self):
        return self._medico_responsavel

    @medico_responsavel.setter
    def medico_responsavel(self, valor):
      
        if isinstance(valor, Medico):
            self._medico_responsavel = valor
        else:
            print("Erro: o responsável deve ser um objeto da classe Medico.")

    
        
    def agendar_consulta(self, paciente):
        
        if len(self.pacientes) >0:
            self.pacientes.append(paciente)
            print(f"Paciente {paciente} adicionado à lista de consultas.")
        else:
            print("Erro: Introduza um nome válido.")

    
    def detalhes_Sala(self):
        print(f"Número da sala: {self.numero}")
        print(f"Capacidade: {self.capacidade}")
        print(f"Médico responsável: {self._medico_responsavel.nome}")
        