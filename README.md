<div align="center">
  <img width="200"
    alt="Java Logo"
    src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"
    />
  <h1>PROGRAMAÇÃO ORIENTADA À OBJETOS</h1>
  Repositório de estudos para Programação Orientada à Objetos em Python.
</div>

## 📋 Aula 01 - Conceitos Iniciais
POO é um paradigma da programação, em que o principal artifício para as modelagens de software é o "objeto". Cada objeto é instânciado por uma "classe" que pode conter tanto atributos, como métodos.

Para entender POO inicialmente, é crucial entender os 4 fundamentos, que são:

### 1. Encapsulamento
O encapsulamento é o fundamento mais crucial do que se trata a segurança dos dados, pois é nele que é selecionado as informações que serão exibidas durante a execução do programa. Para isso existe os **Modificadores de Acesso**, que são:

1. Público: Membros (atributos ou métodos) declarados como public são acessíveis de qualquer lugar no código.

2. Privado: Membros private só são acessíveis dentro da própria classe onde foram declarados. Protege os dados e métodos internos de acesso direto de fora da classe. "__(metodoPrivado)"

3. Membros protected são acessíveis dentro da própria classe, por subclasses (mesmo que estejam em pacotes diferentes) e por classes no mesmo pacote. "_(metodoProtegido)"

### 2. Abstração
O conceito de Abstração é justamente o que a própria palavra significa. ABSTRAIR! Quando estamos programando para POO, precisamos abstrair do mundo real o necessário para o entendimento de seu código.

Resumindo: Simplifica a complexidade do sistema ao esconder detalhes desnecessários. Traduzindo o seu código pro mundo real.

### 3. Herança
Resumidamente, são classes que herdam classes, por exemplo:
```
class Mamífero:
    pass
  
class Gato(mamífero):
    pass
```

### 4. Polimorfismo
O polimorfismo é quando uma classe possui as mesmas atribuições/métodos de outras classes. Por exemplo:
```
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
```
-----------------------------------------
<div align="center">
Em construção
</div>