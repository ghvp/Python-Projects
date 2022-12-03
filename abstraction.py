#importing the needed modules for abstraction
from abc import ABC, abstractmethod
#creating the parent class
class greeting(ABC):
    def greeting1(self, name):
        print("Hi {}! How are you doing today?".format(name))
#abstract method added to greet_per
    @abstractmethod   
    def greet_per(self, name):
        #passing the method since there is no implementation 
        pass


#child class
class to_who(greeting):
    #defining implementation for a shared method between the child and parent class
    def greet_per(self, name):
        print('This greeting was addressed to {}'.format(name))


obj = to_who()
obj.greeting1('Chris')
obj.greet_per('Chris')
        

    
    
