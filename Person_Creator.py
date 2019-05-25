import time
import sys

class Person():
    
    def __init__(self):
        self.name = ''
        self.height = ''
        self.weight = 0
        self.mood = 'happy' # default mood is "happy"
        self.family = ''
        self.aquaintances = ''
        self.calories = 1000
        
    def eat(self):
        food = input("What do you want to eat? apple or doughnut? ")
        def weight_gain(self):
            if self.calories >= 2000:
                self.weight += 2
        if food.lower() == "apple":
            self.calories += 95
            weight_gain(self)
            print(f"{person_1.name} eats the apple")
            time.sleep(2)
            print("It is delicious")
            time.sleep(3)
        elif food.lower() == "doughnut":
            self.calories += 240
            weight_gain(self)
            print(f"{person_1.name} eats the doughnut")
            time.sleep(2)
            print("Yum!!")
            time.sleep(3)  
    
    def go_to_sleep(self):
        print(f"{self.name} is sleeping...")
        time.sleep(20)
        print(f"{self.name} is now awake!")
        time.sleep(3)
        
    def exercise(self):
        while True:
            minutes = int(input("How many minutes do you want to exercise for? "))
            ex_type = input("What kind of exercise? running, bicycling, yoga? ")
            if ex_type == "running":
                met_value = 7
                break
            elif ex_type == "bicycling":
                met_value = 5.5
                break
            elif ex_type == "yoga":
                met_value = 3
                break
            else:
                print("Please choose running, bicycling, or yoga.")
        print("Exercising...")
        time.sleep(minutes)
        print("That was a great workout!")
        weight_loss_rate = ((round(self.weight/2.205))*met_value)/60
        work_out = round((weight_loss_rate*minutes))
        self.calories -= work_out
        print(f"{work_out} Calories Burned!")
        def weight_loss(self):
            if work_out >= 400:
                self.weight -= 2
        weight_loss(self)
        time.sleep(3)



# Create a person
while True:
    start_input = input("Would you like to create a new person? y or n? ")
    if start_input.lower() == "y":
        user_name = input("What is your person called? ")
        user_height = input("How tall is your person? x'x\" ")
        while True:
            user_weight = int(input("What is your person's weight? "))
            if 50 <= user_weight <= 500:
                break
            elif 500 < user_weight < 50:
                print("Please choose a weight that's possible for adult humans")
            else:
                print("Please enter a number")
        break
    elif start_input.lower() == "n":
        print("Ok, maybe next time!")
        sys.exit()
    else:
        print("Please make a valid entry")


person_1 = Person()
print("Making person...")
time.sleep(4)
print(f"{user_name} has been created!")
time.sleep(2)


# Person1 attributes
person_1.name = user_name
person_1.height = user_height
person_1.weight = user_weight
person_1.mood = "happy"
# person1.family = {"mother": "Diana",
#                   "father": "Bill",
#                   "wife": "Jill"}
# person1.aquaintances = {"mailman": "Jimmy",
#                         "boss": "Mr. Higgins",
#                         "best friends": ['Tom', 'Andy', 'Suzie', 'Luke'],
#                         "grocery store guy": "Harvey"}

print(person_1.name)
print(person_1.height)
print(person_1.weight)

while True:
    main_menu = input("\n###### Main Menu ######\n\nWhat would you like to do now?\n\neat,\n\nsleep,\n\nexercise,\n\nexit\n\n--> ")
    if main_menu.lower() == "eat":
        person_1.eat()
    elif main_menu.lower() == "sleep":
        person_1.go_to_sleep()
    elif main_menu.lower() == "exercise":
        person_1.exercise()
    elif main_menu.lower() == "exit":
        print("See you next time!")
        time.sleep(2)
        sys.exit()
    else:
        print("Please make a valid entry")
