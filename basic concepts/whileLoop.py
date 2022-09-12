inp = int(input("ENter number 1 for True and 0 for false"))

if inp == 1:
    flag = True
elif inp == 0:
    flag = False
else:
    print("AWrong in")

while flag:
    print("on")
    inp = int(input("ENter number 1 for True and 0 for false"))

    if inp == 1:
        flag = True
    elif inp == 0:
        flag = False
    else:
        print("AWrong in")