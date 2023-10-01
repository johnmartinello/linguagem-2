class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        self.cargo = None

    def exibeDados(self):
        print(
            f"Nome: {self.nome}\nSalário: {self.salario}\nCargo: {self.cargo}")


class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        self.cargo = "Gerente"


class Assistente(Funcionario):
    def __init__(self, nome, salario, matricula):
        super().__init__(nome, salario)
        self.matricula = matricula
        self.cargo = "Assistente"

    def getMatricula(self):
        return self.matricula

    def exibeDados(self):
        print(
            f"Nome: {self.nome}\nSalário: {self.salario}\nCargo: {self.cargo}\nMatrícula: {self.matricula}")


class Tecnico(Assistente):
    def __init__(self, nome, salario, matricula, bonus):
        super().__init__(nome, salario, matricula)
        self.cargo = "Assistente Técnico"
        self.bonus = bonus

    def exibeDados(self):
        print(
            f"Nome: {self.nome}\nSalário: {self.salario}\nCargo: {self.cargo}\nMatrícula: {self.matricula}\nBônus: {self.bonus}")


class Administrativo(Assistente):
    def __init__(self, nome, salario, matricula, turno):
        super().__init__(nome, salario, matricula)
        self.cargo = "Assistente Administrativo"
        self.turno = turno

        if self.turno == "noite":
            self.adicional_noturno = input("adicional: ")

    def exibeDados(self):
        print(
            f"Nome: {self.nome}\nSalário: {self.salario}\nCargo: {self.cargo}\nMatrícula: {self.matricula}\nTurno: {self.turno}\nAdicional Noturno: {self.adicional_noturno}")


gerente = Gerente("João Gerente", 5000)
assistente_tecnico = Tecnico("Maria Técnica", 3000, "12345", 500)
assistente_administrativo = Administrativo(
    "Pedro Admin", 2500, "67890", "noite")

print("Dados do Gerente:")
gerente.exibeDados()

print("\nDados do Assistente Técnico:")
assistente_tecnico.exibeDados()

print("\nDados do Assistente Administrativo:")
assistente_administrativo.exibeDados()
