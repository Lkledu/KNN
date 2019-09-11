import math
from color import Color

cor = Color()
dataset = [Color(), Color(), Color()]
#VERMELHO
dataset[0].red = 255
dataset[0].green = 0
dataset[0].blue = 0
dataset[0].label = "VERMELHO"

#VERDE
dataset[1].red = 0
dataset[1].green = 255
dataset[1].blue = 0
dataset[1].label = "VERDE"

#AZUL90oooooooooooooooooo--------------------
dataset[2].red = 0
dataset[2].green = 0
dataset[2].blue = 255
dataset[2].label = "AZUL"

cor.red = input("Digite um tom de vermelho: \n")
cor.green = input("Digite um tom de verde: \n")
cor.blue = input("Digite um tom de azul: \n")

def euclidianDist(point, list_data):
    distancia = []

    for x in list_data:
        distancia.append([math.sqrt(((int(point.red) - x.red)**2) + ((int(point.green) - x.green)**2) + ((int(point.blue) - x.blue)**2)), x.label])
        

    return min(distancia)[1]

print(euclidianDist(cor, dataset))
