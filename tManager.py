class Character(object):
  def __init__(self, name, age, goals):
    self.name = name
    self.age = age
    self.goals = goals
  def printStats(self):
    print("Name:" + self.name)
    print("Age:" + self.age)
    print("Goals:" + self.goals)
myCharacter = []

print("Welcome! Do you wish to add a player to ShawnHigh scoccer team or would you like to view the players? Enter 1 to add player or enter 2 to view them.")
option = input()


while option != "0":
  if option == "1":
    print("Looks like you want to add a player, please enter the information below.")
    print("Name:")
    name = input()
    print("Age in numbers:")
    age = input()
    print("Number of goals they have scored:")
    goals = input()
    myCharacter.append(Character(name, age, goals))
    print("Okay we are done! Do you want to option #1, add another player or do you want option #2, to see the stats?")
    option = input()
  elif option == "2":
    print("okay looks like you want to see the stats.")
    for info in myCharacter:
        info.printStats()
    option = input()
