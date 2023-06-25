from tkinter import *
expression = ""
#from arithemetic_functions import add, subtract, multiply, divide
root= Tk()
frame = Frame(root)
frame.pack()

root.title('Beekaz simple calculator')
root.configure(background = 'black')
root.geometry('500x600')
middle=Frame()
equation=StringVar()
equation.set("")


def Standard():
    root.resizable(width=False, height=False)
    root.geometry("480x568+0+0")
 
menubar = Menu(frame)
 
# ManuBar 1 :
filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = filemenu)
filemenu.add_command(label = "Standard", command = Standard)
#filemenu.add_command(label = "Scientific", command = Scientific)

def press(num):
        global expression
        expression = expression_field.get()
        expression += str(num)
        equation.set(expression)
        
        
def equalpress():
                global expression
                try:
                        total = str(eval(expression))
                        equation.set(total)
                        expression =""
                except:
 
                   equation.set(" error ")
                   expression = ""
 
def handle_backspace():
    global expression
    if len(expression) > 0:
        expression = expression[:-1]
        equation.set(expression)
        

      
                               
def clear():
                global expression 
                expression = ""
                equation.set("")
                
                
expression_field = Entry(frame, textvariable=equation)
expression_field.grid(columnspan = 4, ipadx = 100)
button1 = Button(frame , text = '1', fg = 'black', bg = 'pink', command = lambda: press(1), height =1, width=7)
button1.grid(row = 2, column = 0)
button2 = Button(frame, text = '2', fg = 'black', bg = 'white', command = lambda: press(2), height= 1, width=7)
button2.grid(row=2, column=1)
button3 = Button(frame, text= '3', fg='black', bg='pink', command=lambda: press(3), height=1, width=7)
button3.grid(row=2, column=2)
button4 = Button(frame, text=' 4 ', fg='black', bg='pink', command=lambda: press(4), height=1, width=7)
button4.grid(row=3, column=0)
button5 = Button(frame, text=' 5 ', fg='black', bg='white', command=lambda: press(5), height=1, width=7)
button5.grid(row=3, column=1)
button6 = Button(frame, text=' 6 ', fg='black', bg='pink',command=lambda: press(6), height=1, width=7)
button6.grid(row=3, column=2)
button7 = Button(frame, text=' 7 ', fg='black', bg='pink', command=lambda: press(7), height=1, width=7)
button7.grid(row=4, column=0)
button8 = Button(frame, text=' 8 ', fg='black', bg='white', command=lambda: press(8), height=1, width=7)
button8.grid(row=4, column=1)
button9 = Button(frame, text=' 9 ', fg='black', bg='pink', command=lambda: press(9), height=1, width=7)
button9.grid(row=4, column=2)
button0 = Button(frame, text=' 0 ', fg='black', bg='pink', command=lambda: press(0), height=1, width=7)
button0.grid(row=5, column=0)
 
add = Button(frame, text=' + ', fg='black', bg='white', command=lambda: press("+"), height=1, width=7)
add.grid(row=2, column=3)
subtract = Button(frame, text=' - ', fg='black', bg='pink', command=lambda: press("-"), height=1, width=7)
subtract.grid(row=3, column=3)
multiply = Button(frame, text=' * ', fg='black', bg='white', command=lambda: press("*"), height=1, width=7)
multiply.grid(row=4, column=3)
divide = Button(frame, text=' / ', fg='black', bg='pink', command=lambda: press("/"), height=1, width=7)
divide.grid(row=5, column=3)
equal = Button(frame, text=' = ', fg='black', bg='pink', command=equalpress, height=1, width=7)
equal.grid(row=5, column=2)
clear = Button(frame, text='Clear', fg='black', bg='white', command=clear, height=1, width=7)
clear.grid(row=5, column='1')
handle_backspace = Button(frame, text='<--', fg='black', bg='white', command=handle_backspace, height=1, width=7)
handle_backspace.grid(row=6, column='0')
Decimal= Button(frame, text='.', fg='black', bg='pink', command=lambda: press('.'), height=1, width=7)
Decimal.grid(row=6, column=1)



frame.mainloop()
