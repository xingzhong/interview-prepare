class Player(object):
  def __init__(self):
    self._dict = {}
  def addPoints(self, user, points):
    p = self._dict.setdefault(user, [])
    self._dict[user].append(points)
  def getTotalPoints(self, user):
    return sum(self._dict.get(user, []))

from datetime import datetime
class leader (dict):
  def addPoints(self, user, point):
    if self.has_key(user):
      self[user]["pointer"] = self[user]["pointer"] + 1
      if self[user]["pointer"] > 7 :
        self[user]["pointer"] = 0
      self[user]["points"][self[user]["pointer"]] = point
    else:
      self[user] = {}
      self[user]["points"] = [point, 0, 0, 0, 0, 0, 0]
      self[user]["pointer"] = 0
    self[user]['timestamp'] = datetime.now()

  def getTotalPoints(self, user):
    return sum( self[user]["points"] )

if __name__ == "__main__":
  p = Player()
  p.addPoints("John", 10)
  p.addPoints("Xu", 5)
  print p._dict
  print p.getTotalPoints("John")

  l = leader()
  l.addPoints("Xu", 5)
  l.addPoints("Xu", 6)
  l.addPoints("John", 4)

  print l

  print l.getTotalPoints("Xu")
