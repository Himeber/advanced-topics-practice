from employee import Employee,greeting
from app import App
from csv import reader

emp = Employee("Marcia","VP of Sales")

print(emp)
greeting()

apps = []

with open('applist.csv') as csv_file:
    csv_reader = reader(csv_file,delimiter=',')
    next(csv_reader)
    for name,description,category in csv_reader:
        apps.append(App(name,description,category))

for app in apps:
    print(app)