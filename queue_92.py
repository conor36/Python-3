class Queue(object):
   def __init__(self):
      self.l = []

   def enqueue(self, n):
      self.l.append(n)

   def dequeue(self):
      return self.l.pop(0)
   
   def first(self):
      return self.l[0]

   def is_empty(self):
      return not len(self.l)

   def __len__(self):
      return len(self.l)