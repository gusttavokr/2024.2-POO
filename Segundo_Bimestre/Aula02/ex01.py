class Funcionário:
    def __init__(self, nome, salarioBase):
        self.__nome = nome
        self._salarioBase = salarioBase
    def get_nome(self):
        return self.__nome
    def get_salarioBase(self):
        return self._salarioBase
    def __str__(self):
        return f"{self.__nome}, {self.get_salarioBase()}"
    
class Gerente(Funcionário):
    def __init__(self, nome, salarioBase, gratificacao):
        super().__init__(nome, salarioBase) # Puxando um método de outra classe
        self.__gratificacao = gratificacao
    def get_salarioBase(self):
        return self._salarioBase + self.__gratificacao
        #return super().get_salario() + self.__gratificacao

x = Funcionário("José Costa", 5000)
y = Gerente("Maria Lima", 5000, 3000)
print(x.get_nome()) # Nome
print(x.get_salarioBase()) # Salário
print(x)
print(type(x))
print(isinstance(x, object))
print(isinstance(x, Funcionário))
print(isinstance(x, Gerente))

print(y.get_nome())
print(y.get_salarioBase())
print(y)
print(type(y))
print(isinstance(y, object))
print(isinstance(y, Funcionário))
print(isinstance(y, Gerente))