## Animal is-a object (yes sort of confusing) look at the extra credit
class Animal(object):
	pass

 # Dog is-a Animal
 class Dog(Animal):

 	def __init__(self, name):
 		# Has-a name
 		self.name = name

# Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		#has-a name
		self.name = name

# person is-a object
class Person(object):

	def __init__(self, name):
		#has a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

# Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		#has-a name
		super(Employee, self).__init__(name)
		#has-a Salary
		self.salary = salary

# fish is-a object
class Fish(object):
	pass

# Salmon is-a fish
class Salmon(Fish):
	pass

#Halibut is-a fish
class Halibut(Fish):
	pass


## rover is-a Dog
rover = Dog("Rover")

#satan is a cat
satan = cat("Satan")

#many is a person
mary = Person("Mary")

# Mary has a pet
mary.pet = satan

# Frank is an employee and has I name and a salary
frank = Employee("Frank", 120000)

# frank has a pet named rover
frank.pet = rover

# flipper isa fish
flipper = Fish()

# crouse is a Salmon
crouse = Salmon()

# Harry is a halibut
harry = Halibut()

