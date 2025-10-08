def calculate_grades(grades):
    return sum(grades)/len(grades)
def check_pass(average):
    if average>=50:
        return("Passed")
    else:
        return("Failed")

students = {
    "Osama": (70, 80, 90),
    "Sara": (50, 45, 55),
    "Ali": (90, 95, 100)
}

for student, grades in students.items():
    print(f"{student}:")
    avg = calculate_grades(grades)
    print(f"The Average is :{avg}")
    print(f"Result :{check_pass(avg)}")