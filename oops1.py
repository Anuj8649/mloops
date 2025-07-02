#initiate a class
class employee:
    #special method/magic method /dunder method--constructor
    def __init__(self):
        print('statrted executing attributes/data')
        self.id = 123
        self.salary = 50000
        self.designation = 'sde'
        print('attributes have been initiated')
#function inside the class is called method
    def travel(self, destination):
        print("this travel function was called amnually")
        print(f"employee is travelling to {destination}")    



#create an object/instance of the class
sam = employee()
sam.name= "sam kumar"
lam=employee()
#both have different id

print(sam.name)
print(id(sam))
print(id(lam))

print(sam.salary)
print(sam.id)
sam.travel("kerala")
print(type(sam))

print(lam.salary)
print(lam.id)
lam.travel("siliguri")
print(type(lam))