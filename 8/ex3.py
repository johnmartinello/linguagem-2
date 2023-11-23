from abc import ABC, abstractmethod


class Conta(ABC):
    @abstractmethod
    def atualiza():
        pass


if __name__ == '__main__':
    c = Conta()
    
#erro: TypeError: Can't instantiate abstract class Conta with abstract method atualiza
#nao eh possivel instanciar pois a classe eh abstrata