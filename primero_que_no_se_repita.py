# -*- coding: utf-8 -*-
"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""

# "abacabad"  
# {
#   'a': (0, 4),
#   'b': (1, 2),
#   'c': (3, 1), ...
# }
def run(secuencia_letras):
  ver_letras = {}
  # aca recorremos un string
  for indice, letra in enumerate(secuencia_letras):
    if letra not in ver_letras:
      ver_letras[letra] = (indice, 1)
    else:
      ver_letras[letra] = (ver_letras[letra][0], ver_letras[letra[1] + 1])
  print(ver_letras)
  # aca recorremos un diccionario = {}
  for key, value in ver_letras:
    if value[1] == 1:
       return key
  return '_'

if __name__ == '__main__':
  secuencia_caracteres = str(input('Escriba una secuencia: '))
  # resultado = 
  run(secuencia_caracteres)

  # if resultado == '_':
  #   print('Todos los caracteres se repiten.')
  # else:
  #   print('El primer caracter que no se repite: {}'.format(resultado))


def debug(breakpoint=False):
  def debug_decorator(f):
    def new_function(*args, **kwargs):
      print(f"Function {f.__name__}() called!")
      return f(*args, **kwargs)
    return new_function
  return debug_decorator






















