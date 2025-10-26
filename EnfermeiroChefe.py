from Enfermeiro import Enfermeiro
from Administrativo import Administrativo

class EnfermeiroChefe(Enfermeiro, Administrativo):
    def __init__(self, nome, idade, salario_base, turno, setor, bonus_chefia):
        Enfermeiro.__init__(self, nome, idade, "Enfermeiro Chefe", salario_base, turno)
        Administrativo.__init__(self, nome, idade, "Enfermeiro Chefe", salario_base, setor)
        self._bonus_chefia = bonus_chefia


        
    @property
    def bonus_chefia(self):
        return self._bonus_chefia

    @bonus_chefia.setter
    def bonus_chefia(self, valor):
        if valor > 0:
            self._bonus_chefia = valor
        else:
            print("Erro: o bônus de chefia deve ser positivo.")

    
        
    def calcular_pagamento(self):
        pagamento_enfermeiro = Enfermeiro.calcular_pg(self)
        pagamento_admin = Administrativo.calcular_pagamento(self)
        pagamento_total = pagamento_enfermeiro + pagamento_admin + self._bonus_chefia
        return pagamento_total
    
    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Turno: {self._turno}")
        print(f"Setor: {self._setor}")
        print(f"Pacientes sob cuidado: {len(self.pacientes)}")
        print(f"Bônus de chefia: {self._bonus_chefia}")
        print(f"Salário total: {self.calcular_pagamento()}")


