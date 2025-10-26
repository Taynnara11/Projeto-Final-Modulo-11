from Funcionario import Funcionario

class Medico(Funcionario):

    def __init__(self, nome, idade, cargo, salario, especialidade):
        super().__init__(nome, idade, cargo, salario)
        self._especialidade = especialidade
        self.pacientes = []


    @property
    def especialidade(self):
        return self._especialidade
    

    @especialidade.setter
    def especialidade(self, valor):
        if len(valor)>0:
            self._especialidade = valor
        else:
            print("Valor inválido.")
    
    def add_paciente(self, paciente):
        self.pacientes.append(paciente)
        print("Paciente Adcionado!")

    
    def listar_pacientes(self):
        if len(self.pacientes)>0:
            print("Pacientes atendidos: ")
            for i in range(len(self.pacientes)):
                print(i +1, "-", self.pacientes[i])

    def calcular_pagamento(self):
        valor_paciente = 75
        pg_total = self.salario + (len(self.pacientes) * valor_paciente)
        return pg_total
    
    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade:  {self.idade}")
        print(f"Especialidade: {self._especialidade}")
        print(f"Pacientes atendidos: {len(self.pacientes)}")
        print(f"Salário total: {self.calcular_pagamento()}")