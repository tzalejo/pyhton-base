def primo(nro):
    for i in range(2, nro):
        if nro % i == 0:
            return False
    return True


def run():
    numero = int(input('Ingrese un numero: '))
    if primo(numero):
        print('El numero es un primo')
    else:
        print('El numero no es primo')


if __name__=='__main__':
    run()
