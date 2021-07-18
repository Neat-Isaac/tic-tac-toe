from os import *
def printScreen(l): #l:list
    system('cls')
    print("{}|{}|{}".format(l[0][0],l[0][1],l[0][2]))
    print("-----")
    print("{}|{}|{}".format(l[1][0],l[1][1],l[1][2]))
    print("-----")
    print("{}|{}|{}".format(l[2][0],l[2][1],l[2][2]))
def win(a,x):       #a:list;x:int
    #横向
    if a[0][0] == x and a[0][1] == x and a[0][2] == x:
        return x
    elif a[1][0] == x and a[1][1] == x and a[1][2] == x:
        return x
    elif a[2][0] == x and a[2][1] == x and a[2][2] == x:
        return x
    #纵向
    elif a[0][0] == x and a[1][0] == x and a[2][0] == x:
        return x
    elif a[0][1] == x and a[1][1] == x and a[2][1] == x:
        return x
    elif a[0][2] == x and a[1][2] == x and a[2][2] == x:
        return x
    #斜向
    elif a[0][0] == x and a[1][1] == x and a[2][2] == x:
        return x
    elif a[0][2] == x and a[1][1] == x and a[2][0] == x:
        return x
    #OK
    else:
        return 0