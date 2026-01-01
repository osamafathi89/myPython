name = "   osama   "
print(name.strip().title())

data = [
      "   Revise to variable,loops,if,function,string,file,dictionary \n  ",
      "   Learn python from 0 to hero   \n",
        "   I love python programming   \n"
]
with open("revision/revision.txt", "w") as file:
    for line in data:
        file.write(line.strip() + "\n")
