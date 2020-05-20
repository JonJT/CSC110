# Write a function find_hypot which, given the length of two sides of a right-angled
# triangle, returns the length of the hypotenuse. (Hint: x ** 0.5 will return the square
# root.)


def find_hypot(a,b):  
  cSq = a**2 + b**2  
  c = cSq ** 0.5  
  return (c)


print(find_hypot(3,4))