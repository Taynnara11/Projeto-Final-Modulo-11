from Paciente import Paciente
from Medico import Medico
from Enfermeiro import Enfermeiro
from Administrativo import Administrativo
from EnfermeiroChefe import EnfermeiroChefe
from SalaConsulta import SalaConsulta
from SalaCirurgia import SalaCirurgia

def mostrar_menu():
    print("========================")
    print("        HOSPITAL       ")
    print("========================")
    print("Olá, seja bem-vindo(a) ao menu do Hospital")
    input("Pressione [Enter] para continuar...")

def menu_principal():
    pacientes = []
    medicos = []
    enfermeiros = []
    administrativos = []
    enfermeiros_chefes = []
    salas_consulta = []
    salas_cirurgia = []
    consultas = []

    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Criar Paciente")
        print("2. Criar Médico")
        print("3. Criar Enfermeiro")
        print("4. Criar Administrativo")
        print("5. Criar Enfermeiro Chefe")
        print("6. Criar Sala de Consulta")
        print("7. Criar Sala de Cirurgia")
        print("8. Agendar Consulta")
        print("9. Adicionar Equipamento a Sala de Cirurgia")
        print("10. Listar Todos os Registros")
        print("0. Sair")

        op = input("Escolha uma opção: ")

        match op:
            case "1":
                print("\n--- Criar Paciente ---")
                nome = input("Nome: ")

                while True:
                    try:
                        idade = int(input("Idade: "))
                        break
                    except ValueError:
                        print("Erro: Idade inválida! Digite novamente.")

                numero_utente = input("Número de utente: ")
                paciente = Paciente(nome, idade, numero_utente)
                pacientes.append(paciente)
                print(f"Paciente {nome} criado com sucesso!")

            case "2":
                print("\n--- Criar Médico ---")
                nome = input("Nome: ")

                while True:
                    try:
                        idade = int(input("Idade: "))
                        break
                    except ValueError:
                        print("Erro: Idade inválida! Digite novamente.")

                especialidade = input("Especialidade: ")

                while True:
                    try:
                        salario = float(input("Salário base: "))
                        break
                    except ValueError:
                        print("Erro: Salário inválido! Digite novamente.")

                medico = Medico(nome, idade, "Médico", salario, especialidade)
                medicos.append(medico)
                print(f"Médico {nome} ({especialidade}) criado com sucesso!")

            case "3":
                print("\n--- Criar Enfermeiro ---")
                nome = input("Nome: ")

                while True:
                    try:
                        idade = int(input("Idade: "))
                        break
                    except ValueError:
                        print("Erro: Idade inválida! Digite novamente.")

                turno = input("Turno (dia/noite): ")

                while True:
                    try:
                        salario = float(input("Salário base: "))
                        break
                    except ValueError:
                        print("Erro: Salário inválido! Digite novamente.")

                enfermeiro = Enfermeiro(nome, idade, "Enfermeiro", salario, turno)
                enfermeiros.append(enfermeiro)
                print(f"Enfermeiro {nome} criado com sucesso!")

            case "4":
                print("\n--- Criar Administrativo ---")
                nome = input("Nome: ")

                while True:
                    try:
                        idade = int(input("Idade: "))
                        break
                    except ValueError:
                        print("Erro: Idade inválida! Digite novamente.")

                setor = input("Setor: ")

                while True:
                    try:
                        salario = float(input("Salário base: "))
                        break
                    except ValueError:
                        print("Erro: Salário inválido! Digite novamente.")

                admin = Administrativo(nome, idade, "Administrativo", salario, setor)
                administrativos.append(admin)
                print(f"Funcionário administrativo {nome} criado com sucesso!")

            case "5":
                print("\n--- Criar Enfermeiro Chefe ---")
                nome = input("Nome: ")

                while True:
                    try:
                        idade = int(input("Idade: "))
                        break
                    except ValueError:
                        print("Erro: Idade inválida! Digite novamente.")

                turno = input("Turno (dia/noite): ")
                setor = input("Setor: ")

                while True:
                    try:
                        salario = float(input("Salário base: "))
                        bonus = float(input("Bônus de chefia: "))
                        break
                    except ValueError:
                        print("Erro: Salário ou bônus inválido! Digite novamente.")

                chefe = EnfermeiroChefe(nome, idade, salario, turno, setor, bonus)
                enfermeiros_chefes.append(chefe)
                print(f"Enfermeiro Chefe {nome} criado com sucesso!")

            case "6":
                print("\n--- Criar Sala de Consulta ---")
                while True:
                    try:
                        numero = int(input("Número da sala: "))
                        capacidade = int(input("Capacidade: "))
                        break
                    except ValueError:
                        print("Erro: Número ou capacidade inválido! Digite novamente.")

                medico_nome = input("Nome do médico responsável: ")
                medico_resp = None
                for m in medicos:
                    if m.nome == medico_nome:
                        medico_resp = m
                        break

                if medico_resp:
                    sala = SalaConsulta(numero, capacidade, medico_resp)
                    salas_consulta.append(sala)
                    print(f"Sala de consulta {numero} criada com sucesso!")
                else:
                    print("Erro: Médico não encontrado.")

            case "7":
                print("\n--- Criar Sala de Cirurgia ---")
                while True:
                    try:
                        numero = int(input("Número da sala: "))
                        capacidade = int(input("Capacidade: "))
                        break
                    except ValueError:
                        print("Erro: Número ou capacidade inválido! Digite novamente.")

                sala = SalaCirurgia(numero, capacidade)
                salas_cirurgia.append(sala)
                print(f"Sala de cirurgia {numero} criada com sucesso!")

            case "8":
                print("\n--- Agendar Consulta ---")
                nome_medico = input("Nome do Médico: ")
                nome_paciente = input("Nome do Paciente: ")
                
      
                medico_encontrado = None
                for m in medicos:
                    if m.nome == nome_medico:
                        medico_encontrado = m
                        break
                
                if not medico_encontrado:
                    print(f"Erro: Médico '{nome_medico}' não encontrado.")
                    continue
              
                paciente_encontrado = None
                for p in pacientes:
                    if p.nome == nome_paciente:
                        paciente_encontrado = p
                        break
                
                if not paciente_encontrado:
                    print(f"Erro: Paciente '{nome_paciente}' não encontrado.")
                    continue
                
   
                data = input("Data (DD/MM/AAAA): ")
                tipo = input("Tipo (rotina/emergência): ")
    
                consultas.append({
                    "medico": medico_encontrado,
                    "paciente": paciente_encontrado,
                    "data": data,
                    "tipo": tipo
                })
                

                medico_encontrado.add_paciente(paciente_encontrado)
                print("Consulta agendada com sucesso!")

            case "9":
                print("\n--- Adicionar Equipamento ---")
                while True:
                    try:
                        numero = int(input("Número da sala de cirurgia: "))
                        break
                    except ValueError:
                        print("Erro: Número inválido! Digite novamente.")

                equipamento = input("Nome do equipamento: ")
                for sala in salas_cirurgia:
                    if sala.numero == numero:
                        sala.adicionar_equipamento(equipamento)
                        break
                else:
                    print("Sala não encontrada.")

            case "10":
                print("\n--- Listagem Geral ---")
                print("\nMédicos:")
                for m in medicos:
                    m.exibir_informacoes()

                print("\nEnfermeiros:")
                for e in enfermeiros:
                    e.exibir_informacoes()

                print("\nAdministrativos:")
                for a in administrativos:
                    a.exibir_informacoes()

                print("\nEnfermeiros Chefes:")
                for c in enfermeiros_chefes:
                    c.exibir_informacoes()

                print("\nPacientes:")
                for p in pacientes:
                    print(f"Nome: {p.nome}, Número de utente: {p.nutente}, Idade: {p.idade}")

                print("\nSalas de Consulta:")
                for s in salas_consulta:
                    s.detalhes_Sala()

                print("\nSalas de Cirurgia:")
                for s in salas_cirurgia:
                    s.detalhes_Sala()

                print("\nConsultas agendadas:")
                for c in consultas:
                    print(f"Médico: {c['medico'].nome}, Paciente: {c['paciente'].nome}, Data: {c['data']}, Tipo: {c['tipo']}")

            case "0":
                print("Saindo do sistema... Até logo!")
                break

            case _:
                print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    mostrar_menu()
    menu_principal()


