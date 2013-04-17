# heap 
import pdb
from tree import btree

class heap(list):
  def __init__(self, *args, **kwargs):
    list.__init__(self, *args, **kwargs)
    self[0] = -1
    for i in range(len(self), 0, -1):
      self.max_heapify(i)

  def left(self, index):
    return 2*index
  def right(self, index):
    return 2*index+1
  def parent(self, index):
    return index//2

  def max_heapify(self, i):
    l = self.left(i)
    r = self.right(i)
    if l < len(self) and self[l] > self[i]:
      large = l
    else:
      large = i
    if r < len(self) and self[r] > self[large]:
      large = r
    if large != i:
      self[i], self[large] = self[large], self[i]
      self.max_heapify(large)

  def sort(self):
    for i in range(len(self)-1, 0, -1):
      self[i], self[1] = self[1], self[i]
      yield self.pop()
      self.max_heapify(1)

if __name__ == "__main__":
  from random import randint
  h = heap([randint(0,100) for x in range(10)])
  print h
  print list(h.sort())
  
