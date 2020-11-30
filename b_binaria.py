# -*- coding: utf-8 -*-

def binary_search(numbers, number_to_find, low, high):
    if low > high:
        return False

    mid = int((low+high)/2)

    if numbers[mid] == number_to_find:
        return True
    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid-1 )
    else:
        return binary_search(numbers, number_to_find, mid + 1, high )



if __name__ == '__main__':
    list_nro = [2, 6, 8, 9, 15, 16, 19, 21, 29, 38, 71, 88, 99]
    number_to_find = int(input('Ingrese un nùmero: '))
    result = binary_search(list_nro, number_to_find, 0, len(list_nro)-1)
    if result:
        print('El numero existe en la lista')
    else:
        print('El numero no existe en la lista')


