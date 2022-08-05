from math import*
from random import randrange, uniform

baseSimulacoesEfetivadas = [[90,4,1,1,20], [88,1,1,1,20], [1456,1,1,1,2], [60.2,1,1,1,20]]
entrada = [60,2,1,1,20]

SIMILARIDADE_MINIMA = 30

def euclidean_distance(x,y):
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))

def verificaSimilaridadeMinima(valor, minimo):
    if valor <= minimo:
        return True
    return False

def dividaGerador(maximo):
    return round(uniform(50, maximo), 2)

def inteiroGerador(maximo):
    return randrange(1, maximo)

print(dividaGerador(10000))
print(inteiroGerador(30))


def main():
    for i in range(len(baseSimulacoesEfetivadas)):
        distancia = euclidean_distance(baseSimulacoesEfetivadas[i], entrada)
        
        

        if verificaSimilaridadeMinima(distancia, SIMILARIDADE_MINIMA):
            print("Base: ", baseSimulacoesEfetivadas[i],  " - Similar: ", entrada)
            print("dist = ", distancia)
            break
    
    
    