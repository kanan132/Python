a=[]
for i in range(1,101):
    
    if i%3==0:
        if i%5==0:
            a.append("FizzBuzz")
        else:
            a.append("fizz")
    elif i%3==0:
        a.append("fizz")
    elif i%5==0:
        a.append("buzz")
    
    else: 
        a.append("nothing")
print(a)
b=a.count("fizz")
c=a.count("buzz")
d=a.count("FizzBuzz")
print(f"{b}-fizz")
print(f"{c}-buzz")
print(f"{d}-FizzBuzz")