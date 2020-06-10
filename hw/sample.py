for i in range(1,101):
    
    if i%15==0:
        print(f"{i}-FizzBuzz")
    elif i%3==0:
        print(f"{i}-fizz")
    elif i%5==0:
        print(f"{i}-buzz")
    
    else: 
        print(f"{i}-nothing")
