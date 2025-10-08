def  greet_user(name):
    print(f"Hello {name}, Welcome back")

def calculate_average(grades):
    return sum(grades)/len(grades)
def check_pass(average):
    if average>=60:
        print("Passed")
    else:
        print("Failed")
greet_user("Osama")
grades= (50,45,55)
avg=  calculate_average(grades)
print(f"The Average is: {avg}")
check_pass(avg)
def check_age(age):
    if age>=18:
        print("Adult")
    else:
        print("Minor")
check_age(20)
check_age(15)

avg = calculate_average((80,90,100))
print(avg)