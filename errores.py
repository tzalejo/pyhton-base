
countries = {
        'mexico': 122,
        'argentina': 42,
        'colombia': 49,
        'peru': 31,
        'chile': 18
        }
while True:
    country = str(input('Escribe el nombre de un pais: ')).lower()
    try:
        print('La poblacion de {} es : {} millnes'.format(country, countries[country]))
    except KeyError:
        print('No tenemos el dato de la poblacion de {}'.format(country))


