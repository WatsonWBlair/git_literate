def missing_number(A):
  ''' returns the smallest positive integer that does not occur in A '''
  setA = set(A)
    
    
  i = 1
  while True:
        if i not in setA:
            return i  
        i += 1
  return A[0]
