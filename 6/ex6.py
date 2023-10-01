from ex3 import Empregado


class Operario(Empregado):
    def __init__(self, nome: str, endereco: str, salarioBase: float, mesesTrabalhados: int, valorProducao: float, comissao: float):
        super().__init__(nome, endereco, salarioBase, mesesTrabalhados)
        self.valorProducao = valorProducao
        self.comissao = comissao

    def calcularSalario(self):
        return print(f"salario de {self.mesesTrabalhados} meses: R${float((self.salarioBase*self.mesesTrabalhados)+ (self.valorProducao*self.comissao)):.2f}")


operario = Operario("jonas", "rua pindamangueira 3343", 2000, 12, 1000, 0.1)
print(operario.get_nome())
print(operario.get_endereco())
print(operario.get_salarioBase())
print(operario.get_mesesTrabalhados())
operario.calcularSalario()
operario.set_nome("roberto")
operario.set_endereco("alela")
operario.set_salarioBase(2500)
operario.set_mesesTrabalhados(24)
operario.calcularSalario()
