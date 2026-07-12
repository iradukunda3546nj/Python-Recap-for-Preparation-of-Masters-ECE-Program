import tkinter as tk
import math

# ==========================================================
# Create Main Window
# ==========================================================

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("500x600")
root.resizable(False, False)

# ==========================================================
# Display (Entry Widget)
# ==========================================================

display = tk.Entry(
    root,
    font=("Arial", 22),
    bd=10,
    relief="ridge",
    justify="right"
)

display.grid(row=0, column=0, columnspan=5,
             padx=10, pady=10,
             ipadx=10, ipady=15)

# ==========================================================
# Functions
# ==========================================================

def press(value):
    """Insert text into display"""
    display.insert(tk.END, value)


def clear():
    """Clear display"""
    display.delete(0, tk.END)


def backspace():
    """Delete last character"""
    text = display.get()
    display.delete(0, tk.END)
    display.insert(0, text[:-1])


def calculate():
    """Evaluate expression"""
    try:
        expression = display.get()

        # Replace symbols
        expression = expression.replace("^", "**")
        expression = expression.replace("√", "math.sqrt")
        expression = expression.replace("sin", "math.sin")
        expression = expression.replace("cos", "math.cos")
        expression = expression.replace("tan", "math.tan")
        expression = expression.replace("log", "math.log10")
        expression = expression.replace("ln", "math.log")
        expression = expression.replace("π", str(math.pi))
        expression = expression.replace("e", str(math.e))

        answer = eval(expression)

        display.delete(0, tk.END)
        display.insert(0, answer)

    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# ==========================================================
# Buttons
# ==========================================================

buttons = [

    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3), ("C",1,4),

    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3), ("⌫",2,4),

    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3), ("+",3,4),

    ("0",4,0), (".",4,1), ("(",4,2), (")",4,3), ("=",4,4),

    ("sin(",5,0), ("cos(",5,1), ("tan(",5,2), ("√(",5,3), ("^",5,4),

    ("log(",6,0), ("ln(",6,1), ("π",6,2), ("e",6,3)
]

# ==========================================================
# Create Buttons
# ==========================================================

for (text,row,column) in buttons:

    if text == "=":
        button = tk.Button(
            root,
            text=text,
            width=8,
            height=2,
            font=("Arial",13),
            command=calculate
        )

    elif text == "C":
        button = tk.Button(
            root,
            text=text,
            width=8,
            height=2,
            font=("Arial",13),
            command=clear
        )

    elif text == "⌫":
        button = tk.Button(
            root,
            text=text,
            width=8,
            height=2,
            font=("Arial",13),
            command=backspace
        )

    else:
        button = tk.Button(
            root,
            text=text,
            width=8,
            height=2,
            font=("Arial",13),
            command=lambda value=text: press(value)
        )

    button.grid(row=row,
                column=column,
                padx=5,
                pady=5)

# ==========================================================
# Start Application
# ==========================================================

root.mainloop()