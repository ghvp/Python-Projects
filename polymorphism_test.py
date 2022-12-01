#Parent class
class Animal:
    species = ''
    age = 0

    def get_info(self):
        info = '\nSpecies: {}\nAge: {}'.format(self.species,self.age)
        return info


#child class
class Cat:
    species = 'Feline'
    age = 2
    whiskers = True
    pupils = 'Vertical'

    #adding additional info to the function
    def get_info(self):
        info = '\nSpecies: {}\nAge: {}\nWhiskers: {}\nPupils: {}'.format(self.species,self.age,self.whiskers,self.pupils)
        return info

#child class
class Dog:
    species = 'Canine'
    age = 5
    sound = 'Bark'
    breed = 'Pitbull'

    #adding additional info to the function
    def get_info(self):
        info = '\nSpecies: {}\nAge: {}\nSound: {}\nBreed: {}'.format(self.species,self.age,self.sound,self.breed)
        return info




if __name__ == '__main__':
    cat = Cat()
    print(cat.get_info())

    dog = Dog()
    print(dog.get_info())

        
    
