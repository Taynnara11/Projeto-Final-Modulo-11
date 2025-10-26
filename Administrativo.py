from Funcionario import Funcionario
class Administrativo(Funcionario):

    def __init__(self, nome, idade, cargo, salario, setor):
        super().__init__(nome, idade, cargo, salario)
        self._setor = setor
        self.hrs_t = 0

    

    @property
    def setor(self):
        return self._setor

    @setor.setter
    def setor(self, valor):
        if len(valor) > 0:
            self._setor = valor
        else:
            print("Erro: o setor não pode estar vazio.")

    

    
    def registrar_horas(self, horas):
        if horas > 0:
            self.hrs_t = self.hrs_t + horas
            print("Horas registradas com sucesso!")

        else:
            
             print("Erro: as horas devem ser maiores que zero.")

    

    def calcular_pagamento(self):
        valor_por_hora = 8
        pagamento_total = self.salario + (self.hrs_t * valor_por_hora)
        return pagamento_total


    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Setor: {self._setor}")
        print(f"Horas trabalhadas: {self.hrs_t}")
        print(f"Salário total: {self.calcular_pagamento()}")
