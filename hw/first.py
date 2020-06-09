num=int(input("enter a number:\t"))
n=int(input("enter second number:\t"))
mul=num*n
sqr=num**n
byte=sqr.to_bytes
up=sqr.numerator
down=sqr.denominator
ce=mul.__ceil__()
print(ce)
print(down)
print(up)
print(byte)