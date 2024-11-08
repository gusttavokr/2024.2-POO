from datetime import datetime
from paciente import *

class UI:
    paciente = None
    def menu():
        print("Escolha a operação:")
        print("1- Criar paciente, 2- Informar a idade, 3- Mostrar paciente, 4- fim")
        return int(input())
    
    def main():
        op = 0
        while op != 4:
            op = UI.menu()
            if op == 1:
                UI.criarPaciente()
            if op == 2:
                UI.mostrarIdade()
            if op == 3:
                UI.mostrarPaciente()

    @classmethod
    def criarPaciente(cls):
        nome = input("Digite seu nome: ")
        cpf = input("Digite seu cpf: ")
        telefone = input("Digite seu telefone: ")
        nascimento = datetime.strptime(input("Digite sua data de nascimento: "), "%d/%m/%Y")
        cls.paciente = Paciente(nome,cpf,telefone,nascimento)

    @classmethod
    def mostrarIdade(cls):
        if cls.paciente == None:
            print("Paciente não criado")
        else:
            print(cls.paciente.Idade())

    @classmethod
    def mostrarPaciente(cls):
        print(cls.paciente)

UI.main()