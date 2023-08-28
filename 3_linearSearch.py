# Pasos:
#     iterar a traves de cada item de una lista

#     si el item es el buscado, devolver el indice


# Source from: https://www.geeksforgeeks.org/python-program-for-linear-search/
def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
 
    return -1

A = [1,2,3,4,5,6,7,8,10]
B = [10,9,8,7,6,5,4,3,2,1]
C = [7,4,7,3,4,8,2,8,3,6,4,10,1]

if __name__ == '__main__':
    print(linearSearch(A, 9))
    print(linearSearch(B, 9))
    print(linearSearch(C, 1))


# Peor Caso Complejidad Tiempo: O(n)
                                
# Caso Promedio Complejidad Tiempo: O(n/2)
                                    
# Mejor Caso Complejidad Tiempo: O(1)