for i in range(1,101):
    
    if i%3==0:
        print(f"{i}-fizz")
    elif i%5==0:
        print(f"{i}-buzz")
    elif i%15==0:
        print(f"{i}-FizzBuzz")
    else: 
        print(f"{i}-nothing")
