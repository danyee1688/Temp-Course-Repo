grade = int(input("Enter a grade to determine which letter grade it equals to: "))

while type(grade) != int:
    grade = int(input("Enter a grade to determine which letter grade it equals to: "))

if grade >= 90:
    letter_grade = "A"
elif grade >= 80 and grade <= 89:
    letter_grade = "B"
elif grade >= 70 and grade <= 79:
    letter_grade = "C"
elif grade >= 60 and grade <= 69:
    letter_grade = "D"
elif grade <= 60:
    letter_grade = "F"

print("Letter grade: " + letter_grade)
print("-----------------------------")

for i in range(0, 11):
    print(i)

print("-----------------------------")

groceries = ["milk", "eggs", "bread", "butter", "bacon"]
groceries.append("yogurt")
groceries.append("mini peanut butter cups from Trader Joes")

for i in groceries:
    i += "ay"
    print(i)

print(groceries)

for index in range(0, len(groceries)):
    groceries[index] += "ay"

print(groceries)

print("-----------------------------")

name_list = []
name_input = input("Enter a name, type done when finished: ")
name_list.append(name_input)

while name_input != "done":
    name_input = input("Enter a name, type done when finished: ")
    name_list.append(name_input)

name_list.remove("done")
set_name_list = tuple(name_list)

if (len(set_name_list) == 0):
    print("Looks like no names were typed")
else:
    print("This is a tuple containing all the names:")
    print(set_name_list)

print("-----------------------------")

mailing_list = {
    "Dan StateFarm": "dan@statefarm.com",
    "Garfield Cat": "garfield@lasagna.com",
    "Jake StateFarm": "jake@statefarm.com",
}

mailing_list["Jane StateFarm"] = "jane@statefarm.com"

print("Here is the email for Jake, from StateFarm: " + mailing_list["Jake StateFarm"])

