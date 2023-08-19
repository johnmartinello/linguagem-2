class Empregado:
    def __init__(self, nome, departamento, horasTrabalhadasNoMes, salarioPorHora):
        self.nome = nome
        self.departamento = departamento
        self.horasTrabalhadasNoMes = horasTrabalhadasNoMes
        self.salarioPorHora = salarioPorHora

    def mostraDados(self):
        print(f"Nome: {self.nome}\nDepartamento: {self.departamento}\nHoras trabalhadas no mês: {self.horasTrabalhadasNoMes}\nSalário por hora: {self.salarioPorHora}")

    def calculaSalarioMensal(self):
        return self.salarioPorHora * self.horasTrabalhadasNoMes


empregado = Empregado(
    nome="Jonas",
    departamento="TI",
    horasTrabalhadasNoMes=160,
    salarioPorHora=35
)
empregado.mostraDados()
print("Salário Mensal:", empregado.calculaSalarioMensal())
