import sys

mark = 0

try:
   with open(sys.argv[1], 'r') as f:
      for line in f:
         if int(line.strip().split()[0]) > int(mark):
            mark = line.strip().split()[0]
            student = line.strip().split()[1:]

   s = ''
   for word in student:
      s = s + word + ' '

   print('Best student: ' + s.strip())
   print('Best mark: ' + mark)
except:
   print('The file students.txtt could not be opened.')
