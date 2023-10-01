from ex1 import Pessoa


class Empregado(Pessoa):
    def __init__(self, nome: str, endereco: str, salarioBase: float, mesesTrabalhados: int):
        super().__init__(nome, endereco)
        self.salarioBase = salarioBase
        self.mesesTrabalhados = mesesTrabalhados

    def get_salarioBase(self):
        return self.salarioBase

    def set_salarioBase(self, novo_salarioBase: str):
        self.salarioBase = novo_salarioBase
        return print(f"salarioBase mudado para '{self.salarioBase}'")

    def get_mesesTrabalhados(self):
        return self.mesesTrabalhados

    def set_mesesTrabalhados(self, novo_mesesTrabalhados: str):
        self.mesesTrabalhados = novo_mesesTrabalhados
        return print(f"mesesTrabalhados mudado para '{self.mesesTrabalhados}'")

    def calcularSalario(self):
        return print(f"salario de {self.mesesTrabalhados} meses: R${float(self.salarioBase*self.mesesTrabalhados):.2f}")


empregado = Empregado("jonas", "rua pindamangueira 3343", 2000, 12)
print(empregado.get_nome())
print(empregado.get_endereco())
print(empregado.get_salarioBase())
print(empregado.get_mesesTrabalhados())
empregado.calcularSalario()
empregado.set_nome("roberto")
empregado.set_endereco("alela")
empregado.set_salarioBase(2500)
empregado.set_mesesTrabalhados(24)
empregado.calcularSalario()
