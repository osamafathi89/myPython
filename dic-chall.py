student = {
    "name": "Sara",
    "grades": [80, 90, 85]
}
for k,v in student.items():
    if k =="grades":
     avg = 0 
     for g in student[k]: 
      avg+= g 
     avg= avg/len(student[k]) 
     print(f"The average = {avg}") 
    else: 
        print(f"{k}:{v}")