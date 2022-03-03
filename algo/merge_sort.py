import numpy as np

def merge(l1, l2):
  out = []
  
  while 0 not in [len(l1), len(l2)]:
    if l1[0] < l2[0]:
      out.append(l1.pop(0))
    else:
      out.append(l2.pop(0))
  
  if len(l1) != 0:
    out.extend(l1)
  else:
    out.extend(l2)
  
  return out

def sort(l):
  if len(l) == 1:
    return l
  
  cut = len(l) // 2
  left = l[:cut]
  right = l[cut:]
  left = sort(left)
  right = sort(right)
  
  return merge(left, right)
  
print(sort(np.random.randn(())))