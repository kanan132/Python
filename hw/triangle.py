n=int(input("enter length of triangle:\t"))

sym=input("enter symbol:\t")

def making_triangle(n,sym):
    a=1
    for i in range(n):
        
        print(a*f"{sym}")
        a+=1
making_triangle(n,sym)

    