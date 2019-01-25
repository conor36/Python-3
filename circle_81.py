class Point(object):
 
    def __init__(self, x=0, y=0):
       self.x = x
       self.y = y
 
    def midpoint(self, other):
       return Point((self.x + other.x) / 2, (self.y + other.y) / 2)
 
    def __str__(self):
       return '({:.1f}, {:.1f})'.format(self.x, self.y)
 
class Circle(object):
 
    def __init__(self, centre=Point(0,0), rad=0):
       self.rad = rad
       self.centre = centre
 
    def __add__(self, other):
       centre=self.centre.midpoint(other.centre)
       rad= self.rad + other.rad
       return Circle(centre,rad)
 
    def __str__(self):
       return 'Centre: {}\nRadius: {}'.format(self.centre, self.rad)