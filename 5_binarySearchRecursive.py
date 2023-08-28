# Pasos
#     Elegir el punto medio

#     Comparar el elemento buscado, si es mas chico eliminar la parte superior de la list, de lo contrario la parte inferior

#     Repetir hasta encontrar el elemento o quedarse sin elementos en la lista


#Source from: https://www.geeksforgeeks.org/python-program-for-binary-search/
def binarySearch(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binarySearch(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1


A = [1,2,3,4,5,6,7,8,10]
B = [1,2,3,4,5,6,7,8,9,10]

if __name__ == '__main__':
    print(binarySearch(A, 0, len(A)-1, 9))
    print(binarySearch(B, 0, len(B)-1, 9))
    print(binarySearch(B, 0, len(B)-1, 2))
