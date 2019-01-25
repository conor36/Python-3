from stack_92 import Stack

def matcher(line):
   s = Stack()
   if len(line) % 2 != 0:
      return False

   parentheses = {
      "(" : ")",
      "{" : "}",
      "[" : "]",
   }

   for ch in line:
      if ch in parentheses.keys():
         s.push(ch)
      elif parentheses[s.top()] == ch:
         s.pop()

   return s.is_empty()
