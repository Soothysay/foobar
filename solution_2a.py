def solution(l,t):
  i=0 #start position
  j=0 #finish position
  while (i<=j) and j<len(l):
    if(sum(l[i:(j+1)])==t): #If sum found
      return [i,j]
    elif(sum(l[i:(j+1)])<t):
      j=j+1 #Iterating to find the next element helps the sum or not
    else:
      i=i+1 #If the sum has exceeded, we need to increment our starting postion
      j=max(i,j) #Found while handlng errors
  return [-1,-1]
