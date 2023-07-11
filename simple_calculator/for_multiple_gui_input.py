from tkinter import Label, Entry, IntVar, Radiobutton, Button

# Function to create the GUI components
def create_gui(frame, calculate_numbers):
    # Create and position input fields, buttons, and labels
    
    label_nums = Label(frame, text="Numbers (separated by commas):")
    label_nums.pack()
    
    entry_nums = Entry(frame)
    entry_nums.pack()
    
    label_operation = Label(frame, text="Select Operation:")
    label_operation.pack()
    
    choice = IntVar()
    
    # Create radio buttons for selecting the operation
    radio_add = Radiobutton(frame, text="Addition", variable=choice, value=1)
    radio_add.pack()
    
    radio_subtract =Radiobutton(frame, text="Subtraction", variable=choice, value=2)
    radio_subtract.pack()
    
    radio_multiply = Radiobutton(frame, text="Multiplication", variable=choice, value=3)
    radio_multiply.pack()
    
    radio_divide = Radiobutton(frame, text="Division", variable=choice, value=4)
    radio_divide.pack()
    
    button_calculate = Button(frame, text="Calculate", command=calculate_numbers)
    button_calculate.pack()
    
    label_result = Label(frame, text="Result: ")
    label_result.pack()
    
    # Pass necessary components to the calculate_numbers function
 #   calculate_numbers._globals_.update(locals())