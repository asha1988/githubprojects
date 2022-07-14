# Health Management System

def getdate():
    import datetime
    return datetime.datetime.now()

def log():
        print("whose record you want log\n")
        print("1:Asha\n2:Ashok\n3:Satish\n4:Quit\n")
        input1 = int(input())
        if input1 == 1:
            print("what you want to log from Asha\n1:Diet\n2:Exercise\n")
            input2 = int(input())
            if input2 == 1:
                val = input("Enter food\n")
                with open("ashadiet.txt", 'a') as f:
                    f.write(str(str(getdate()) + ":" + val + "\n"))
                    print("successfully added")
            elif input2 == 2:
                val = input("Enter exercise\n")
                with open("ashaexercise.txt", 'a') as f:
                    f.write(str(str(getdate()) + ":" + val + "\n"))
                    print("successfully added")
            else:
                print("invalid input")
        elif input1 == 2:
            print("what you want to log from Ashok\n1:Diet\n2:Exercise\n")
            input7 = int(input())
            if input7 == 1:
                val = input("Enter food\n")
                with open("ashokdiet.txt", 'a') as f:
                    f.write(str(str(getdate()) + ":" + val + "\n"))
                    print("successfully added")
            elif input7 == 2:
                val = input("Enter exercise\n")
                with open("ashokexercise.txt", 'a') as f:
                    f.write(str(str(getdate()) + ":" + val + "\n"))
                print("successfully added")
            else:
                print("invalid input")
        elif input1 == 3:
            print("what you want to log from Satish\n1:Diet\n2:Exercise\n")
            input9 = int(input())
            if input9 == 1:
                val = input("Enter food\n")
                with open("satishdiet.txt", 'a') as f:
                    f.write(str(str(getdate()) + ":" + val + "\n"))
                    print("successfully added")
            elif input9 == 2:
                val = input("Enter exercise\n")
                with open("satishexercise.txt", 'a') as f:
                    f.write(str(str(getdate()) + ":" + val + "\n"))
                print("successfully added")
            else:
                print("Invalid input")
        elif input1 == 4:
            print("Thanks for your input.\nQuitting the process")
            exit()
        else:
            print("invalid input")

def retrieve():
    print("whose record you want to retrieve\n")
    print("1:Asha\n2:Ashok\n3:Satish\n4:Quit\n")
    input3 = int(input())
    if input3 == 1:
        print("what you want to retreive from Asha\n1:Diet\n2:Exercise\n")
        input4 = int(input())
        if input4 == 1:
            f = open("ashadiet.txt")
            for line in f:
                print(line, end="")
            f.close()
        elif input4 == 2:
            f = open("ashaexercise.txt")
            for d in f:
                print(d, end="")
            f.close()
        else:
            print("Sorry wrong input")

    elif input3 == 2:
       print("What you want to retreive from Ashok\n1:Diet\n2:Exercise\n")
       input5 = int(input())
       if input5 == 1:
           f = open("ashokdiet.txt")
           for y in f:
               print(y, end="")
           f.close()
       elif input5 == 2:
           f = open("ashokexercise.txt")
           for x in f:
               print(x, end="")
           f.close()
       else:
           print("sorry wrong input")
    elif input3 == 3:
        print("what you want to retreive from Satish\n1:Diet\n2:Exercise\n")
        input6 = int(input())
        if input6 == 1:
            f = open("satishdiet.txt")
            for a in f:
                print(a, end="")
            f.close()
        elif input6 == 2:
            f = open("satishexercise.txt")
            for b in f:
                print(b, end="")
            f.close()
        else:
            print("invalid input")
    elif input3 == 4:
        print("Thanks for your input.\nQuitting the process")
        exit()
    else:
        print("invalid input")

print("Health Management System")
record = int(input("Do you want to log or retrive 1:Log 2:Retreive\n"))
if record == 1:
    log()
elif record == 2:
    retrieve()
else:
    print("invalid input")
