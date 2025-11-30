'''
Implementation of:
https://en.wikipedia.org/wiki/Midpoint_circle_algorithm#Jesko's_method
'''

# import numpy as np

def zero_matrix(dim):
  m = [[0 for i in range(dim)] for i in range(dim)]
  return m

def circumference(dim,r):
  if dim%2 == 1:
    if 0 < r:
      if dim >= r*2:

        u = zero_matrix(dim)
        c = dim//2
        i,j = [c,c]
        t1 = r / 16
        x = r + i
        y = 0 + j
        
        while x>=y:
          u[x][y] = 1
          u[y][x] = 1
          u[dim-y-1][x] = 1
          u[dim-x-1][y] = 1
          u[dim-x-1][dim-y-1] = 1
          u[dim-y-1][dim-x-1] = 1
          u[y][dim-x-1] = 1
          u[x][dim-y-1] = 1
          y += 1
          t1 = t1 + y
          t2 = t1 - x
          if t2 >= 0:
            t1 = t2
            x = x - 1
        return u
      
      else:
        return print("Circle out of bounds. Diameter greater than dim.")
    else:
      return print(f"Radius {r} less than zero.")
  else:
    return print(f"{dim} is even. Only odd numbers.")


# print(np.array(circumference(11,5),dtype='float'))
