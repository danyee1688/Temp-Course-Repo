import csv

def add_nums_in_file(file_name) -> int:
    ret_val = 0

    with open(file_name, "r") as file:
        for line in file:
            ret_val += int(line)

    return ret_val

def file_append(file_name, text):
    try:
        with open(file_name, "a") as file:
            file.write(text + "\n")
    except:
        print("Error occurred.")

def file_cat(file_name):
    with open(file_name, "r") as file:
        for line in file:
            print(line)

def file_clear(file_name):
    with open(file_name, "w") as file:
        file.write("")

print("Adding numbers...")

result = add_nums_in_file("numbers.txt")

print("Result: " + str(result))
print("Clearing file")

file_clear("numbers.txt")

print("Adding the following numbers to numbers.txt: 10, 10, 20")

file_append("numbers.txt", "10")
file_append("numbers.txt", "10")
file_append("numbers.txt", "20")

print("New numbers.txt: ")

file_cat("numbers.txt")

print("Adding numbers...")

result = add_nums_in_file("numbers.txt")

print("Result: " + str(result))

class Customer:
    name: str
    email: str
    balance: int

    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.balance = balance

def add_customer(customer: Customer):
    with open("CustomerData.txt", "a") as file:
        file.write(customer.name + "," + customer.email + "," + str(customer.balance) + "\n")

def parse_csv(file_name):
    customer_list = []

    with open(file_name, "r") as file:
        csv_reader = csv.reader(file, delimiter=',')

        for line in csv_reader:
            customer = Customer(line[0], line[1], line[2])
            customer_list.append(customer)

    return customer_list

file_clear("CustomerData.txt")

add_customer(Customer("Jane Doe", "janed1@SkillStorm.com", 5709))
add_customer(Customer("Jane Dodger", "janed2@SkillStorm.com", 61))
add_customer(Customer("Jane Darl", "janed3@SkillStorm.com", 8705023))

customer_list = parse_csv("CustomerData.txt")

for index in range(0, len(customer_list)):
    print("Customer " + str(index))
    print("Name: " + customer_list[index].name)
    print("Email: " + customer_list[index].email)
    print("Balance: " + customer_list[index].balance)

print("Confidential information, please do not share.")