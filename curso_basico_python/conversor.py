menu = """
Bienvenindo al conversor de monedas
1.- Pesos colombianos
2.- Pesos argentinos
3.- Pesos mexicanos

Elige una opción:"""

opcion = input(menu)
valor_dolar_pesos_colombianos = 3875
valor_dolar_argentinos = 72.76
valor_dolar_pesos_mexicanos = 22.39
dolares = 0
varStr1 = "Cuantos pesos "
varStr2 = " tienes?: "
valor_dolar = -1

if opcion == '1':
    pesos = input(varStr1 + "colombianos" + varStr2)
    pesos = float(pesos)
    dolares = pesos/valor_dolar_pesos_colombianos
elif opcion == '2':
    pesos = input(varStr1 + "argentinos" + varStr2)
    pesos = float(pesos)
    dolares = pesos/valor_dolar_argentinos
elif opcion == '3':
    pesos = input(varStr1 + "mexicanos" + varStr2)
    pesos = float(pesos)
    dolares = pesos/valor_dolar_pesos_mexicanos
else:
    print("Ingresa una opción de menú válida!!")
    exit()
print("Tienes $" + str(round(dolares,2)) + " dólares")

