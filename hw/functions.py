name =input("enter your name:\t")
activity=input(f"what do you like to do {name}:\n")
examine="are you sure about this:\t"
choice=input(examine.capitalize())
answer="you are not allowed"
if choice.lower()=="yes":
    print(f"so you are excited {name} to do {activity}" )
    print(answer.replace("not","very"))
else:
    print(answer.upper())
