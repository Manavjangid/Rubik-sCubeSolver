import random
from sys import exit
white=[]
blue=[]
yellow=[]
green=[]
orange=[]
red=[]

# Entering data
def entry():
    print("Enter values of your rubiks cube according to given Image1 and Image2:-")
    white=input("White >> ").split(" ")
    blue=input("blue >> ").split(" ")
    yellow=input("yellow >> ").split(" ")
    green=input("green >> ").split(" ")
    orange=input("ornage >> ").split(" ")
    red=input("red >> ").split(" ")
    print("\n(Caution! Move each colour shown in only clock wise direction)")
    return white,blue,yellow,green,orange,red
white,blue,yellow,green,orange,red=entry()
sides=[white,blue,yellow,green,orange,red]

# copies real rotation of rubiks cube in lists of every side
numbers=1
def rotate(colour):
    global numbers
    if colour=='w':
        print(f'{numbers}. White     |')
        numbers+=1
        rough=white[0]
        white[0]=white[6]
        white[6]=white[8]
        white[8]=white[2]
        white[2]=rough
        rough=white[1]
        white[1]=white[3]
        white[3]=white[7]
        white[7]=white[5]
        white[5]=rough
        rough=green[6]
        green[6]=red[8]
        red[8]=blue[2]
        blue[2]=orange[0]
        orange[0]=rough
        rough=green[7]
        green[7]=red[5]
        red[5]=blue[1]
        blue[1]=orange[3]
        orange[3]=rough
        rough=green[8]
        green[8]=red[2]
        red[2]=blue[0]
        blue[0]=orange[6]
        orange[6]=rough

    elif colour=='b':
        print(f'{numbers}. Blue      |')
        numbers+=1
        rough=blue[0]
        blue[0]=blue[6]
        blue[6]=blue[8]
        blue[8]=blue[2]
        blue[2]=rough
        rough=blue[1]
        blue[1]=blue[3]
        blue[3]=blue[7]
        blue[7]=blue[5]
        blue[5]=rough
        rough=white[6]
        white[6]=red[6]
        red[6]=yellow[6]
        yellow[6]=orange[6]
        orange[6]=rough
        rough=white[7]
        white[7]=red[7]
        red[7]=yellow[7]
        yellow[7]=orange[7]
        orange[7]=rough
        rough=white[8]
        white[8]=red[8]
        red[8]=yellow[8]
        yellow[8]=orange[8]
        orange[8]=rough

    elif colour=='y':
        print(f'{numbers}. Yellow    |')
        numbers+=1
        rough=yellow[0]
        yellow[0]=yellow[6]
        yellow[6]=yellow[8]
        yellow[8]=yellow[2]
        yellow[2]=rough
        rough=yellow[1]
        yellow[1]=yellow[3]
        yellow[3]=yellow[7]
        yellow[7]=yellow[5]
        yellow[5]=rough
        rough=red[0]
        red[0]=green[2]
        green[2]=orange[8]
        orange[8]=blue[6]
        blue[6]=rough
        rough=red[3]
        red[3]=green[1]
        green[1]=orange[5]
        orange[5]=blue[7]
        blue[7]=rough
        rough=red[6]
        red[6]=green[0]
        green[0]=orange[2]
        orange[2]=blue[8]
        blue[8]=rough

    elif colour=='g':
        print(f'{numbers}. Green     |')
        numbers+=1
        rough=green[0]
        green[0]=green[6]
        green[6]=green[8]
        green[8]=green[2]
        green[2]=rough
        rough=green[1]
        green[1]=green[3]
        green[3]=green[7]
        green[7]=green[5]
        green[5]=rough
        rough=red[2]
        red[2]=white[2]
        white[2]=orange[2]
        orange[2]=yellow[2]
        yellow[2]=rough
        rough=red[1]
        red[1]=white[1]
        white[1]=orange[1]
        orange[1]=yellow[1]
        yellow[1]=rough
        rough=red[0]
        red[0]=white[0]
        white[0]=orange[0]
        orange[0]=yellow[0]
        yellow[0]=rough

    elif colour=='o':
        print(f'{numbers}. Orange    |')
        numbers+=1
        rough=orange[0]
        orange[0]=orange[6]
        orange[6]=orange[8]
        orange[8]=orange[2]
        orange[2]=rough
        rough=orange[1]
        orange[1]=orange[3]
        orange[3]=orange[7]
        orange[7]=orange[5]
        orange[5]=rough
        rough=white[8]
        white[8]=blue[8]
        blue[8]=yellow[0]
        yellow[0]=green[8]
        green[8]=rough
        rough=white[5]
        white[5]=blue[5]
        blue[5]=yellow[3]
        yellow[3]=green[5]
        green[5]=rough
        rough=white[2]
        white[2]=blue[2]
        blue[2]=yellow[6]
        yellow[6]=green[2]
        green[2]=rough

    elif colour=='r':
        print(f'{numbers}. Red       |')
        numbers+=1
        rough=red[0]
        red[0]=red[6]
        red[6]=red[8]
        red[8]=red[2]
        red[2]=rough
        rough=red[1]
        red[1]=red[3]
        red[3]=red[7]
        red[7]=red[5]
        red[5]=rough
        rough=white[0]
        white[0]=green[0]
        green[0]=yellow[8]
        yellow[8]=blue[0]
        blue[0]=rough
        rough=white[3]
        white[3]=green[3]
        green[3]=yellow[5]
        yellow[5]=blue[3]
        blue[3]=rough
        rough=white[6]
        white[6]=green[6]
        green[6]=yellow[2]
        yellow[2]=blue[6]
        blue[6]=rough
    
# algorithm for solving Rubiks cube layer by layer are called as and when they are required
def white_corner1(x,y):
    rotate('y')
    rotate('y')
    rotate(x)
    rotate(x)
    rotate(x)
    rotate(y)
    rotate(y)
    rotate(y)
    rotate('y')
    rotate('y')
    rotate(y)
    rotate(x)
    rotate('y')
    rotate('y')
    rotate(x)
    rotate(x)
    rotate(x)
    print("\n")

def white_corner2(x,y):                              
    rotate(x)
    rotate(x)
    rotate(x)
    rotate('y')
    rotate('y')
    if (x=='b' and y=='o') or (x=='g' and y=='r') or (x=='o' and y=='g') or (x=='r' and y=='b'):
        rotate('y')
    rotate(x)
    if (x=='b' and y=='g') or (x=='g' and y=='b') or (x=='o' and y=='r') or (x=='r' and y=='o'):
        rotate('y')
        rotate('y')
    rotate(y)
    rotate('y')
    rotate('y')
    if (x=='b' and y!='r') or (x=='g' and y!='o') or (x=='o' and y!='b') or (x=='r' and y!='g'):
        rotate('y')
    rotate(y)
    rotate(y)
    rotate(y)
    print("\n")

def white_corner3(x,y):
    rotate(x)
    rotate('y')
    if (x=='b' and y=='o') or (x=='g' and y=='r') or (x=='o' and y=='g') or (x=='r' and y=='b'):
        rotate('y')
    rotate(x)
    rotate(x)
    rotate(x)
    if (x=='b' and y=='g') or (x=='g' and y=='b') or (x=='o' and y=='r') or (x=='r' and y=='o'):
        rotate('y')
        rotate('y')
    rotate(y)
    rotate(y)
    rotate(y)
    rotate('y')
    if (x=='b' and y!='r') or (x=='g' and y!='o') or (x=='o' and y!='b') or (x=='r' and y!='g'):
        rotate('y')
    rotate(y)
    print("\n")

def white_corner4(x,y):
    if (x=='b' and (y=='b' or y=='r')) or (x=='g' and (y=='g' or y=='o')) or (x=='o' and (y=='b' or y=='o')) or (x=='r' and (y=='r' or y=='b')):
        rotate('y')
        rotate('y')
    rotate(y)
    rotate('y')
    rotate('y')
    if (x=='b' and (y=='b' or y=='g')) or (x=='g' and (y=='b' or y=='g')) or (x=='o' and (y=='r' or y=='o')) or (x=='r' and (y=='r' or y=='o')):
        rotate('y')
    rotate(y)
    rotate(y)
    rotate(y)
    print("\n")

def white_corner5(x,y):
    if (x=='b' and (y=='o' or y=='b')) or (x=='g' and (y=='r' or y=='g')) or (x=='o' and (y=='o' or y=='g')) or (x=='r' and (y=='b' or y=='r')):
        rotate('y')
        if y=='o' or y=='r' or y=='g' or y=='b':
            rotate('y')
    rotate(y)
    rotate(y)
    rotate(y)
    rotate('y')
    if (x=='b' and y!='g') or (x=='g' and y!='b') or (x=='o' and y!='r') or (x=='r' and y!='o'):
        rotate('y')
    rotate(y)
    print("\n")

def white_corner6(a,b,x,y):
    rotate(x)
    rotate('y')
    if (a=='bo' and b==6) or (a=='rb' and b==0) or (a=='gr' and b==2) or (a=='og' and b==8):
        rotate('y')
    rotate(x)
    rotate(x)
    rotate(x)
    if (a=='bo' and b==0) or (a=='rb' and b==2) or (a=='gr' and b==8) or (a=='og' and b==6):
        rotate('y')
        rotate('y')
    rotate(y)
    rotate('y')
    rotate('y')
    if (a=='bo' and b!=2) or (a=='rb' and b!=8) or (a=='gr' and b!=6) or (a=='og' and b!=0):
        rotate('y')
    rotate(y)
    rotate(y)
    rotate(y)
    print("\n")

def mid_layer1(x,y,z):
    if (x==green and y!='b') or (x==orange and y!='r') or (x==red and y!='o') or (x==blue and y!='g'):
        rotate('y')
        if (x==green and (y=='r' or y=='g')) or (x==orange and (y=='g' or y=='o')) or (x==red and (y=='b' or y=='r')) or (x==blue and (y=='o' or y=='b')):
            rotate('y')
            if (x==green and y=='r') or (x==orange and y=='g') or (x==red and y=='b') or (x==blue and y=='o'):
                rotate('y')
    rotate(y)
    if (y=='o' and z=='b') or (y=='b' and z=='r') or (y=='r' and z=='g') or (y=='g' and z=='o'):
        rotate(y)
        rotate(y)
    rotate('y')
    if (y=='b' and z=='o') or (y=='r' and z=='b') or (y=='g' and z=='r') or (y=='o' and z=='g'):
        rotate('y')
        rotate('y')
    rotate(y)
    if (y=='b' and z=='o') or (y=='r' and z=='b') or (y=='g' and z=='r') or (y=='o' and z=='g'):
        rotate(y)
        rotate(y)
    rotate('y')
    rotate('y')
    rotate(z)
    if (y=='b' and z=='o') or (y=='r' and z=='b') or (y=='g' and z=='r') or (y=='o' and z=='g'):
        rotate(z)
        rotate(z)
    rotate('y')
    rotate('y')
    rotate(z)
    if (y=='o' and z=='b') or (y=='b' and z=='r') or (y=='r' and z=='g') or (y=='g' and z=='o'):
        rotate(z)
        rotate(z)
    print("\n")

def mid_layer2(a,b,c,d):
    if a!=c or b!=d:
        rotate(c)
        if (c=='b' and d=='r') or (c=='r' and d=='g') or (c=='g' and d=='o') or (c=='o' and d=='b'):
            rotate(c)
            rotate(c)
        rotate('y')
        rotate('y')
        rotate(c)
        if (c=='b' and d=='o') or (c=='r' and d=='b') or (c=='g' and d=='r') or (c=='o' and d=='g'):
            rotate(c)
            rotate(c)
        rotate('y')
        rotate('y')
        rotate(d)
        if (c=='b' and d=='o') or (c=='r' and d=='b') or (c=='g' and d=='r') or (c=='o' and d=='g'):
            rotate(d)
            rotate(d)
        rotate('y')
        if (c=='b' and d=='o') or (c=='r' and d=='b') or (c=='g' and d=='r') or (c=='o' and d=='g'):
            rotate('y')
            rotate('y')
        rotate(d)
        if (c=='b' and d=='r') or (c=='r' and d=='g') or (c=='g' and d=='o') or (c=='o' and d=='b'):
            rotate(d)
            rotate(d)
        if (a=='o' and b=='b' and c!='r' and d!='b') or (a=='b' and b=='r' and c!='g' and d!='r') or (a=='r' and b=='g' and c!='o' and d!='g') or (a=='g' and b=='o' and c!='b' and d!='o'):
            rotate('y')
            if (a=='o' and b=='b' and ((c=='r' and d=='g') or (c=='o' and d=='g') or (c=='g' and d=='o') or (c=='b' and d=='o'))) or (a=='b' and b=='r' and ((c=='g' and d=='o') or (c=='b' and d=='o') or (c=='o' and d=='b') or (c=='r' and d=='b'))) or (a=='r' and b=='g' and ((c=='o' and d=='b') or (c=='r' and d=='b') or (c=='b' and d=='r') or (c=='g' and d=='r'))) or (a=='g' and b=='o' and ((c=='b' and d=='r') or (c=='g' and d=='r') or (c=='r' and d=='g') or (c=='o' and d=='g'))):
                rotate('y')
                if (a=='o' and b=='b' and ((c=='g' and d=='o') or (c=='b' and d=='o'))) or (a=='b' and b=='r' and ((c=='o' and d=='b') or (c=='r' and d=='b'))) or (a=='r' and b=='g' and ((c=='b' and d=='r') or (c=='g' and d=='r'))) or (a=='g' and b=='o' and ((c=='r' and d=='g') or (c=='o' and d=='g'))):
                    rotate('y')
        rotate(b)
        rotate('y')
        rotate('y')
        rotate('y')
        rotate(b)
        rotate(b)
        rotate(b)
        rotate('y')
        rotate('y')
        rotate(a)
        rotate(a)
        rotate(a)
        rotate('y')
        rotate('y')
        rotate(a)
        print("\n")

def yellow_cross1(a,b):
    rotate(a)
    rotate('y')
    rotate(b)
    rotate('y')
    rotate('y')
    rotate('y')
    rotate(b)
    rotate(b)
    rotate(b)
    rotate(a)
    rotate(a)
    rotate(a)
    print("\n")

def yellow_cross2(a):
    rotate(a)
    rotate('y')
    rotate(a)
    rotate(a)
    rotate(a)
    rotate('y')
    rotate(a)
    rotate('y')
    rotate('y')
    rotate(a)
    rotate(a)
    rotate(a)
    print("\n")

def yellow_corner1(x,y,a,b):
    rotate('y')
    if (a==1 and b==3) or (a==3 and b==2) or (a==0 and b==1) or (a==2 and b==0):
        rotate('y')
        rotate('y')
        rotate(x)
        rotate(x)
    rotate(x)
    rotate('y')
    if (a==2 and b==3) or (a==0 and b==2) or (a==3 and b==1) or (a==1 and b==0):
        rotate('y')
        rotate('y')
        rotate(y)
        rotate(y)
    rotate(y)
    rotate('y')
    if (a==1 and b==3) or (a==3 and b==2) or (a==0 and b==1) or (a==2 and b==0):
        rotate('y')
        rotate('y')
    else:
        rotate(x)
        rotate(x)
    rotate(x)
    rotate('y')
    if (a==2 and b==3) or (a==0 and b==2) or (a==3 and b==1) or (a==1 and b==0):
        rotate('y')
        rotate('y')
    else:
        rotate(y)
        rotate(y)
    rotate(y)
    print("\n")

def yellow_corner2(a,b,c,d):
    rotate(a)
    rotate(c)
    rotate(c)
    rotate(c)
    rotate(a)
    rotate(a)
    rotate(a)
    rotate(b)
    rotate(b)
    rotate(b)
    rotate(c)
    rotate(c)
    rotate(c)
    rotate(b)
    rotate(d)
    rotate(b)
    rotate(b)
    rotate(b)
    rotate(c)
    rotate(b)
    rotate(a)
    rotate(c)
    rotate(a)
    rotate(a)
    rotate(a)
    rotate(d)
    rotate(d)
    rotate(d)
    print("\n")

# solving rubiks cube layer by layer:-
# 1. White Cross
# 2. White Corner
# 3. Middle Layer
# 4. yellow Cross
# 5. Yellow Corners
class White_Cross():
    sides=[white,blue,yellow,green,orange,red]

    def enter(self):
        self.edge_peices()
        self.edge_align()
        return 'white_corner'

    # Function to make plus sign on white side
    def edge_peices(self):
        print("\nwhite Cross Edge Peices:- \n")
        while 'w'!= white[1] or 'w'!=white[3] or 'w'!=white[5] or 'w'!=white[7]:
            for i in self.sides[1:6]:
                for j in range(1,8,2):
                    if i[j]=='w':
                        if i==yellow:
                            if j == 7:
                                while white[j]=='w':
                                    rotate('w')
                                rotate('b')
                                rotate('b')
                            elif j == 1:
                                while white[j]=='w':
                                    rotate('w')
                                rotate('g')
                                rotate('g')
                            elif j == 3:
                                b=5
                                while white[b]=='w':
                                    rotate('w')
                                rotate('o')
                                rotate('o')
                            elif j == 5:
                                b=3
                                while white[b]=='w':
                                    rotate('w')
                                rotate('r')
                                rotate('r')     
                            
                        elif i==blue:
                            if j == 3:
                                while white[j]=='w':
                                    rotate('w')
                                rotate('r')
                                rotate('r')
                                rotate('r')
                            elif j == 5:
                                while white[j]=='w':
                                    rotate('w')
                                rotate('o')
                            elif j == 1:
                                b=5
                                rotate('b')
                                while white[b]=='w':
                                    rotate('w')
                                rotate('o')
                            elif j == 7:
                                b=3
                                while white[j]=='w':
                                    rotate('w')
                                rotate('b')
                                while white[b]=='w':
                                    rotate('w')
                                rotate('r')
                                rotate('r')
                                rotate('r')
                        
                        elif i==green:
                            if j == 3:
                                while white[j]=='w':
                                    rotate('w')
                                rotate('r')
                            elif j == 5:
                                while white[j]=='w':
                                    rotate('w')
                                rotate('o')
                                rotate('o')
                                rotate('o')
                            elif j == 7:
                                b=3
                                rotate('g')
                                while white[b]=='w':
                                    rotate('w')
                                rotate('r')
                            elif j == 1:
                                b=5
                                while white[j]=='w':
                                    rotate('w')
                                rotate('g')
                                while white[b]=='w':
                                    rotate('w')
                                rotate('o')
                                rotate('o')
                                rotate('o')
                            
                        elif i==orange:
                            if j == 1:
                                while white[j]=='w':
                                    rotate('w')
                                rotate('g')
                            elif j == 7:
                                while white[j]=='w':
                                    rotate('w')
                                rotate('b')
                                rotate('b')
                                rotate('b')
                            elif j == 3:
                                b=1
                                rotate('o')
                                while white[b]=='w':
                                    rotate('w')
                                rotate('g')
                            elif j == 5:
                                b=7
                                while white[j]=='w':
                                    rotate('w')
                                rotate('o')
                                while white[b]=='w':
                                    rotate('w')
                                rotate('b')
                                rotate('b')
                                rotate('b')

                        elif i == red:
                            if j == 1:
                                while white[j]=='w':
                                    rotate('w')
                                rotate('g')
                                rotate('g')
                                rotate('g')
                            elif j == 7:
                                while white[j]=='w':
                                    rotate('w')
                                rotate('b')
                            elif j == 5:
                                b=7
                                rotate('r')
                                while white[b]=='w':
                                    rotate('w')
                                rotate('b')
                            elif j == 3:
                                b=1
                                while white[j]=='w':
                                    rotate('w')
                                rotate('r')
                                while white[b]=='w':
                                    rotate('w')
                                rotate('g')
                                rotate('g')
                                rotate('g')
             
    # Function to align white edge peices
    def edge_align(self):
        print("\nwhite Cross Edge Align:- \n")
        blue[1]+='a'
        red[5]+='a'
        green[7]+='a'
        orange[3]+='a'
        while blue[1]!='ba':
            rotate('w')
        if red[5]!='ra':
            if 'ra'==green[7]:
                rotate('g')
                rotate('g')
                while red[3]!='ra':
                    rotate('y')
                if 'ga'==red[5]:
                    rotate('r')
                    rotate('r')
                    while green[1]!='ga':
                        rotate('y')
                    if green[7]=='oa':
                        rotate('g')
                        rotate('g')
                        while orange[5]!='oa':
                            rotate('y')
                        rotate('o')
                        rotate('o')
                    else:
                        rotate('g')
                        rotate('g')
                elif 'oa'==red[5]:
                    rotate('r')
                    rotate('r')
                    while orange[5]!='oa':
                        rotate('y')
                    if orange[3]=='ga':
                        rotate('o')
                        rotate('o')
                        while green[1]!='ga':
                            rotate('y')
                        rotate('g')
                        rotate('g')
                    else:
                        rotate('o')
                        rotate('o')
                else:
                    rotate('r')
                    rotate('r')
            elif 'ra'==orange[3]:
                rotate('o')
                rotate('o')
                while red[3]!='ra':
                    rotate('y')
                if 'ga'==red[5]:
                    rotate('r')
                    rotate('r')
                    while green[1]!='ga':
                        rotate('y')
                    if green[7]=='oa':
                        rotate('g')
                        rotate('g')
                        while orange[5]!='oa':
                            rotate('y')
                        rotate('o')
                        rotate('o')
                    else:
                        rotate('g')
                        rotate('g')
                elif 'oa'==red[5]:
                    rotate('r')
                    rotate('r')
                    while orange[5]!='oa':
                        rotate('y')
                    if orange[3]=='ga':
                        rotate('o')
                        rotate('o')
                        while green[1]!='ga':
                            rotate('y')
                        rotate('g')
                        rotate('g')
                    else:
                        rotate('o')
                        rotate('o')
                else:
                    rotate('r')
                    rotate('r')
        if green[7]!='ga':
            if 'ga'==red[5]:
                rotate('r')
                rotate('r')
                while green[1]!='ga':
                    rotate('y')
                if 'ra'==green[7]:
                    rotate('g')
                    rotate('g')
                    while red[3]!='ra':
                        rotate('y')
                    if red[5]=='oa':
                        rotate('r')
                        rotate('r')
                        while orange[5]!='oa':
                            rotate('y')
                        rotate('o')
                        rotate('o')
                    else:
                        rotate('r')
                        rotate('r')
                elif 'oa'==green[7]:
                    rotate('g')
                    rotate('g')
                    while orange[5]!='oa':
                        rotate('y')
                    if orange[3]=='ra':
                        rotate('o')
                        rotate('o')
                        while red[3]!='ra':
                            rotate('y')
                        rotate('r')
                        rotate('r')
                    else:
                        rotate('o')
                        rotate('o')
                else:
                    rotate('g')
                    rotate('g')
            elif 'ga'==orange[3]:
                rotate('o')
                rotate('o')
                while green[1]!='ga':
                    rotate('y')
                if 'ra'==green[7]:
                    rotate('g')
                    rotate('g')
                    while red[3]!='ra':
                        rotate('y')
                    if red[5]=='oa':
                        rotate('r')
                        rotate('r')
                        while orange[5]!='oa':
                            rotate('y')
                        rotate('o')
                        rotate('o')
                    else:
                        rotate('r')
                        rotate('r')
                elif 'oa'==green[7]:
                    rotate('g')
                    rotate('g')
                    while orange[5]!='oa':
                        rotate('y')
                    if orange[3]=='ra':
                        rotate('o')
                        rotate('o')
                        while red[5]!='ra':
                            rotate('y')
                        rotate('r')
                        rotate('r')
                    else:
                        rotate('o')
                        rotate('o')
                else:
                    rotate('g')
                    rotate('g')

class White_Corner():
    sides=[white,blue,yellow,green,orange,red]

    def enter(self):
        self.corner_peices()
        return 'middle_layer'

    # Function to Arrange corner peices on White side    
    def corner_peices(self):
        print("\nwhite Corners:- \n")
        z=1
        while z<=10:
            z+=1
            for i in range(0,9):
                if yellow[i]=='w' and i==0:
                    if green[2]=='b' and orange[2]=='o':
                        rotate('b')
                        rotate('y')
                        white_corner1('b','o')
                    elif green[2]=='r' and orange[2]=='b':
                        rotate('r')
                        white_corner1('r','b')
                    elif green[2]=='g' and orange[2]=='r':
                        rotate('y')
                        rotate('y')
                        rotate('g')
                        rotate('y')
                        white_corner1('g','r')
                    elif green[2]=='o' and orange[2]=='g':
                        rotate('y')
                        rotate('o')
                        rotate('y')
                        white_corner1('o','g')
                
                if yellow[i]=='w' and i==2:
                    if red[0]=='b' and green[0]=='o':
                        rotate('b')
                        white_corner1('b','o')
                    elif red[0]=='r' and green[0]=='b':
                        rotate('y')
                        rotate('y')
                        rotate('r')
                        rotate('y')
                        white_corner1('r','b')
                    elif red[0]=='g' and green[0]=='r':
                        rotate('y')
                        rotate('g')
                        rotate('y')
                        white_corner1('g','r')
                    elif red[0]=='o' and green[0]=='g':
                        rotate('o')
                        rotate('y')
                        white_corner1('o','g')

                if yellow[i]=='w' and i==6:
                    if orange[8]=='b' and blue[8]=='o':
                        rotate('y')
                        rotate('b')
                        rotate('y')
                        white_corner1('b','o')
                    elif orange[8]=='r' and blue[8]=='b':
                        rotate('r')
                        rotate('y')
                        white_corner1('r','b')
                    elif orange[8]=='g' and blue[8]=='r':
                        rotate('g')
                        white_corner1('g','r')
                    elif orange[8]=='o' and blue[8]=='g':
                        rotate('y')
                        rotate('y')
                        rotate('o')
                        rotate('y')
                        white_corner1('o','g')

                if yellow[i]=='w' and i==8:
                    if blue[6]=='b' and red[6]=='o':
                        rotate('y')
                        rotate('y')
                        rotate('b')
                        rotate('y')
                        white_corner1('b','o')
                    elif blue[6]=='r' and red[6]=='b':
                        rotate('y')
                        rotate('r')
                        rotate('y')
                        white_corner1('r','b')
                    elif blue[6]=='g' and red[6]=='r':
                        rotate('g')
                        rotate('y')
                        white_corner1('g','r')
                    elif blue[6]=='o' and red[6]=='g':
                        rotate('o')
                        white_corner1('o','g')
                        
                if blue[i]=='w' and i==0:
                    if white[6]=='b' and red[8]=='o':
                        white_corner2('b','b')
                    elif white[6]=='r' and red[8]=='b':
                        white_corner2('b','r')
                    elif white[6]=='g' and red[8]=='r':
                        white_corner2('b','g')
                    elif white[6]=='o' and red[8]=='g':
                        white_corner2('b','o')

                if blue[i]=='w' and i==2:
                    if orange[6]=='b' and white[8]=='o':
                        white_corner3('b','o')
                    elif orange[6]=='r' and white[8]=='b':
                        white_corner3('b','b')
                    elif orange[6]=='g' and white[8]=='r':
                        white_corner3('b','r')
                    elif orange[6]=='o' and white[8]=='g':
                        white_corner3('b','g')

                if blue[i]=='w' and i==6:
                    if red[6]=='b' and yellow[8]=='o':
                        white_corner4('b','b')
                    elif red[6]=='r' and yellow[8]=='b':
                        white_corner4('b','r')
                    elif red[6]=='g' and yellow[8]=='r':
                        white_corner4('b','g')
                    elif red[6]=='o' and yellow[8]=='g':
                        white_corner4('b','o')

                if blue[i]=='w' and i==8:
                    if yellow[6]=='b' and orange[8]=='o':
                        white_corner5('b','o')
                    elif yellow[6]=='r' and orange[8]=='b':
                        white_corner5('b','b')
                    elif yellow[6]=='g' and orange[8]=='r':
                        white_corner5('b','r')
                    elif yellow[6]=='o' and orange[8]=='g':
                        white_corner5('b','g')
                
                if green[i]=='w' and i==0:
                    if yellow[2]=='b' and red[0]=='o':
                        white_corner5('g','o')
                    elif yellow[2]=='r' and red[0]=='b':
                        white_corner5('g','b')
                    elif yellow[2]=='g' and red[0]=='r':
                        white_corner5('g','r')
                    elif yellow[2]=='o' and red[0]=='g':
                        white_corner5('g','g')
                
                if green[i]=='w' and i==2:
                    if orange[2]=='b' and yellow[0]=='o':
                        white_corner4('g','b')
                    elif orange[2]=='r' and yellow[0]=='b':
                        white_corner4('g','r')
                    elif orange[2]=='g' and yellow[0]=='r':
                        white_corner4('g','g')
                    elif orange[2]=='o' and yellow[0]=='g':
                        white_corner4('g','o')

                if green[i]=='w' and i==6:
                    if red[2]=='b' and white[0]=='o':
                        white_corner3('g','o')
                    elif red[2]=='r' and white[0]=='b':
                        white_corner3('g','b')
                    elif red[2]=='g' and white[0]=='r':
                        white_corner3('g','r')
                    elif red[2]=='o' and white[0]=='g':
                        white_corner3('g','g')

                if green[i]=='w' and i==8:
                    if white[2]=='b' and orange[0]=='o':
                        white_corner2('g','b')
                    elif white[2]=='r' and orange[0]=='b':
                        white_corner2('g','r')
                    elif white[2]=='g' and orange[0]=='r':
                        white_corner2('g','g')
                    elif white[2]=='o' and orange[0]=='g':
                        white_corner2('g','o')

                if orange[i]=='w' and i==0:
                    if green[8]=='b' and white[2]=='o':
                        white_corner3('o','o')
                    elif green[8]=='r' and white[2]=='b':
                        white_corner3('o','b')
                    elif green[8]=='g' and white[2]=='r':
                        white_corner3('o','r')
                    elif green[8]=='o' and white[2]=='g':
                        white_corner3('o','g')

                if orange[i]=='w' and i==2:
                    if yellow[0]=='b' and green[2]=='o':
                        white_corner5('o','o')
                    elif yellow[0]=='r' and green[2]=='b':
                        white_corner5('o','b')
                    elif yellow[0]=='g' and green[2]=='r':
                        white_corner5('o','r')
                    elif yellow[0]=='o' and green[2]=='g':
                        white_corner5('o','g')

                if orange[i]=='w' and i==6:
                    if white[8]=='b' and blue[2]=='o':
                        white_corner2('o','b')
                    elif white[8]=='r' and blue[2]=='b':
                        white_corner2('o','r')
                    elif white[8]=='g' and blue[2]=='r':
                        white_corner2('o','g')
                    elif white[8]=='o' and blue[2]=='g':
                        white_corner2('o','o')

                if orange[i]=='w' and i==8:
                    if blue[8]=='b' and yellow[6]=='o':
                        white_corner4('o','b')
                    elif blue[8]=='r' and yellow[6]=='b':
                        white_corner4('o','r')
                    elif blue[8]=='g' and yellow[6]=='r':
                        white_corner4('o','g')
                    elif blue[8]=='o' and yellow[6]=='g':
                        white_corner4('o','o')

                if red[i]=='w' and i==0:
                    if green[0]=='b' and yellow[2]=='o':
                        white_corner4('r','b')
                    elif green[0]=='r' and yellow[2]=='b':
                        white_corner4('r','r')
                    elif green[0]=='g' and yellow[2]=='r':
                        white_corner4('r','g')
                    elif green[0]=='o' and yellow[2]=='g':
                        white_corner4('r','o')

                if red[i]=='w' and i==2:
                    if white[0]=='b' and green[6]=='o':
                        white_corner2('r','b')
                    elif white[0]=='r' and green[6]=='b':
                        white_corner2('r','r')
                    elif white[0]=='g' and green[6]=='r':
                        white_corner2('r','g')
                    elif white[0]=='o' and green[6]=='g':
                        white_corner2('r','o')

                if red[i]=='w' and i==6:
                    if yellow[8]=='b' and blue[6]=='o':
                        white_corner5('r','o')
                    elif yellow[8]=='r' and blue[6]=='b':
                        white_corner5('r','b')
                    elif yellow[8]=='g' and blue[6]=='r':
                        white_corner5('r','r')
                    elif yellow[8]=='o' and blue[6]=='g':
                        white_corner5('r','g')

                if red[i]=='w' and i==8:
                    if blue[0]=='b' and white[6]=='o':
                        white_corner3('r','o')
                    elif blue[0]=='r' and white[6]=='b':
                        white_corner3('r','b')
                    elif blue[0]=='g' and white[6]=='r':
                        white_corner3('r','r')
                    elif blue[0]=='o' and white[6]=='g':
                        white_corner3('r','g')
            
                if white[i]=='w' and i==0:
                    if green[6]=='b' and red[2]=='o':
                        white_corner6('bo',0,'g','b')
                    elif green[6]=='r' and red[2]=='b':
                        white_corner6('rb',0,'g','r')
                    elif green[6]=='o' and red[2]=='g':
                        white_corner6('og',0,'g','o')

                if white[i]=='w' and i==2:
                    if orange[0]=='b' and green[8]=='o':
                        white_corner6('bo',2,'o','b')
                    elif orange[0]=='r' and green[8]=='b':
                        white_corner6('rb',2,'o','r')
                    elif orange[0]=='g' and green[8]=='r':
                        white_corner6('gr',2,'o','g')

                if white[i]=='w' and i==6:
                    if red[8]=='b' and blue[0]=='o':
                        white_corner6('bo',6,'r','b')
                    elif red[8]=='g' and blue[0]=='r':
                        white_corner6('gr',6,'r','g')
                    elif red[8]=='o' and blue[0]=='g':
                        white_corner6('og',6,'r','o')

                if white[i]=='w' and i==8:
                    if blue[2]=='r' and orange[6]=='b':
                        white_corner6('rb',8,'b','r')
                    elif blue[2]=='g' and orange[6]=='r':
                        white_corner6('gr',8,'b','g')
                    elif blue[2]=='o' and orange[6]=='g':
                        white_corner6('og',8,'b','o')

class Middle_Layer():
    edges=[['o','b'],['b','r'],['r','g'],['g','o']]
    edges1=['',green,'',orange,'',red,'',blue]
    edges2=[[orange,blue],[blue,red],[red,green],[green,orange]]

    def enter(self):
        self.middle_peices()
        return 'yellow_cross'  

    # Functin to arrange Middle Layer on the Rubiks Cube     
    def middle_peices(self):
        print("\nMiddle Layer:-\n")
        zz=0
        while zz<10:
            zz+=1
            for i in self.edges:
                for j in range(1,8,2):
                    if yellow[j]==i[0]:
                        sa=self.edges1[j]
                        if j==1 or j==7:
                            a=j
                        elif j==3:
                            a=5
                        elif j==5:
                            a=3
                        if sa[a]==i[1]:
                            mid_layer1(sa,i[0],i[1])
                    elif yellow[j]==i[1]:
                        sa=self.edges1[j]
                        if j==1 or j==7:
                            a=j
                        elif j==3:
                            a=5
                        elif j==5:
                            a=3
                        if sa[a]==i[0]:
                            mid_layer1(sa,i[1],i[0])
            for i in self.edges:
                for j in self.edges2:
                    if j[0]==orange:
                        a=7
                        c='o'
                    elif j[0]==blue:
                        a=3
                        c='b'
                    elif j[0]==red:
                        a=1
                        c='r'
                    elif j[0]==green:
                        a=5
                        c='g'
                    if j[1]==blue:
                        b=5
                        d='b'
                    elif j[1]==red:
                        b=7
                        d='r'
                    elif j[1]==green:
                        b=3
                        d='g'
                    elif j[1]==orange:
                        b=1
                        d='o'
                    if j[0][a]==i[0]:
                        if j[1][b]==i[1]:
                            mid_layer2(i[0],i[1],c,d)
                    if j[0][a]==i[1]:
                        if j[1][b]==i[0]:
                            mid_layer2(i[0],i[1],d,c)
       
class Yellow_Cross():
    edges=[1,7]
    edges1=[3,5]
    edges2=[[orange,5,'o'],[blue,7,'b'],[red,3,'r'],[green,1,'g']]

    def enter(self):
        self.edge_peices()
        self.edge_align()
        return 'yellow_corner'

    # Function to Create Plus Sign on Yellow Side    
    def edge_peices(self):
        print("\nYellow Cross Edge Peices:- \n")
        if yellow[1]!='y' and yellow[3]!='y' and yellow[5]!='y' and yellow[7]!='y':
            yellow_cross1('o','b')
        if (yellow[1]=='y' and yellow[7]=='y' and yellow[5]!='y' and yellow[3]!='y') or (yellow[5]=='y' and yellow[3]=='y' and yellow[1]!='y' and yellow[7]!='y'):
            yellow_cross1('o','b')
        for i in self.edges:
            for j in self.edges1:
                if yellow[i] =='y' and yellow[j] == 'y'and (yellow[1]!='y' or yellow[3]!='y' or yellow[5]!='y' or yellow[7]!='y'):
                    if i==1 and j==3:
                        a='b'
                        b='r'
                    elif i==1 and j==5:
                        a='o'
                        b='b'
                    elif i==7 and j==3:
                        a='r'
                        b='g'
                    elif i==7 and j==5:
                        a='g'
                        b='o'
                    yellow_cross1(a,b)
    
    # Function to align edge peices of yellow side
    def edge_align(self):
        print("\nYellow Cross Edge Align:- \n")
        count=0
        while count<2:
            count=0
            count1=[]
            for i in self.edges2:
                if i[0][i[1]]==i[2]:
                    count1+=i[2]
                    count+=1
            if count >=2:
                if count!=3 and count!=4:
                    if count1[0]=='o' and count1[1]=='g':
                        a='g'
                    else:
                        a=count1[0]
                    yellow_cross2(a)
                    if orange[5]=='g' and green[1]=='r' and red[3]=='b' and blue[7]=='o':
                        rotate('y')
                    if (count1[0]=='b' and count1[1]=='g') or (count1[0]=='o' and count1[1]=='r'):
                        count=0
            else:
                rotate('y')

class Yellow_Corner():
    corner=[['y','g','o'],['y','r','g'],['y','o','b'],['y','b','r']]
    corner1=[[yellow,green,orange],[yellow,red,green],[yellow,orange,blue],[yellow,blue,red]]
    corner2=[[0,2,2],[2,0,0],[6,8,8],[8,6,6]]
    result=[]
    edges=[[1,0,2,3],[3,1,0,2],[0,2,3,1],[2,3,1,0]]
    edges1=[['o','r'],['r','o'],['g','b'],['b','g']]

    def enter(self):
        self.corner_peices()
        self.corner_align()
        return 'finish'

    # Function to arrange Corner peices of yellow side
    def corner_peices(self):
        print("\nYellow corner peices:- \n")
        for zzz in range(0,4):
            first=[]
            first+=[self.corner1[zzz][0][self.corner2[zzz][0]],self.corner1[zzz][1][self.corner2[zzz][1]],self.corner1[zzz][2][self.corner2[zzz][2]]]
            self.result.append(first)
        a=0
        b=0
        e=0
        i=0
        while i<4:
            j=self.corner[i]
            k=self.result[i]
            for l in j:
                for m in k:
                    if l==m:
                        a+=1
                        break
            if a==3:
                e=i
                b+=1
            a=0
            if i==3 and b==0:
                yellow_corner1('g','b',1,3)
                i=0
                self.result.clear()
                for zzz in range(0,4):
                    first=[]
                    first+=[self.corner1[zzz][0][self.corner2[zzz][0]],self.corner1[zzz][1][self.corner2[zzz][1]],self.corner1[zzz][2][self.corner2[zzz][2]]]
                    self.result.append(first)
            i+=1
        if b==1:
            x=0
            y=0
            z=0
            for i in self.edges:
                if e==i[1]:
                    j=self.corner[i[3]]
                    k=self.result[i[0]]
                    l=self.result[i[2]]
                    o=self.result[i[3]]
                    for m in j:
                        for n in o:
                            if m==n:
                                z+=1
                                break
                    if z!=3:
                        for m in j:
                            for n in k:
                                if m==n:
                                    x+=1
                                    break
                        if x==3:
                            if i[0]==1 and i[3]==3:
                                c='g' 
                                d='b'
                            elif i[0]==3 and i[3]==2:
                                c='r' 
                                d='o'
                            elif i[0]==0 and i[3]==1:
                                c='o' 
                                d='r'
                            else:
                                c='b' 
                                d='g'
                            yellow_corner1(c,d,i[0],i[3])
                        else:
                            for m in j:
                                for n in l:
                                    if m==n:
                                        y+=1
                                        break
                            if y==3:
                                if i[2]==2 and i[3]==3:
                                    c='o' 
                                    d='r'
                                elif i[2]==0 and i[3]==2:
                                    c='g' 
                                    d='b'
                                elif i[2]==3 and i[3]==1:
                                    c='b' 
                                    d='g'
                                else:
                                    c='r' 
                                    d='o'
                                yellow_corner1(c,d,i[2],i[3])

    # Function to align corner peices on yellow side
    def corner_align(self):
        print("\nYellow corner align:- \n")
        sides=[blue,orange,green,red,yellow,yellow,yellow,yellow]
        sides1=[[6,8],[2,8],[2,0],[6,0],[0,2],[0,6],[2,8],[6,8]]
        sides2=['y','y','y','y','g','o','r','b']
        sides3=[['o','b','w','y'],['g','o','w','y'],['r','g','w','y'],['b','r','w','y'],['o','y','b','g'],['b','y','r','o'],['g','y','o','r'],['r','y','g','b']]
        sides4=['b','o','g','r']
        i=0
        while i<8:
            if sides[i][sides1[i][0]]==sides2[i] and sides[i][sides1[i][1]]==sides2[i]:
                yellow_corner2(sides3[i][0],sides3[i][1],sides3[i][2],sides3[i][3])
            i+=1
        i=0
        while i<4:
            if (sides[i][sides1[i][0]]==sides2[i] and sides[i][sides1[i][1]]!=sides4[i]) or (sides[i][sides1[i][1]]==sides2[i] and sides[i][sides1[i][0]]!=sides4[i]):
                yellow_corner2(sides3[i][0],sides3[i][1],sides3[i][2],sides3[i][3])
            i+=1
        i=0
        while i<8:
            if sides[i][sides1[i][0]]==sides2[i] and sides[i][sides1[i][1]]==sides2[i]:
                yellow_corner2(sides3[i][0],sides3[i][1],sides3[i][2],sides3[i][3])
            i+=1
        self.result.clear()
        for zzz in range(0,4):
            first=[]
            first+=[self.corner1[zzz][0][self.corner2[zzz][0]],self.corner1[zzz][1][self.corner2[zzz][1]],self.corner1[zzz][2][self.corner2[zzz][2]]]
            self.result.append(first)
        if (self.corner[0]==self.result[0]) and (self.corner[3]==self.result[3]):
            i=0
            while i<4:
                if sides[i][sides1[i][1]]=='y':
                    yellow_corner2(sides3[i][0],sides3[i][1],sides3[i][2],sides3[i][3])
                    j=0
                    while j<4:
                        if sides[j][sides1[j][0]]==sides2[j] and sides[j][sides1[j][1]]==sides2[j]:
                            yellow_corner2(sides3[j][0],sides3[j][1],sides3[j][2],sides3[j][3])
                        j+=1
                i+=1
        if (self.corner[1]==self.result[1]) and (self.corner[2]==self.result[2]):
            i=1
            while i<3:
                if sides[i][sides1[i][0]]=='y':
                    yellow_corner2(sides3[i][0],sides3[i][1],sides3[i][2],sides3[i][3])
                    j=0
                    while j<4:
                        if sides[j][sides1[j][0]]==sides2[j] and sides[j][sides1[j][1]]==sides2[j]:
                            yellow_corner2(sides3[j][0],sides3[j][1],sides3[j][2],sides3[j][3])
                        j+=1
                i+=1

# Class to finish the solving of rubiks cube
class Finish():
    white=['w','w','w','w','w','w','w','w','w']
    blue=['b','b','b','b','b','b','b','b','b']
    yellow=['y','y','y','y','y','y','y','y','y']
    green=['g','g','g','g','g','g','g','g','g']
    orange=['o','o','o','o','o','o','o','o','o']
    red=['r','r','r','r','r','r','r','r','r']

    def enter(self):
        print('Your Rubiks Cube is solved:-')
        print(self.white)
        print(self.blue)
        print(self.yellow)
        print(self.green)
        print(self.orange)
        print(self.red)
        print("\nQuit??? YES/NO")
        a=input(">")
        if a=="Yes":
            exit(1)
        else:
            print("Nothing Is Left to do so I am Quiting")
            b=input("")

# Class to run the all other classes sequentially
class Engine():
    stages={
        'white_cross':White_Cross(),
        'white_corner':White_Corner(),
        'middle_layer':Middle_Layer(),
        'yellow_cross':Yellow_Cross(),
        'yellow_corner':Yellow_Corner(),
        'finish':Finish()
        }
    def __init__(self,current_stage):
        self.current_stage=current_stage
    def begin(self):
        while 1:
            cs=self.stages.get(self.current_stage)
            self.current_stage=cs.enter()

# Starting point
play=Engine('white_cross')
play.begin()