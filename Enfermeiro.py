from Funcionario import Funcionario
class Enfermeiro(Funcionario):
    def __init__(self, nome, idade, cargo, salario, turno):
        Funcionario.__init__(self, nome, idade, cargo, salario)
        self._turno = turno
        self.pacientes = []

    
    @property
    def turno(self):
        return self._turno

    @turno.setter
    def turno(self, valor):
        if valor == "dia" or valor == "noite":
            self._turno = valor
        else:
            print("Erro: o turno deve ser 'dia' ou 'noite'. ")

    
    def add_paciente(self, paciente):
        self.pacientes.append(paciente)
        print("Paciente adicionado aos cuidados do enfermeiro!")


    def listar_pacientes(self):
        if len(self.pacientes)>0:
            for i in range(len(self.pacientes)):
                print(i + 1, "-", self.pacientes[i])
        
        else:
            print("Nenhum paciente sob cuidado.")


    def calcular_pg(self):
        if self._turno == "noite":
            adicional = 100
        else :
            adicional = 20
        
        pg_total = self.salario + adicional
        return pg_total
    

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Turno: {self._turno}")
        print(f"Pacientes sob cuidado: {len(self.pacientes)}")
        print(f"Salário total: {self.calcular_pg()}")
