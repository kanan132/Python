import time
d={"AHMAD": "0505555555","LAMIYA":"0512741258","KANAN":"0515944411","GAFUR":"055334803"}
while True:
    
    name=input("enter a name in contact or exit:\t")
    if name.upper() in d.keys():
        number=d[name.upper()]
        print(f"Number of {name} is ->  {number}")
    elif name.upper()=="EXIT":
        a=time.sleep(1)
        print(f"Exiting program...")
        break
    else:
        confirm=input("There is no named person like this in contact and\n if you want add this name in contact enter 'yes':\t")
        if confirm.lower()=="yes":
            num=input("enter number:\t")
            d[f"{name.upper()}"]= f"{num}"
        


        
