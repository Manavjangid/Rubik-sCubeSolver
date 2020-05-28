import tkinter as tk 
from tkinter import ttk,messagebox
import subprocess


# Creating tkinter window 
window = tk.Tk() 
window.title('3x3 Rubik\'s Cube Solver') 
window.geometry('610x270') 

# Combobox creation
r1 = ttk.Combobox(window, width = 4)
r1['values'] = ('white','blue','green','orange','red','yellow')
r1.grid(column = 10, row = 2)

r2 = ttk.Combobox(window, width = 4)
r2['values'] = ('white','blue','green','orange','red','yellow')
r2.grid(column = 11, row = 2)

r3 = ttk.Combobox(window, width = 4)
r3['values'] = ('white','blue','green','orange','red','yellow')
r3.grid(column = 12, row = 2)

r4 = ttk.Combobox(window, width = 4)
r4['values'] = ('white','blue','green','orange','red','yellow')
r4.grid(column = 10, row = 3)

r5=tk.Label(window,text='red')
r5.grid(column = 11, row = 3)

r6 = ttk.Combobox(window, width = 4)
r6['values'] = ('white','blue','green','orange','red','yellow')
r6.grid(column = 12, row = 3)

r7 = ttk.Combobox(window, width = 4)
r7['values'] = ('white','blue','green','orange','red','yellow')
r7.grid(column = 10, row = 4)

r8 = ttk.Combobox(window, width = 4)
r8['values'] = ('white','blue','green','orange','red','yellow')
r8.grid(column = 11, row = 4)

r9 = ttk.Combobox(window, width = 4)
r9['values'] = ('white','blue','green','orange','red','yellow')
r9.grid(column = 12, row = 4)





y1 = ttk.Combobox(window, width = 4)
y1['values'] = ('white','blue','green','orange','red','yellow')
y1.grid(column = 2, row = 6)

y2 = ttk.Combobox(window, width = 4)
y2['values'] = ('white','blue','green','orange','red','yellow')
y2.grid(column = 3, row = 6)

y3 = ttk.Combobox(window, width = 4)
y3['values'] = ('white','blue','green','orange','red','yellow')
y3.grid(column = 4, row = 6)

y4 = ttk.Combobox(window, width = 4)
y4['values'] = ('white','blue','green','orange','red','yellow')
y4.grid(column = 2, row = 7)

y5 = tk.Label(window,text='yellow')
y5.grid(column = 3, row = 7)

y6 = ttk.Combobox(window, width = 4)
y6['values'] = ('white','blue','green','orange','red','yellow')
y6.grid(column = 4, row = 7)

y7 = ttk.Combobox(window, width = 4)
y7['values'] = ('white','blue','green','orange','red','yellow')
y7.grid(column = 2, row = 8)

y8 = ttk.Combobox(window, width = 4)
y8['values'] = ('white','blue','green','orange','red','yellow')
y8.grid(column = 3, row = 8)

y9 = ttk.Combobox(window, width = 4)
y9['values'] = ('white','blue','green','orange','red','yellow')
y9.grid(column = 4, row = 8)




b1 = ttk.Combobox(window, width = 4)
b1['values'] = ('white','blue','green','orange','red','yellow')
b1.grid(column = 6, row = 6)

b2 = ttk.Combobox(window, width = 4)
b2['values'] = ('white','blue','green','orange','red','yellow')
b2.grid(column = 7, row = 6)

b3 = ttk.Combobox(window, width = 4)
b3['values'] = ('white','blue','green','orange','red','yellow')
b3.grid(column = 8, row = 6)

b4 = ttk.Combobox(window, width = 4)
b4['values'] = ('white','blue','green','orange','red','yellow')
b4.grid(column = 6, row = 7)

b5 = tk.Label(window,text='blue')
b5.grid(column = 7, row = 7)

b6 = ttk.Combobox(window, width = 4)
b6['values'] = ('white','blue','green','orange','red','yellow')
b6.grid(column = 8, row = 7)

b7 = ttk.Combobox(window, width = 4)
b7['values'] = ('white','blue','green','orange','red','yellow')
b7.grid(column = 6, row = 8)

b8 = ttk.Combobox(window, width = 4)
b8['values'] = ('white','blue','green','orange','red','yellow')
b8.grid(column = 7, row = 8)

b9 = ttk.Combobox(window, width = 4)
b9['values'] = ('white','blue','green','orange','red','yellow')
b9.grid(column = 8, row = 8)





w1 = ttk.Combobox(window, width = 4)
w1['values'] = ('white','blue','green','orange','red','yellow')
w1.grid(column = 10, row = 6)

w2 = ttk.Combobox(window, width = 4)
w2['values'] = ('white','blue','green','orange','red','yellow')
w2.grid(column = 11, row = 6)

w3 = ttk.Combobox(window, width = 4)
w3['values'] = ('white','blue','green','orange','red','yellow')
w3.grid(column = 12, row = 6)

w4 = ttk.Combobox(window, width = 4)
w4['values'] = ('white','blue','green','orange','red','yellow')
w4.grid(column = 10, row = 7)

w5 = tk.Label(window,text='white')
w5.grid(column = 11, row = 7)

w6 = ttk.Combobox(window, width = 4)
w6['values'] = ('white','blue','green','orange','red','yellow')
w6.grid(column = 12, row = 7)

w7 = ttk.Combobox(window, width = 4)
w7['values'] = ('white','blue','green','orange','red','yellow')
w7.grid(column = 10, row = 8)

w8 = ttk.Combobox(window, width = 4)
w8['values'] = ('white','blue','green','orange','red','yellow')
w8.grid(column = 11, row = 8)

w9 = ttk.Combobox(window, width = 4)
w9['values'] = ('white','blue','green','orange','red','yellow')
w9.grid(column = 12, row = 8)






g1 = ttk.Combobox(window, width = 4)
g1['values'] = ('white','blue','green','orange','red','yellow')
g1.grid(column = 14, row = 6)

g2 = ttk.Combobox(window, width = 4)
g2['values'] = ('white','blue','green','orange','red','yellow')
g2.grid(column = 15, row = 6)

g3 = ttk.Combobox(window, width = 4)
g3['values'] = ('white','blue','green','orange','red','yellow')
g3.grid(column = 16, row = 6)

g4 = ttk.Combobox(window, width = 4)
g4['values'] = ('white','blue','green','orange','red','yellow')
g4.grid(column = 14, row = 7)

g5 = tk.Label(window,text='green')
g5.grid(column = 15, row = 7)

g6 = ttk.Combobox(window, width = 4)
g6['values'] = ('white','blue','green','orange','red','yellow')
g6.grid(column = 16, row = 7)

g7 = ttk.Combobox(window, width = 4)
g7['values'] = ('white','blue','green','orange','red','yellow')
g7.grid(column = 14, row = 8)

g8 = ttk.Combobox(window, width = 4)
g8['values'] = ('white','blue','green','orange','red','yellow')
g8.grid(column = 15, row = 8)

g9 = ttk.Combobox(window, width = 4)
g9['values'] = ('white','blue','green','orange','red','yellow')
g9.grid(column = 16, row = 8)





o1 = ttk.Combobox(window, width = 4)
o1['values'] = ('white','blue','green','orange','red','yellow')
o1.grid(column = 10, row = 10)

o2 = ttk.Combobox(window, width = 4)
o2['values'] = ('white','blue','green','orange','red','yellow')
o2.grid(column = 11, row = 10)

o3 = ttk.Combobox(window, width = 4)
o3['values'] = ('white','blue','green','orange','red','yellow')
o3.grid(column = 12, row = 10)

o4 = ttk.Combobox(window, width = 4)
o4['values'] = ('white','blue','green','orange','red','yellow')
o4.grid(column = 10, row = 11)

o5 = tk.Label(window,text='orange')
o5.grid(column = 11, row = 11)

o6 = ttk.Combobox(window, width = 4)
o6['values'] = ('white','blue','green','orange','red','yellow')
o6.grid(column = 12, row = 11)

o7 = ttk.Combobox(window, width = 4)
o7['values'] = ('white','blue','green','orange','red','yellow')
o7.grid(column = 10, row = 12)

o8 = ttk.Combobox(window, width = 4)
o8['values'] = ('white','blue','green','orange','red','yellow')
o8.grid(column = 11, row = 12)

o9 = ttk.Combobox(window, width = 4)
o9['values'] = ('white','blue','green','orange','red','yellow')
o9.grid(column = 12, row = 12)


l1=tk.Label(window,text=' ')
l1.grid(column = 1, row =  6)

l2=tk.Label(window,text=' ')
l2.grid(column = 1, row =  7)

l3=tk.Label(window,text=' ')
l3.grid(column = 1, row =  8)

l1=tk.Label(window,text=' ')
l1.grid(column = 5, row =  6)

l2=tk.Label(window,text=' ')
l2.grid(column = 5, row =  7)

l3=tk.Label(window,text=' ')
l3.grid(column = 5, row =  8)

l1=tk.Label(window,text=' ')
l1.grid(column = 9, row =  6)

l2=tk.Label(window,text=' ')
l2.grid(column = 9, row =  7)

l3=tk.Label(window,text=' ')
l3.grid(column = 9, row =  8)

l1=tk.Label(window,text=' ')
l1.grid(column = 13, row =  6)

l2=tk.Label(window,text=' ')
l2.grid(column = 13, row =  7)

l3=tk.Label(window,text=' ')
l3.grid(column = 13, row =  8)



l1=tk.Label(window,text=' ')
l1.grid(column = 10, row =  1)

l2=tk.Label(window,text=' ')
l2.grid(column = 11, row =  1)

l3=tk.Label(window,text=' ')
l3.grid(column = 11, row =  1)

l1=tk.Label(window,text=' ')
l1.grid(column = 10, row =  5)

l2=tk.Label(window,text=' ')
l2.grid(column = 11, row =  5)

l3=tk.Label(window,text=' ')
l3.grid(column = 11, row =  5)

l1=tk.Label(window,text=' ')
l1.grid(column = 10, row =  9)

l2=tk.Label(window,text=' ')
l2.grid(column = 11, row =  9)

l3=tk.Label(window,text=' ')
l3.grid(column = 11, row =  9)

for i in range(1,14):
    l=tk.Label(window,text=' ')
    l.grid(column=17,row=i)


def display():
    try:
        with open("rc_run.cmd",'w') as w:
            # w.write('pythonw rc_algorithm.py w w w w w w w w w b b b b b b b b b y y y y y y y y y g g g g g g g g g o o o o o o o o o r r r r r r r r r')
            w.write('pythonw rc_algorithm.py y g g g w b w w o o b g w b b r b w r o r o y y g r y w y y g g r o o y o w b y o w w o r b y b r r r g g b')
            # w.write(f'python rc_algorithm.py {w3.get()[0]} {w6.get()[0]} {w9.get()[0]} \
            #     {w2.get()[0]} w {w8.get()[0]} {w1.get()[0]} {w4.get()[0]} {w7.get()[0]} \
            #     {b3.get()[0]} {b6.get()[0]} {b9.get()[0]} {b2.get()[0]} b {b8.get()[0]} \
            #     {b1.get()[0]} {b4.get()[0]} {b7.get()[0]} {y7.get()[0]} {y4.get()[0]} \
            #     {y1.get()[0]} {y8.get()[0]} y {y2.get()[0]} {y9.get()[0]} {y6.get()[0]} \
            #     {y3.get()[0]} {g3.get()[0]} {g6.get()[0]} {g9.get()[0]} {g2.get()[0]} \
            #     g {g8.get()[0]} {g1.get()[0]} {g4.get()[0]} {g7.get()[0]} {o3.get()[0]} \
            #     {o6.get()[0]} {o9.get()[0]} {o2.get()[0]} o {o8.get()[0]} {o1.get()[0]} \
            #     {o4.get()[0]} {o7.get()[0]} {r3.get()[0]} {r6.get()[0]} {r9.get()[0]} \
            #     {r2.get()[0]} r {r8.get()[0]} {r1.get()[0]} {r4.get()[0]} {r7.get()[0]}')
        subprocess.call("rc_run.cmd")
        subprocess.call(['rm','rc_run.cmd'])
    except IndexError:
        subprocess.call(['rm','rc_run.cmd'])
        messagebox.showerror(title='Invalid Input!!!!',message='You Have not selected some combobox. Try again!!!!')
        

def reset():
    w1.set('')
    w2.set('')
    w3.set('')
    w4.set('')
    w6.set('')
    w7.set('')
    w8.set('')
    w9.set('')

    b1.set('')
    b2.set('')
    b3.set('')
    b4.set('')
    b6.set('')
    b7.set('')
    b8.set('')
    b9.set('')
    
    y1.set('')
    y2.set('')
    y3.set('')
    y4.set('')
    y6.set('')
    y7.set('')
    y8.set('')
    y9.set('')
    
    g1.set('')
    g2.set('')
    g3.set('')
    g4.set('')
    g6.set('')
    g7.set('')
    g8.set('')
    g9.set('')
    
    o1.set('')
    o2.set('')
    o3.set('')
    o4.set('')
    o6.set('')
    o7.set('')
    o8.set('')
    o9.set('')
    
    r1.set('')
    r2.set('')
    r3.set('')
    r4.set('')
    r6.set('')
    r7.set('')
    r8.set('')
    r9.set('')

start = tk.Button(window, text ="Start Solving", command = display)
start.grid(column = 4, columnspan=3, row = 3)

reset = tk.Button(window, text ="Reset",command=reset)
reset.grid(column = 4, columnspan=3, row = 11)

window.mainloop()