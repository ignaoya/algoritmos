# Pasos
#     Seleccioná un punto en la lista para dividir

#     Iterar a lo largo de la lista para que los numeros mas chicos queden de un lado y los grandes del otro

#     Particionar las listas que te quedaron

#     Repetir recursivamente.


# Source from: https://www.geeksforgeeks.org/python-program-for-quicksort/
def partition(array, low, high):
 
    # choose the rightmost element as pivot
    pivot = array[high]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort
 
 
def quickSort(array, low, high):
    # print(f'Start: {array}')
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)
    # print(f'Finish: {array}')




A = [1,2,3,4,5,6,7,8,10]
B = [10,9,8,7,6,5,4,3,2,1]
C = [7,4,7,3,4,8,2,8,3,6,4,10,1]
# C = [ 0 for i in range(10000)]

if __name__ == '__main__':
    quickSort(A, 0, len(A) - 1)
    print(A)
    quickSort(B, 0, len(B) - 1)
    print(B)
    quickSort(C, 0, len(C) - 1)
    print(C)



# Peor Caso Complejidad Tiempo: O(n^2)
                                
# Caso Promedio Complejidad Tiempo: O(n log n)
                                    
# Mejor Caso Complejidad Tiempo: O(n log n)


# 7,4,7,3,4,8,2,8,3,6,4,10,1,5

# 4,3,4,2,3,4,1,   5,     7,7,8,8,6,10

# 1, 4,3,4,2,3,4 ,   5,   7,7,8,8,6,   10 

# 1,  4,3,4,2,3, 4
#     2, 3, 4, 4
