import random

def run():
    nro_aleatorio= random.randint(1,10)
    nro_elegido = int(input('Elige un nro del 1 al 10: '))
    while nro_aleatorio != nro_elegido:
        if nro_elegido < nro_aleatorio:
            print('Busca un nro mas grande')
        else:
            print('Busca un nro mas pequeño')
        nro_elegido = int(input('Elige un nro del 1 al 10: '))
    input('Ganaste')

if __name__ == '__main__':
    run()
