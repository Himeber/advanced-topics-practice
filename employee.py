class Employee:
    def __init__(self,name,title):
        self.name = name
        self.title = title
    def __str__(self):
        return f"{self.name} - {self.title}"
def greeting():
    print(f'Hello from the "employee.py" file :D')