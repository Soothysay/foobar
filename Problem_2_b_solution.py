from itertools import combinations
def solution(l):
  l.sort(reverse = True) #sorting the list so as to get the combinations in ascending order
  i=len(l)+1
  while (i>=1):
    for j in combinations(l,i):
      if ((sum(j)%3)==0):
        return int(''.join(map(str,j))) #Returning the tuple in the form of an integer value
    i=i-1
  return 0 # Base case
