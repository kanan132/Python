import random
l=["R","S","P"]

played=0
human=0
comp=0
tie=0
while True:
    choice=input("enter your choice(Rock=>R,Scissors=>S,Paper=>P):\t")
    comp_choice=random.choice(l)
    if choice=="R":
        if comp_choice=="R":
            played+=1
            tie+=1
            print(f"Computer chose:{comp_choice}")
            print("Tie!")
            print(f"Played game:{played}\tHuman:{human}\tComputer:{comp}\tTie:{tie}")
        elif comp_choice=="S":
            played+=1
            human+=1
            print(f"Computer chose:{comp_choice}")
            print("Human wins!")
            print(f"Played game:{played}\tHuman:{human}\tComputer:{comp}\tTie:{tie}")
        elif comp_choice=="P":
            played+=1
            comp+=1
            print(f"Computer chose:{comp_choice}")
            print("Computer wins!")
            print(f"Played game:{played}\tHuman:{human}\tComputer:{comp}\tTie:{tie}")
    elif choice=="S":
        if comp_choice=="R":
            played+=1
            comp+=1
            print(f"Computer chose:{comp_choice}")
            print("Computer wins!")
            print(f"Played game:{played}\tHuman:{human}\tComputer:{comp}\tTie:{tie}")
        elif comp_choice=="S":
            played+=1
            tie+=1
            print(f"Computer chose:{comp_choice}")
            print("Tie!")
            print(f"Played game:{played}\tHuman:{human}\tComputer:{comp}\tTie:{tie}")
        elif comp_choice=="P":
            played+=1
            human+=1
            print(f"Computer chose:{comp_choice}")
            print("Human wins!")
            print(f"Played game:{played}\tHuman:{human}\tComputer:{comp}\tTie:{tie}")
    elif choice=="P":
        if comp_choice=="R":
            played+=1
            human+=1
            print(f"Computer chose:{comp_choice}")
            print("Human wins!")
            print(f"Played game:{played}\tHuman:{human}\tComputer:{comp}\tTie:{tie}")
        elif comp_choice=="S":
            played+=1
            comp+=1
            print(f"Computer chose:{comp_choice}")
            print("Computer wins!")
            print(f"Played game:{played}\tHuman:{human}\tComputer:{comp}\tTie:{tie}")
        elif comp_choice=="P":
            played+=1
            tie+=1
            print(f"Computer chose:{comp_choice}")
            print("Tie!")
            print(f"Played game:{played}\tHuman:{human}\tComputer:{comp}\tTie:{tie}")
    elif choice=="exit":
        break
    else:
        print("Please informed that game ends and try again!")
        break
    
