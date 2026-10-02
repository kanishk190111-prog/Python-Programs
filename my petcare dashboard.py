class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
        self.__health = 100

    
    def get_health(self):
        return self.__health

    
    def set_health(self, amount):
        if 0 <= amount <= 100:
            self.__health = amount
        else:
            print("Health must be between 0 and 100!")

    
    def care_routine(self):
        print(f"Taking general care of {self.name} the {self.species}.")




class Dog(Pet):
    def __init__(self, name):
        super().__init__(name, "Dog")

    
    def care_routine(self):
        print(f" Taking {self.name} for a walk and playing fetch!")


class Cat(Pet):
    def __init__(self, name):
        super().__init__(name, "Cat")

    def care_routine(self):
        print(f" Grooming {self.name} and giving catnip treats!")



dog1 = Dog("Rocky")
cat1 = Cat("Bob")

dashboard_pets = [dog1, cat1]

print("===  Welcome to My Pet Care Dashboard  ===\n")

print("--- Daily Care Routines ---")
for pet in dashboard_pets:
    pet.care_routine()

print("\n--- Health Management (Encapsulation) ---")

print(f"{dog1.name}'s initial health: {dog1.get_health()}%")

dog1.set_health(85)
print(f"{dog1.name}'s updated health: {dog1.get_health()}%")