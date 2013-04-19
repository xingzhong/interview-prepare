class Player(object):
  def __init__(self):
    self._dict = {}
  def addPoints(self, user, points):
    p = self._dict.setdefault(user, [])
    self._dict[user].append(points)
  def getTotalPoints(self, user):
    return sum(self._dict.get(user, []))

if __name__ == "__main__":
  p = Player()
  p.addPoints("John", 10)
  p.addPoints("Xu", 5)
  print p._dict
  print p.getTotalPoints("John")
