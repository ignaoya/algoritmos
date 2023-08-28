# Pasos
#     Elegir el punto medio

#     Comparar el elemento buscado, si es mas chico eliminar la parte superior de la list, de lo contrario la parte inferior

#     Repetir hasta encontrar el elemento o quedarse sin elementos en la lista


#Source from: https://www.geeksforgeeks.org/python-program-for-binary-search/
def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1


A = [1,2,3,4,5,6,7,8,10]
B = [1,2,3,4,5,6,7,8,9,10]

if __name__ == '__main__':
    print(binarySearch(A, 9))
    print(binarySearch(B, 9))
    print(binarySearch(B, 2))


# Peor Caso Complejidad Tiempo: O(log n)
                                
# Caso Promedio Complejidad Tiempo: O(log n)
                                    
# Mejor Caso Complejidad Tiempo: O(1)