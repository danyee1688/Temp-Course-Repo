
class Person:
    name: str
    age: int

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self, text):
        print("(No Position) " + self.name + ": " + text)

    def return_age(self):
        return self.age

class Developer(Person):
    salary: int
    language: str

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language

    def speak(self, text):
        print("(Developer) " + self.name + ": " + text)

    def print_report(self, show_salary=False):
        if show_salary:
            print(self.name + " uses " + self.language + " and makes " + str(self.salary) + " dollars per year")
        else:
            print(self.name + " uses " + self.language)

JohnObj = Developer("John Doe", "200k", "Python")
MaryObj = Developer("Mary Jane", "2", "NetLogo")
DudeObj = Person("Dude Guy", 22)

JohnObj.speak("Hello World! It'sa me, Mario")
JohnObj.print_report()
MaryObj.speak("Hello World! Please let me know what my salary is!")
MaryObj.print_report(True)
DudeObj.speak("How do you make so little Mary, I feel bad...")
MaryObj.speak("I just need 7 dollars for Spotify Premium, " + DudeObj.name + "!")
