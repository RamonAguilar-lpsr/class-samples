class Student(object):

	def _init_(self, name, fave_food, fave_color, current_grade):
		self.name = name
		self.fave_food = fave_food
		self.fave_color = fave_color
		self.current_grade = current_grade

	def setGrade(self, new_grade):
		self.current_grade = new_grade
		

myKarla = Student("Karla", "Turbos", "blue", "A")
myJose = Student("Jose", "pizza", "green", "A")
myHillary = Student("Hillary", "pizza", "green", "C")
print(myJose.fave_food)
myHillary.fave_food = "Burritos"
  
print(myKarla.current_grade)

# change Karla's grade
myKarla.setGrade("F")
print(myKarla.current_grade)
