import pdb
class linkedList(object):
  def __init__(self, data):
    self.data = data
    self.pointer = None
  
  def insert(self, data):
    new = linkedList(data)
    self.pointer = new
    return new

  def walk(self):
    print self.data
    if self.pointer:
      self.pointer.walk()
 
  def reverse(self):
    return self._reverse(None) 

  def _reverse(self, previous):
    if not self.pointer :
      self.pointer = previous
      return self
    else:
      temp = self.pointer._reverse(self)
      self.pointer = previous
      return temp

  def middle(self):
    x = self.pointer.pointer
    y = self.pointer
    while(x):
      y = y.pointer
      if x.pointer:
        x = x.pointer.pointer
      else:
        break
    print y.data
    return y


if __name__ == "__main__":
  l = linkedList(-1)
  x = l
  for i in range(6):
    x = x.insert(i)

  l.walk()
  print 
  l = l.reverse()
  print 
  l.middle()

