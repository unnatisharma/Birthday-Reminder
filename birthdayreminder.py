dict={}
while True:
    print("---***---BIRTHDAY REMINDER---***---:)")
    print("1. Check Birthday Date")
    print("2. Add New Birthday")
    print("3. Exit")
    choice=int(input("Enter your choice : "))
    if(choice == 1):
        if (dict.keys()==0):
            print("Nothing to show")
        else:
            name=input("Enter the name to search for Birthday : ")
            birthday=dict.get(name,"No search found")
            print(birthday)
    elif(choice == 2):
        name=input("Enter the name : ")
        date=input("Enter Birth Date : ")
        dict[name]=date
        print("Birthday Added")
    elif(choice == 3):
        quit()
    else:
        print("option not valid :(")
