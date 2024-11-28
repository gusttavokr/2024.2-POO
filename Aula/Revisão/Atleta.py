class Treino:
    def __init__(self, data, distancia, tempo):
        self.__data = data
        self.__distancia = distancia
        self.__tempo = tempo

        if distancia <= 0:
            raise ValueError("Distância inválida")
        if tempo == "":
            raise ValueError("Tempo inválido")
        
    def getData(self):
        return self.__data
    def setData(self, data):
        self.__data = data

    def getDistancia(self):
        return self.__distancia
    def setDistancia(self, distancia):
        self.__distancia = distancia
        if distancia <= 0:
            raise ValueError("Distância inválida")
        
    def getTempo(self):
        return self.__tempo
    def setTempo(self, tempo):
        self.__tempo = tempo
        if tempo == "":
            raise ValueError("Tempo inválido")
        
    def Pace(self):
        horas, minutos, segundos = map(int, self.__tempo.split(':'))
        time = horas * 3600 + minutos * 60 + segundos

        if self.__distancia <= 0:
            raise ValueError("Distância inválida")
        
        metros = self.__distancia // 1000

        pace_seg = time/metros

        minutos = int(pace_seg // 60)
        segundos = int(pace_seg % 60)

        return f"{minutos}'{segundos}"
    
    def __str__(self):
        return f"Data: {self.__data} - Distância: {self.__distancia} - Tempo: {self.__tempo}"
    
class Atleta:
    def __init__(self, nome, nascimento):
        self.__nome = nome
        self.__nascimento = nascimento
        self.__treinos = []
        if nome == "":
            raise ValueError("Nome inválido!")
    
    def inserir(self, treino):
        self.__treinos.append(treino)
    
    def remove(self, treino):
        self.__treinos.remove(treino)

    def listar(self):
        return self.__treinos
    
    def distanciatotal(self, dist):
        for x in self.__treinos:
            if x.getDistancia() == dist:
                return x
        return None
    
    def __str__(self):
        return f"Nome: {self.__nome}, Data de nascimento: {self.__nascimento}, Treinos: {len(self.__treinos)}"
    

corrida1 = Treino("01/01/2025", 5, "02:30:00")
corrida2 = Treino("01/05/2025", 10, "03:00:00")

print(corrida1, corrida1.pace())
print(corrida2, corrida2.pace())

maikinho = Atleta("Maike", "")
    

        
        
        