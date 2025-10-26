from Pessoa import Pessoa
class Paciente(Pessoa):


    def __init__(self, nome, idade, nutente):
        self._nome = nome
        self._idade = idade
        self._nutente = nutente
        self.historico = []

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
    def nutente(self):
        return self._nutente 

    @nutente.setter
    def nutente(self, valor):
        if len(valor)>0:
            self._nutente = valor
        
        else:
            print("Erro: Valor inválido")
            
    
    def add_registro(self, descricao):
        if len(descricao)>0:
            self.historico.append(descricao)
            print("Descrição registrada!")
        
        else:
            print("Erro: A descrição não pode estar vazia")

    
    def mostrar_historico(self):
        if len(self.historico)>0:
            print("Histórico do Paciente: ")
            for i in range(len(self.historico)):
                print(i +1, "-", self.historico[i])
        
        else:
            print("O histórico está vazio")



    def exibir_informacoes(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Número de Utente:", self.nutente)