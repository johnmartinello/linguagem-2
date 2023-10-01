# from ex1 import Pessoa
from ex3 import Empregado


class Administrador(Empregado):
    def __init__(self, nome: str, endereco: str, salarioBase: float, mesesTrabalhados: int, ajudasDeCusto: float):
        super().__init__(nome, endereco, salarioBase, mesesTrabalhados)
        self.ajudasDeCusto = ajudasDeCusto

    def calcularSalario(self):
        return print(f"salario de {self.mesesTrabalhados} meses: R${float((self.salarioBase*self.mesesTrabalhados)+self.ajudasDeCusto):.2f}")


administrador = Administrador(
    "jonas", "rua pindamangueira 3343", 2000, 12, 1500)
print(administrador.get_nome())
print(administrador.get_endereco())
print(administrador.get_salarioBase())
print(administrador.get_mesesTrabalhados())
administrador.calcularSalario()
administrador.set_nome("roberto")
administrador.set_endereco("alela")
administrador.set_salarioBase(2500)
administrador.set_mesesTrabalhados(24)
administrador.calcularSalario()
