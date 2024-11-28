from models.atleta import Atleta, Atletas
from models.treino import Treino, Treinos
from datetime import datetime, timedelta

class View:
    @staticmethod
    def atleta_inserir(id, nome, nasc):
        a = Atleta(id, nome, nasc)
        Atletas.inserir(a)
    
    @staticmethod
    def atleta_listar():
        return Atletas.listar()

    @staticmethod
    def treino_inserir(id, id_atleta, data, dist, tempo):
        a = Treino(id, id_atleta, data, dist, tempo)
        Treinos.inserir(a)

    @staticmethod
    def listar_treinos():
        return Treinos.listar()

    @staticmethod 
    def atleta_mais_rapido():
        treinos = Treinos.listar()
        menor = treinos[0]
        for treino in Treinos.listar():
            if treino.pace() < menor.pace():
                menor = treino
        return menor.get_id_atleta()

    @staticmethod
    def treino_mais_rápido(id_atleta):
        treinos = Treinos.listar()
        for treino in treinos:
            if treino.getId_Atleta() == id_atleta():
                menor = treino
                break
        for treino in treinos:
            if treino.getId_Atleta() == id_atleta():
                if treino.pace() < menor.pace():
                    menor = treino
        return(menor)