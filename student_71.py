class Student(object):
   
   def __init__(self, surname, forename, sid, modlist = []):
       self.sid = sid
       self.surname = surname
       self.forename = forename
       self.modlist = modlist


   def add_module(self, s):
      if s not in self.modlist:
         self.modlist.append(s)

   def del_module(self, s):
      if s in self.modlist:
         self.modlist.remove(s)


   def print_details(self):
      print('ID: {}'.format(self.sid)) 
      print('Surname: {}'.format(self.surname)) 
      print('Forename: {}'.format(self.forename)) 
      print('Modules: {}'.format(" ".join(self.modlist))) 
