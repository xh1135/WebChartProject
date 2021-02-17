from model import Employee

e = Employee()
e.first_name = 'marc'
e.salary = 1000

f = Employee()
f.first_name = 'marc'
f.salary = 1000

print(f > e)
