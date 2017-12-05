## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal (object):
	pass

## Animal has-a Dog
class Dog(Animal):
	def __init__(self, name):
		## Dog has-a name
		self.name = name

## Animal has-a Cat
class Cat(Animal):
	def __init__(self, name):
		## Cat has-a name
		self.name = name

## Person is-a object
class Person(object):
	def __init__(self, name):
		## Person has-a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Person has-a Enployee
class Employee(Person):
	def __init__(self, name, salary):
		## hmm what is this strange magic
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary

## Fish is-a object
class Fish(object):
	pass 

## Fish has-a Salmon
class Salmon(Fish):
	pass

## Rover is a Dog	
rover = Dog("Rover")

## Satan is-a Cat
satan = Cat("Satan")

## Mary is a Person
mary = Person("Mary")



