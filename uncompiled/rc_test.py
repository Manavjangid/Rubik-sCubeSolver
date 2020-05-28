import random
import subprocess

# for random data entry
white=['w','w','w','w','w','w','w','w','w']
blue=['b','b','b','b','b','b','b','b','b']
yellow=['y','y','y','y','y','y','y','y','y']
green=['g','g','g','g','g','g','g','g','g']
orange=['o','o','o','o','o','o','o','o','o']
red=['r','r','r','r','r','r','r','r','r']

sides=[white,blue,yellow,green,orange,red]

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

# Code to shuffling Rubiks cube randomly
print("\nShuffling Cube \n")
while white[1]=='w' or white[3]=='w' or white[5]=='w' or white[7]=='w':
    a=random.randint(1,6)
    b=random.randint(1,3)
    if a==1:
        for i in range(0,b):
            rotate('w')
    elif a==2:
        for i in range(0,b):
            rotate('b')
    elif a==3:
        for i in range(0,b):
            rotate('y')
    elif a==4:
        for i in range(0,b):
            rotate('g')
    elif a==5:
        for i in range(0,b):
            rotate('o')
    else:
        for i in range(0,b):
            rotate('r')
    print('\n')
for i in sides:
    print(i)

with open('rc_test_run.cmd','w') as w:
    w.write('python rc_algorithm.py ')
    for i in sides:
        for j in i:
            w.write(f'{j} ')
    
subprocess.call('rc_test_run.cmd')
subprocess.call(['rm','rc_test_run.cmd'])