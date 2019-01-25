class Stack(object):
   def __init__(self):
      self.l = []

   def push(self, n):
      self.l.append(n)

   def pop(self):
      return self.l.pop()

   def top(self):
      return self.l[-1]

   def is_empty(self):
      return not len(self.l)

   def __len__(self):
      return len(self.l)