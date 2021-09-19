import math
from tkinter import *

class MainPage (Frame):
        def __init__(self):
            Frame.__init__(self)
            self.master.title("Rayan's basic calculator")
            lbl = Label(self, text = "Welcome to Rayan's basic calculator. Select operation...").grid()
            bttn1 = Button(self, text = "1. Addition")
            bttn1.grid()
            bttn2 = Button(self, text = "2. Subtraction")
            bttn2.grid()
            bttn3 = Button(self, text = "3. Multiplication")
            bttn3.grid()
            bttn4 = Button(self, text = "4. Division")
            bttn4.grid()
            bttn5 = Button(self, text = "5. Exponents")
            bttn5.grid()
            bttn6 = Button(self, text = "6. Square Root")
            bttn6.grid()
            bttn7 = Button(self, text = "7. Quadratic Solver")
            bttn7.grid()
            bttn8 = Button(self, text = "8. Sine Law")
            bttn8.grid()
            bttn9 = Button(self, text = "9. Randomly Generated Quadratics")
            bttn9.grid()
            self.grid()
        def show(self):
                self.lift()

def main():
   MainPage().mainloop()
   
if __name__ == "__main__":
   main()

class Addition (Page):
        def __init__(self):
                Frame.__init__(self)
                self.master.title("Addition")
        def create_widget(self):
                addself.inst_lbl = Label(addself, text = "Enter the first number: ")
                addself.inst_lbl.grid(row = 0, column = 0, columnspan = 2, stick = W)
                addself.pw_lbl = Label(addself, text = "#1")
                addself.pw_lbl.grid(row = 1, column = 0, sticky = W)
