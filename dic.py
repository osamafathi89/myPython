person= {
    "name":"Osama",
    "age":36,
    "job":"Developper"
}
person["age"] = 38
person["country"] = "Egypt"
print(person)
person.pop("job")
print(person)
for key,value in person.items():
    print(f"{key}: {value}")