from tkinter import Tk, Frame, Menu, Button, Entry, StringVar


root = Tk()
root.title("Beekaz simple calculator")
root.configure(background="black")
root.geometry("500x600")

expression = StringVar()
expression.set("")

frame = Frame(root)
frame.pack()
menubar = Menu(frame)


def standard():
    root.resizable(width=False, height=False)
    root.geometry("480x568")


def handle_key_press(key: str):
    old_expression = expression.get()
    new_expression = old_expression + key
    expression.set(new_expression)


def handle_equal_press():
    try:
        expression.set(eval(expression.get()))
    except ZeroDivisionError:
        expression.set("Can't divide by zero")
    except:
        expression.set("Error")


def handle_backspace():
    old_expression = expression.get()
    new_expression = old_expression[:-1]
    expression.set(new_expression)


def handle_clear():
    expression.set("")


# ManuBar 1 :
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Standard", command=standard)
# file_menu.add_command(label = "Scientific", command = Scientific)


expression_field = Entry(frame, textvariable=expression)
expression_field.grid(columnspan=4, ipadx=100)

button1 = Button(
    frame,
    text="1",
    fg="black",
    bg="pink",
    command=lambda: handle_key_press("1"),
    height=1,
    width=7,
)
button1.grid(row=2, column=0)
button2 = Button(
    frame,
    text="2",
    fg="black",
    bg="white",
    command=lambda: handle_key_press("2"),
    height=1,
    width=7,
)
button2.grid(row=2, column=1)
button3 = Button(
    frame,
    text="3",
    fg="black",
    bg="pink",
    command=lambda: handle_key_press("3"),
    height=1,
    width=7,
)
button3.grid(row=2, column=2)
button4 = Button(
    frame,
    text=" 4 ",
    fg="black",
    bg="pink",
    command=lambda: handle_key_press("4"),
    height=1,
    width=7,
)
button4.grid(row=3, column=0)
button5 = Button(
    frame,
    text=" 5 ",
    fg="black",
    bg="white",
    command=lambda: handle_key_press("5"),
    height=1,
    width=7,
)
button5.grid(row=3, column=1)
button6 = Button(
    frame,
    text=" 6 ",
    fg="black",
    bg="pink",
    command=lambda: handle_key_press("6"),
    height=1,
    width=7,
)
button6.grid(row=3, column=2)
button7 = Button(
    frame,
    text=" 7 ",
    fg="black",
    bg="pink",
    command=lambda: handle_key_press("7"),
    height=1,
    width=7,
)
button7.grid(row=4, column=0)
button8 = Button(
    frame,
    text=" 8 ",
    fg="black",
    bg="white",
    command=lambda: handle_key_press("8"),
    height=1,
    width=7,
)
button8.grid(row=4, column=1)
button9 = Button(
    frame,
    text=" 9 ",
    fg="black",
    bg="pink",
    command=lambda: handle_key_press("9"),
    height=1,
    width=7,
)
button9.grid(row=4, column=2)
button0 = Button(
    frame,
    text=" 0 ",
    fg="black",
    bg="pink",
    command=lambda: handle_key_press("0"),
    height=1,
    width=7,
)
button0.grid(row=5, column=0)

add_button = Button(
    frame,
    text=" + ",
    fg="black",
    bg="white",
    command=lambda: handle_key_press("+"),
    height=1,
    width=7,
)
add_button.grid(row=2, column=3)

subtract_button = Button(
    frame,
    text=" - ",
    fg="black",
    bg="pink",
    command=lambda: handle_key_press("-"),
    height=1,
    width=7,
)
subtract_button.grid(row=3, column=3)

multiply_button = Button(
    frame,
    text=" X ",
    fg="black",
    bg="white",
    command=lambda: handle_key_press("*"),
    height=1,
    width=7,
)
multiply_button.grid(row=4, column=3)

divide_button = Button(
    frame,
    text=" / ",
    fg="black",
    bg="pink",
    command=lambda: handle_key_press("/"),
    height=1,
    width=7,
)
divide_button.grid(row=5, column=3)

equal_button = Button(
    frame,
    text=" = ",
    fg="black",
    bg="pink",
    command=handle_equal_press,
    height=1,
    width=7,
)
equal_button.grid(row=5, column=2)

clear_button = Button(
    frame, text="Clear", fg="black", bg="white", command=handle_clear, height=1, width=7
)
clear_button.grid(row=5, column=1)

backspace_button = Button(
    frame,
    text="CC",
    fg="black",
    bg="white",
    command=handle_backspace,
    height=1,
    width=7,
)
backspace_button.grid(row=6, column=0)

decimal_point_button = Button(
    frame,
    text=".",
    fg="black",
    bg="pink",
    command=lambda: handle_key_press("."),
    height=1,
    width=7,
)
decimal_point_button.grid(row=6, column=1)
