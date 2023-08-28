

term = [0 for i in range(1000)]
 
def fibA(n):
   
  # base case
  if n <= 1:
    return n

  if term[n] != 0:
    return term[n]
 
  else:
    term[n] = fibA(n - 1) + fibA(n - 2)
    return term[n]
  
def fibB(n):
   
  # base case
  if n <= 1:
    return n
 
  else:
    return fibB(n - 1) + fibB(n - 2)

 

if __name__ == '__main__':
    n = 100
    print(fibA(n))


# 0 1 1 2 3 5 8 