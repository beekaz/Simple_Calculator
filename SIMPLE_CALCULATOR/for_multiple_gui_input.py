from tkinter import *
from calculator_ui_design import *

# Function to create the GUI components
def create_gui(frame, calculate_numbers):
    # Create and position input fields, buttons, and labels
    
    label_nums = Tk.Label(frame, text="Numbers (separated by commas):")
    label_nums.pack()
    
    entry_nums = Tk.Entry(frame)
    entry_nums.pack()
    
    label_operation =Tk.Label(frame, text="Select Operation:")
    label_operation.pack()
    
    choice = Tk.IntVar()
    
    # Create radio buttons for selecting the operation
    radio_add = Tk.Radiobutton(frame, text="Addition", variable=choice, value=1)
    radio_add.pack()
    
    radio_subtract =Tk.Radiobutton(frame, text="Subtraction", variable=choice, value=2)
    radio_subtract.pack()
    
    radio_multiply = Tk.Radiobutton(frame, text="Multiplication", variable=choice, value=3)
    radio_multiply.pack()
    
    radio_divide = Tk.Radiobutton(frame, text="Division", variable=choice, value=4)
    radio_divide.pack()
    
    button_calculate = Tk.Button(frame, text="Calculate", command=calculate_numbers)
    button_calculate.pack()
    
    label_result = Tk.Label(frame, text="Result: ")
    label_result.pack()
    
    # Pass necessary components to the calculate_numbers function
 #   calculate_numbers._globals_.update(locals())