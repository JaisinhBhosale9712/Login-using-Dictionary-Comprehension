User=[(0,"Jay","Password"),(1,"Jayb","Password1"),(2,"Jayc","123")] #Database
dict_comprehension={Userdetails[1]:Userdetails for Userdetails in User}  #Create Dist Comprehension

#print(x for x,y,z in dict_comprehension["Jay"]))  cant use this as dictcomp is not iterable

username=input("Enter your id")
try:
    dict_comprehension[username]
    pasword=input("Enter your Password")
    x,y,z=dict_comprehension[username]
    if z==str(paswordd):
            print("Login Succesfull")
    else:
            print("Invalid Password")

except KeyError:
   print("ID doesnt exist")

 #   password=input("Enter your Password")



