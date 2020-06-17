import time
d={ "AHMAD": {
        "name":"AHMAD",
        "phone":"0505555555",
        "occupation":"SCIENTIST"
        },
    "LAMIYA":{
        "name":"LAMIYA",
        "phone":"0512741258",
        "occupation":"DOCTOR"
        },
    "KANAN":{
        "name":"KANAN",
        "phone":"0515944411",
        "occupation":"ENGINEER"
        },
    "GAFUR":{
        "name":"GAFUR",
        "phone":"055334803",
        "occupation":"SOLDIER"
        }
    
}

def adding_info(cont,name,phone,occupation):
    d[cont]={"name":name,"phone":phone,"occupation":occupation}
    return d


def demonstration(cont):
   
    print(f"Name:\t {d[cont][name]}")
    print(f"Phone:\t {d[cont][phone]}")
    print(f"Occupation:\t {d[cont][occupation]}")
    print("-"*40)

while True:
    
    name=input("Enter a name or exit:\t")
    if name.upper() in d.keys():
        demonstration(name.upper())
    elif name.upper()=="EXIT":
        a=time.sleep(1)
        print(f"Exiting program...")
        break
    else:
        confirm=input("There is no named person like this in contact and\n if you want add this name in contact enter 'yes':\t")
        if confirm.lower()=="yes":
            prenom=input("Enter name:\t")
            num=input("Enter number:\t")
            occup=input("Enter occupation:\t")
            adding_info(name.upper(),prenom.upper(),phone,occup.upper())
        else:
            a=time.sleep(1)
            print(f"Exiting program...")
            break

            
        
