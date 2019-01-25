class Point(object):
    
   def __init__(self, x=0, y=0):
      self.x = x
      self.y = y

   def reflect(self):
      self.x = -1 * self.x
      self.y = -1 * self.y

   def distance(self, s):
      return ((s.x-self.x)**2 + (s.y-self.y)**2)**0.5



      
      
