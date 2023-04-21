#
# Attempt to give poster ordering for each person to visit
#
# Seth McNeill
# 2014 April 09

import random
import sys

# Np = 17
# Ns = 4

# takes list of lists, checks each element for duplicates
# returns true if no duplicates found
def checkDups(L): 
  for ii in L:
    if(len(ii) != len(set(ii))):
      return False
  return True

# takes a list of lists, L, and a list of numbers, A,
# the same length as the list of lists
# returns true of none of the numbers in A at ii are 
# in the list at ii.
def checkAssign(L, A):
  for ii in range(len(L)):
    Li = L[ii][:] # to make a new variable, otherwise it changes L
    Li.append(A[ii])
    if(len(Li) != len(set(Li))):
      return False
  return True

if(len(sys.argv) < 3):
  print("Usage: python order.py [number of posters] [number for each to grade]")
  sys.exit()

Np = int(sys.argv[1])
Ns = int(sys.argv[2])
okay = False
while(not okay):
  p = []
  for ii in range(1,Ns+1):
    a = list(range(1,Np+1))
    random.shuffle(a)
    p.append(a)

  q = []
  for ii in range(0,len(p[0])):
    r = []
    for jj in range(0,len(p)):
      r.append(p[jj][ii])
    q.append(r)
  okay = checkDups(q)

okay = False
while(not okay):
  A = list(range(1,Np+1))
  random.shuffle(A)
  okay = checkAssign(q, A)

niceOut = []
for ii in range(Np):
  niceOut.append([A[ii], q[ii]])
#  print A[ii],
#  print ' grades ',
#  print q[ii]

s = sorted(niceOut, key=lambda n: n[0])

for ii in range(Np):
  print(f'{str(s[ii][0])} grades {str(s[ii][1])}')
