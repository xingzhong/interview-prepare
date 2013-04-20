import pdb
# binary tree
class btree(object):
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def add_left(self, data):
    self.left = btree(data)
    return self.left

  def add_right(self, data):
    self.right = btree(data)
    return self.right

  def left(self):
    return self.left

  def right(self):
    return self.right

  def data(self):
    return self.data

  def traverse(self, node=None):
    if not node :
      node = self
    print "[",
    print node.data,
    if node.left:
      self.traverse(node=node.left)
    if node.right:
      self.traverse(node=node.right)
    print "]",

  def walk(self, x=None):
    if not x:
      x = self
    if x.left:
      self.walk(x=x.left)
    print x.data
    if x.right:
      self.walk(x=x.right)

  def depth(self):
    if not (self.left or self.right):
      return 1
    d1 = 0
    d2 = 0
    if self.left:
      d1 = 1 + self.left.depth()
    if self.right:
      d2 = 1 + self.right.depth()
    return max(d1, d2)

  def leafs(self):
    if not (self.left or self.right):
      return 1
    num = 0
    if self.left:
      num = num + self.left.leafs()
    if self.right:
      num = num + self.right.leafs()
    return num

  def max(self):
    if self.right:
      return self.right.max()
    else:
      return self.data

  def min(self):
    if self.left:
      return self.left.min()
    else:
      return self.data

  def search(self, x):
    if self.data == x:
      return self
    elif self.data > x:
      if not self.left:
        self.left.search(x)
      else:
        return None
    elif self.data < x:
      if not self.right:
        self.right.search(x)
      else:
        return None

  def insert(self, data):
    if data < self.data:
      if self.left :
        self.left.insert(data)
      else:
        self.left = btree(data)
    else:
      if self.right :
        self.right.insert(data)
      else:
        self.right = btree(data)

  @staticmethod
  def demo():
    from random import randint
    test = [randint(0,100) for x in range (20)]
    tree = None
    for t in test:
      if tree:
        tree.insert(t)
      else:
        tree = btree(t)
    return tree


if __name__ == "__main__":
  t = btree.demo()
  t.traverse()
  print
  print t.max()
  print t.min()
  print t.leafs()
  print t.depth()
