# Pasos:
#     Encontrá el valor mínimo e intercambialo por el primer valor del array

#     Encontrá el segundo valor más chico e intercambialo por el segundo valor del array

#     Repetir hasta que esté ordenado el array


#     por cada i del array:
#         minimo = i
#         por cada j del array:
#             si j < i:
#                 intercambiar(i, j)


def selectionSort(array):
    array_res = []

    print(f'Starting: {array}')

    for index_i, i in enumerate(array):
        index_min = index_i
        min = i

        for index_j, j in enumerate(array[index_i:]):
            if j < min:
                index_min = index_j + index_i
                min = j

        array[index_min] = i
        array[index_i] = min

    print(f'Finish: {array}')



A = [1,2,3,4,5,6,7,8,10]
B = [10,9,8,7,6,5,4,3,2,1]
C = [7,4,7,3,4,8,2,8,3,6,4,10,1]

if __name__ == '__main__':
    selectionSort(A)
    selectionSort(B)
    selectionSort(C)


# Peor Caso Complejidad Tiempo: O(n^2)
                                
# Caso Promedio Complejidad Tiempo: O(n^2)
                                    
# Mejor Caso Complejidad Tiempo: O(n^2)


7,4,7,3,4,8,2,8,3,6,4,10,1

index_i = 0
i = 7

index_j = 11
j = 1
        