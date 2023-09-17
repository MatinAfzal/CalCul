############################################################################
# CalCul Created By Matin Afzal
# https://github.com/MatinAfzal
# contact.matin@yahoo.com
############################################################################

from tkinter import *
from calculations import DoCalCul
from list import List
from functools import partial

# File identity information
__author__ = 'Matin Afzal (contact.matin@yahoo.com)'
__version__ = '0.0.1'
__last_modification__ = '2023/09/17'

# List initialize
list = List(20)

# Calculator initialize
calculations = DoCalCul()

# Define Functions
spin_number = ""
def button_press(button_val):
    global spin_number
    current = output.cget("text")

    # check number in each program loop spin
    if button_val in "0123456789.000":
        spin_number += button_val

    # check every single button
    if button_val == "CE":
        list.clear()
        new = ""

    elif button_val == "C":
        spin_number = ""

    elif button_val == "DEL":
        new = current[:-1]

    elif button_val in ("Sin", "Cos", "Tan", "Cot", "Sec", "^", "Abs", "sqrt", "Ln", "Log", "/", "*", "+", "-"):
        status = list.push(spin_number)
        status1 = list.push(button_val)
        spin_number = ""
        if status != True or status1 != True:
            new = "LIST PUSHING ERROR"
        new = current + button_val

    elif button_val == "=":
        list.push(spin_number)
        spin_number = ""

        result = calculations.docalcul(list.list)
        new = result

    else:
        new = current + button_val

    # Update Output screen
    output.configure(text=new)

# initialize calcul window
calcul = Tk()
calcul.geometry("352x493")
calcul.resizable(width=False, height=False)
calcul.title("CAL CUL")

# initialize segment frame
segment = LabelFrame(calcul, text="OUTPUT")
segment.pack(expand=False, fill=X, pady=27)

output = Button(segment, text="", bg="white", fg="black", font="bold", bd=2, width=38, height=3, anchor="e")
output.grid(row=0, column=0)

# initialize P1 controll frame
controll = Frame(calcul, bg="pink")
controll.pack(fill="both", ipady=0)

controll_2 = Frame(calcul, bg="red")
controll_2.pack(fill="x", side="right", ipady=120, ipadx=0)

load_sin = partial(button_press, "Sin")
op_sin = Button(controll, text="Sin", bg="white", fg="black", bd=4, width=5, height=3, command=load_sin)
op_sin.grid(row=0, column=0)

load_cos = partial(button_press, "Cos")
op_cos = Button(controll, text="Cos", bg="white", fg="black", bd=4, width=5, height=3, command=load_cos)
op_cos.grid(row=0, column=1)

load_tan = partial(button_press, "Tan")
op_tan = Button(controll, text="Tan", bg="white", fg="black", bd=4, width=5, height=3, command=load_tan)
op_tan.grid(row=0, column=2)

load_cot = partial(button_press, "Cot")
op_Cot = Button(controll, text="Cot", bg="white", fg="black", bd=4, width=5, height=3, command=load_cot)
op_Cot.grid(row=0, column=3)

load_sec = partial(button_press, "Sec")
op_sec = Button(controll, text="Sec", bg="white", fg="black", bd=4, width=5, height=3, command=load_sec)
op_sec.grid(row=0, column=4)

load_float = partial(button_press, ".")
op_float = Button(controll, text=".", bg="white", fg="black", bd=4, width=5, height=3, command=load_float)
op_float.grid(row=0, column=5)

load_percent = partial(button_press, "%")
op_percent = Button(controll, text="%", bg="white", fg="black", bd=4, width=7, height=3, command=load_percent)
op_percent.grid(row=0, column=6)

load_xPowery = partial(button_press, "^")
op_xPowery = Button(controll, text="X^Y", bg="white", fg="black", bd=4, width=5, height=3, command=load_xPowery)
op_xPowery.grid(row=1, column=0)

load_divideByOne = partial(button_press, "/1")
op_divide1 = Button(controll, text="1/X", bg="white", fg="black", bd=4, width=5, height=3, command=load_divideByOne)
op_divide1.grid(row=1, column=1)

load_absolute = partial(button_press, "Abs")
op_absoluteValue = Button(controll, text="|X|", bg="white", fg="black", bd=4, width=5, height=3, command=load_absolute)
op_absoluteValue.grid(row=1, column=2)

load_sqrt = partial(button_press, "sqrt")
op_sqrt = Button(controll, text="√", bg="white", fg="black", bd=4, width=5, height=3, command=load_sqrt)
op_sqrt.grid(row=1, column=3)

load_log = partial(button_press, "Log")
op_log = Button(controll, text="Log", bg="white", fg="black", bd=4, width=5, height=3, command=load_log)
op_log.grid(row=1, column=4)

load_ln = partial(button_press, "Ln")
op_ln = Button(controll, text="Ln", bg="white", fg="black", bd=4, width=5, height=3, command=load_ln)
op_ln.grid(row=1, column=5)

load_division = partial(button_press, "/")
op_division = Button(controll, text="÷", bg="white", fg="black", bd=4, width=7, height=3, command=load_division)
op_division.grid(row=1, column=6)

load_multiplication = partial(button_press, "*")
op_multiplication = Button(controll_2, text="×", bg="white", fg="black", bd=4, width=6, height=3, command=load_multiplication)
op_multiplication.grid(row=0, column=0)

load_addition = partial(button_press, "+")
op_addition = Button(controll_2, text="+", bg="white", fg="black", bd=4, width=6, height=3, command=load_addition)
op_addition.grid(row=1, column=0)

load_subtraction = partial(button_press, "-")
op_subtraction = Button(controll_2, text="-", bg="white", fg="black", bd=4, width=6, height=3, command=load_subtraction)
op_subtraction.grid(row=2, column=0)

load_equal = partial(button_press, "=")
op_equal = Button(controll_2, text="=", bg="white", fg="black", bd=4, width=6, height=3, command=load_equal)
op_equal.grid(row=3, column=0)

# initialize numpad frame
numPad = Frame(calcul, bg="green")
numPad.pack(fill="x", side="left", ipady=30, ipadx=145)

load_one = partial(button_press, "1")
num_one = Button(numPad, text="1", bg="white", font="Times 20 italic bold",fg="black", bd=4, width=3, height=1, command=load_one)
num_one.grid(row=0, column=2)

load_two = partial(button_press, "2")
num_two = Button(numPad, text="2", bg="white", fg="black", font="Times 20 italic bold",bd=4, width=3, height=1, command=load_two)
num_two.grid(row=0, column=3)

load_three = partial(button_press, "3")
num_three = Button(numPad, text="3", bg="white", fg="black", font="Times 20 italic bold",bd=4, width=3, height=1, command=load_three)
num_three.grid(row=0, column=4)

load_four = partial(button_press, "4")
num_four = Button(numPad, text="4", bg="white", fg="black", font="Times 20 italic bold",bd=4, width=3, height=1, command=load_four)
num_four.grid(row=1, column=2)

load_five = partial(button_press, "5")
num_five = Button(numPad, text="5", bg="white", fg="black", font="Times 20 italic bold",bd=4, width=3, height=1, command=load_five)
num_five.grid(row=1, column=3)

load_six = partial(button_press, "6")
num_six = Button(numPad, text="6", bg="white", fg="black", font="Times 20 italic bold",bd=4, width=3, height=1, command=load_six)
num_six.grid(row=1, column=4)

load_seven = partial(button_press, "7")
num_seven = Button(numPad, text="7", bg="white", fg="black", font="Times 20 italic bold",bd=4, width=3, height=1, command=load_seven)
num_seven.grid(row=2, column=2)

load_eight = partial(button_press, "8")
num_eight = Button(numPad, text="8", bg="white", fg="black", font="Times 20 italic bold",bd=4, width=3, height=1, command=load_eight)
num_eight.grid(row=2, column=3)

load_nine = partial(button_press, "9")
num_nine = Button(numPad, text="9", bg="white", fg="black", font="Times 20 italic bold",bd=4, width=3, height=1, command=load_nine)
num_nine.grid(row=2, column=4)

load_3z = partial(button_press, "000")
num_3Zero = Button(numPad, text="000", bg="white", fg="black", font="Times 20 italic bold",bd=4, width=6, height=1, command=load_3z)
num_3Zero.grid(row=0, column=5)

load_2z = partial(button_press, "00")
num_2Zero = Button(numPad, text="00", bg="white", fg="black", font="Times 20 italic bold",bd=4, width=6, height=1, command=load_2z)
num_2Zero.grid(row=1, column=5)

load_1z = partial(button_press, "0")
num_1Zero = Button(numPad, text="0", bg="white", fg="black", font="Times 20 italic bold",bd=4, width=6, height=1, command=load_1z)
num_1Zero.grid(row=2, column=5)

## Some controll operators inside numpad frame
load_clear_empty = partial(button_press, "CE")
op_clearEmpty = Button(numPad, text="CE", bg="white", fg="red" ,font="Times 20 italic bold", bd=4, width=3, height=1, command=load_clear_empty)
op_clearEmpty.grid(row=3, column=2)

load_clear = partial(button_press, "C")
op_clear = Button(numPad, text="C", bg="white", fg="black" ,font="Times 20 italic bold", bd=4, width=3, height=1, command=load_clear)
op_clear.grid(row=3, column=3)

op_positiveOrNegative = Button(numPad, text="+/-", bg="white", fg="black" ,font="Times 20 italic bold", bd=4, width=3, height=1)
op_positiveOrNegative.grid(row=3, column=4)

load_delete = partial(button_press, "DEL")
op_delete = Button(numPad, text="←", bg="white", fg="black" ,font="Times 20 italic bold", bd=4, width=6, height=1, command=load_delete)
op_delete.grid(row=3, column=5)

# Program loop
calcul.mainloop()