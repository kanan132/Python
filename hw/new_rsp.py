import random

game = {
    "played": 0,
    "human": 0,
    "computer": 0,
    "tie": 0,
}

def pretty_print_results():
    print(f'Total {game["played"]} games played;\tHuman: {game["human"]};\tComputer: {game["computer"]};\tTie {game["tie"]}.')
    print("-"*60)
def update(value):
    game[value] += 1
    game["played"] = game["human"] + game["computer"] + game["tie"]


def decide_result(human_choice, comp_choice):
    result = {'R': 'S', 'S': 'P', 'P': 'R',}
    if human_choice == comp_choice:
        return "tie"
    elif result[human_choice] == comp_choice:
       return "human"
    else:
       return "computer"





while True:
    human_choice = input("Your choice (q to exit):\t")
    comp_choice = random.choice(['R', 'S', 'P'])
    if human_choice != "q": 
        print(f"Computer chose:{comp_choice}")
        result = decide_result(human_choice, comp_choice)
        update(result)
        print(decide_result(human_choice, comp_choice))
        pretty_print_results()
    else:
        print(f'Good bye. Exiting program.')
        break
    


