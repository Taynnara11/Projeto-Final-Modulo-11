from Pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, salario):
        self._nome = nome
        self._idade = idade
        self.cargo = cargo
        self._salario = salario
        
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):              
        if isinstance(valor, str) and len(valor.strip()) > 0:
            self._nome = valor
        else:
            print("Erro: Nome inválido")

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, valor):             
        if isinstance(valor, int) and valor > 0:
            self._idade = valor
        else:
            print("Erro: Idade deve ser um número inteiro positivo")

    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, new_salario):
        if new_salario >0:
            self._salario = new_salario
        else:
            print("Salário não pode ser nulo ou negativo.")

    
    def mostrar_informacoes(self):
        print("Nome:", self.nome)
        print("Cargo:", self.cargo)
        print("Salário:", self._salario)

    def aplicar_aumento(self, porcentagem):
        if porcentagem >0:
            aumento = self.salario * (porcentagem/100)
            self._salario = self._salario + aumento
            print(f"Novo salário: {self.salario}")

        else:
            print("Pocentagem te que ser maior que zero.")

    
    def exibir_informacoes(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Cargo:", self.cargo)
        print("Salário:", self._salario)