

def funcion_decoradora(func_parametro):
    def funcion_interior():
        # Acciones adcionales que decora
        print('Vamos a realizar un calculo: ')
        func_parametro()
        # Acciones adicionales que decora
        print('Hemos terminado el calculo')
    return funcion_interior


@funcion_decoradora
def suma():
    print(3+5)

@funcion_decoradora
def resta():
    print(10-5)


suma()
resta()


