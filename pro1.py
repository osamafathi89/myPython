student = {
    "name":"osama",
    "age":36,
    "grades":(85,90,78,92,88),
    "passed_subjects" : {"Math","Science","English","History"}
}
avg = (sum(student["grades"])/len(student["grades"]))
print(f"The average = {avg} ")
print(f"Passed subjects:{student['passed_subjects']}")
print(f"Is math passed ?{'Math' in student['passed_subjects']}")
