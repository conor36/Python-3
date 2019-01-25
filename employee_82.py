class Employee(object):
 
    next_employee_number = 0
 
    def __init__(self, name, num=0, hourly_rate=9.25, hours_worked=0):
       self.name = name
       self.num = Employee.next_employee_number
       self.hourly_rate = hourly_rate
       self.hours_worked = hours_worked
       Employee.next_employee_number += 1
 
    def add_hours(self, other):
       z = self.hours_worked + other
       self.hours_worked = z
       return self
 
    def __str__(self):
    	return 'Name: {}\nID: {}\nHours: {:.2f}\nRate: {:.2f}\nWages: {:.2f}'.format(self.name, self.num, self.hours_worked, self.hourly_rate, (self.hours_worked * self.hourly_rate))