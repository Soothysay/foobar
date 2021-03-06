def solution(x,y):
  x,y=int(x), int(y)
  optimizer= 0
  while x> 1 and y> 1:
    x,y=min(x,y),max(x,y) # As default we are assuming y to be the bigger one as it will be the dividend
    optimizer+= y//x # We are just counting the level of tree we have reached
    y=y%x 
  x,y=min(x,y),max(x,y) # In case impossible condition is hit
  if x== 1:
    return str(optimizer+(y//x)-1) 
  else:
    return 'impossible'
