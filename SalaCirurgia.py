from Sala import Sala
class SalaCirurgia(Sala):
   
    def __init__(self, numero, capacidade):
        self._numero = numero
        self._capacidade = capacidade
        self.equipamentos = []  

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

    
    def adicionar_equipamento(self, equipamento):
        if len(equipamento) > 0:
            self.equipamentos.append(equipamento)
            print(f"Equipamento '{equipamento}' adicionado com sucesso!")
        else:
            print("Erro: nome de equipamento inválido.")

    
    def detalhes_Sala(self):
        print(f"Número da sala: {self.numero}")
        print(f"Capacidade: {self.capacidade}")
        print("Equipamentos disponíveis:")

        if len(self.equipamentos) == 0:
            print("Nenhum equipamento cadastrado.")
        else:
            for i in range(len(self.equipamentos)):
                print(i + 1, "-", self.equipamentos[i])
