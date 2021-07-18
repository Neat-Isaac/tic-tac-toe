from random import *
def space(ax,ay,bx,by,cx,cy,l,x,r):
    if l[ax][ay] == x and l[bx][by] == x and l[cx][cy] == ' ':
        l[cx][cy] = x
        r = 1
    elif l[ax][ay] == x and l[cx][cy] == x and l[bx][by] == ' ':
        l[bx][by] = x
        r = 1
    elif l[bx][by] == x and l[cx][cy] == x and l[ax][ay] == ' ':
        l[ax][ay] = x
        r = 1
def space1(ax,ay,bx,by,cx,cy,l,x,r):
    b = 0
    if x == 'x':
        b = 'o'
    else:
        b = 'x'
    if l[ax][ay] == x and l[bx][by] == x and l[cx][cy] == ' ':
        l[cx][cy] = b
        r = 1
    elif l[ax][ay] == x and l[cx][cy] == x and l[bx][by] == ' ':
        l[bx][by] = b
        r = 1
    elif l[bx][by] == x and l[cx][cy] == x and l[ax][ay] == ' ':
        l[ax][ay] = b
        r = 1
def isline(l,x):
    a = 0
    space(0,0,0,1,0,2,l,x,a)
    if a == 0:
        space(1,0,1,1,1,2,l,x,a)
        if a == 0:
            space(2,0,2,1,2,2,l,x,a)
            if a == 0:
                space(0,0,1,0,2,0,l,x,a)
                if a == 0:
                    space(0,1,1,1,2,1,l,x,a)
                    if a == 0:
                        space(0,2,1,2,2,2,l,x,a)
                        if a == 0:
                            space(0,0,1,1,2,2,l,x,a)
                            if a == 0:
                                space(0,2,1,1,2,0,l,x,a)
                                if a == 0:
                                    isline1(l,x)
def isline1(l,x):
    a = 0
    space1(0,0,0,1,0,2,l,x,a)
    if a == 0:
        space1(1,0,1,1,1,2,l,x,a)
        if a == 0:
            space1(2,0,2,1,2,2,l,x,a)
            if a == 0:
                space1(0,0,1,0,2,0,l,x,a)
                if a == 0:
                    space1(0,1,1,1,2,1,l,x,a)
                    if a == 0:
                        space1(0,2,1,2,2,2,l,x,a)
                        if a == 0:
                            space1(0,0,1,1,2,2,l,x,a)
                            if a == 0:
                                space1(0,2,1,1,2,0,l,x,a)
                                if a == 0:
                                    gott(l,x)
def gott(l,x):
    i = randint(0,2)
    j = randint(0,2)
    while l[i][j] != ' ':
        i = randint(0,2)
        j = randint(0,2)
    l[i][j] = x