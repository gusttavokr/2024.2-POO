from datetime import datetime

class Paciente:
    def __init__(self, Nome, Cpf, Telefone, Nascimento):
        self.__setNome(Nome)
        self.__setCpf(Cpf)
        self.__setTelefone(Telefone)
        self.nascimento = Nascimento

    def __setNome(self, Nome):
        if len(Nome) > 0:
            self.nome = Nome
        else:
            raise ValueError ("Nome vazio")
    def __setCpf(self, Cpf):
        if len(Cpf) > 0:
            self.cpf = Cpf
        else:
            raise ValueError ("Cpf inválido")
    def __setTelefone(self, Telefone):
        if len(Telefone) > 0:
            self.telefone = Telefone
        else:
            raise ValueError ("Telefone inválido")

    def Idade(self):
        dataAtual = datetime.now()
        anos = dataAtual.year - self.nascimento.year
        meses = dataAtual.month - self.nascimento.month
        return f'{anos} anos e {meses} meses'

    def __str__(self):
        return f"{self.nome} - {self.cpf} - {self.telefone} - {self.nascimento.date()}"