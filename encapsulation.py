#protected encapsulation
class Employee:
    def __init__(self):
        #protected variable
        self._hourly = 0
#defining obj as class Employee
obj = Employee()
#obj will replace the 'self' in the self._hourly and assign it a value of 24
obj._hourly = 24
#printing the output of obj._hourly which should be 24
print(obj._hourly)


#private encapsulation
class Employee:
    def __init__(self):
        
        #private variable
        self.__title = " "

obj = Employee()
obj.__title = "Manager"
print(obj.__title)
