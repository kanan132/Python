for i in range(1,101):
    
    if i%2==0:
        print("nothing")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    elif i%6==0:
        print("fizz")
    elif i%15==0:
        print("buzz")
    else:
        print("nothing")
