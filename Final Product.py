import tkinter as tk
import math
import random


LARGE_FONT= ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.grid()

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix, PageSeven, PageEight, PageNine, PageTen, PageEleven):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Welcome to Mr. Cotton's mental math strengthening program", font=LARGE_FONT)
        label.grid(pady=10,padx=10)

        button = tk.Button(self, text="Addition",
                            command=lambda: controller.show_frame(PageOne))
        button.grid()

        button2 = tk.Button(self, text="Subtraction",
                            command=lambda: controller.show_frame(PageTwo))
        button2.grid()

        button3 = tk.Button(self, text="Multiplication",
                            command=lambda: controller.show_frame(PageThree))
        button3.grid()

        button4 = tk.Button(self, text="Division",
                            command=lambda: controller.show_frame(PageFour))
        button4.grid()

        button5 = tk.Button(self, text="Exponents",
                            command=lambda: controller.show_frame(PageFive))
        button5.grid()

        button6 = tk.Button(self, text="Square Root",
                            command=lambda: controller.show_frame(PageSix))
        button6.grid()

        button7 = tk.Button(self, text="Quadratic Solver",
                            command=lambda: controller.show_frame(PageSeven))
        button7.grid()

        button8 = tk.Button(self, text="Sine Law",
                            command=lambda: controller.show_frame(PageEight))
        button8.grid()

        button9 = tk.Button(self, text="Randomly Generated Quadratics",
                            command=lambda: controller.show_frame(PageNine))
        button9.grid()

        button10 = tk.Button(self, text="Regression Calculator",
                             comman=lambda: controller.show_frame(PageTen))
        button10.grid()

        button11 = tk.Button(self, text="Probability Calculator",
                              comman=lambda: controller.show_frame(PageEleven))

        button11.grid()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Addition", font=LARGE_FONT)
        label.grid(row=0, column=2)
        label1 = tk.Label(self, text="Input 1").grid(row=1, column=1)
        Label2 = tk.Label(self, text="Input 2").grid(row=2, column=1)
        sumtext = "Sum: "
        Label3 = tk.Label(self, text=sumtext).grid(row=3, column = 1)
        v1 = tk.StringVar()
        v1.set('0')
        v2 = tk.StringVar()
        v2.set('0')
        e1 = tk.Entry(self, width=10, textvariable=v1).grid(row=1, column=2)
        e2 = tk.Entry(self, width=10, textvariable=v2).grid(row=2, column=2)
        def comp_s():
            self.sum = int(v1.get()) + int(v2.get())
            try:
                self.Label4.destroy()
                self.Label4 = tk.Label(self, text=str(self.sum))
                self.Label4.grid(row=3, column=2)
            except:
                self.Label4 = tk.Label(self, text=str(self.sum))
                self.Label4.grid(row=3, column=2)
        button0 = tk.Button(self, text="Calculate Sum", command=comp_s).grid(row=3, column=3)
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=4, column=2)
    


class PageTwo(tk.Frame):

     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Subtraction", font=LARGE_FONT)
        label.grid(row=0, column=2)
        label1 = tk.Label(self, text="Input 1").grid(row=1, column=1)
        Label2 = tk.Label(self, text="Input 2").grid(row=2, column=1)
        sumtext = "Difference: "
        Label3 = tk.Label(self, text=sumtext).grid(row=3, column = 1)
        v1 = tk.StringVar()
        v1.set('0')
        v2 = tk.StringVar()
        v2.set('0')
        e1 = tk.Entry(self, width=10, textvariable=v1).grid(row=1, column=2)
        e2 = tk.Entry(self, width=10, textvariable=v2).grid(row=2, column=2)
        def comp_s():
            self.sum = int(v1.get()) - int(v2.get())
            try:
                self.Label4.destroy()
                self.Label4 = tk.Label(self, text=str(self.sum))
                self.Label4.grid(row=3, column=2)
            except:
                self.Label4 = tk.Label(self, text=str(self.sum))
                self.Label4.grid(row=3, column=2)
        button0 = tk.Button(self, text="Calculate Difference", command=comp_s).grid(row=3, column=3)
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=4, column=2)



class PageThree(tk.Frame):

     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Multiplication", font=LARGE_FONT)
        label.grid(row=0, column=2)
        label1 = tk.Label(self, text="Input 1").grid(row=1, column=1)
        Label2 = tk.Label(self, text="Input 2").grid(row=2, column=1)
        sumtext = "Product: "
        Label3 = tk.Label(self, text=sumtext).grid(row=3, column = 1)
        v1 = tk.StringVar()
        v1.set('0')
        v2 = tk.StringVar()
        v2.set('0')
        e1 = tk.Entry(self, width=10, textvariable=v1).grid(row=1, column=2)
        e2 = tk.Entry(self, width=10, textvariable=v2).grid(row=2, column=2)
        def comp_s():
            self.sum = int(v1.get()) * int(v2.get())
            try:
                self.Label4.destroy()
                self.Label4 = tk.Label(self, text=str(self.sum))
                self.Label4.grid(row=3, column=2)
            except:
                self.Label4 = tk.Label(self, text=str(self.sum))
                self.Label4.grid(row=3, column=2)
        button0 = tk.Button(self, text="Calculate Product", command=comp_s).grid(row=3, column=3)
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=4, column=2)



class PageFour(tk.Frame):

     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Division", font=LARGE_FONT)
        label.grid(row=0, column=2)
        label1 = tk.Label(self, text="Input 1").grid(row=1, column=1)
        Label2 = tk.Label(self, text="Input 2").grid(row=2, column=1)
        sumtext = "Quotient: "
        Label3 = tk.Label(self, text=sumtext).grid(row=3, column = 1)
        v1 = tk.StringVar()
        v1.set('0')
        v2 = tk.StringVar()
        v2.set('0')
        e1 = tk.Entry(self, width=10, textvariable=v1).grid(row=1, column=2)
        e2 = tk.Entry(self, width=10, textvariable=v2).grid(row=2, column=2)
        def comp_s():
            self.sum = int(v1.get()) / int(v2.get())
            try:
                self.Label4.destroy()
                self.Label4 = tk.Label(self, text=str(self.sum))
                self.Label4.grid(row=3, column=2)
            except:
                self.Label4 = tk.Label(self, text=str(self.sum))
                self.Label4.grid(row=3, column=2)
        button0 = tk.Button(self, text="Calculate Quotient", command=comp_s).grid(row=3, column=3)
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=4, column=2)



class PageFive(tk.Frame):

     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Exponents", font=LARGE_FONT)
        label.grid(row=0, column=2)
        label1 = tk.Label(self, text="Base").grid(row=1, column=1)
        Label2 = tk.Label(self, text="Power").grid(row=2, column=1)
        sumtext = "Answer: "
        Label3 = tk.Label(self, text=sumtext).grid(row=3, column = 1)
        v1 = tk.StringVar()
        v1.set('0')
        v2 = tk.StringVar()
        v2.set('0')
        e1 = tk.Entry(self, width=10, textvariable=v1).grid(row=1, column=2)
        e2 = tk.Entry(self, width=10, textvariable=v2).grid(row=2, column=2)
        def comp_s():
            self.sum = int(v1.get()) ** int(v2.get())
            try:
                self.Label4.destroy()
                self.Label4 = tk.Label(self, text=str(self.sum))
                self.Label4.grid(row=3, column=2)
            except:
                self.Label4 = tk.Label(self, text=str(self.sum))
                self.Label4.grid(row=3, column=2)
        button0 = tk.Button(self, text="Calculate Answer", command=comp_s).grid(row=3, column=3)
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=4, column=2)



class PageSix(tk.Frame):

     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Square Root", font=LARGE_FONT)
        label.grid(row=0, column=2)
        label1 = tk.Label(self, text="Number").grid(row=1, column=1)
        sumtext = "Square Root: "
        Label3 = tk.Label(self, text=sumtext).grid(row=3, column = 1)
        v1 = tk.StringVar()
        v1.set('0')
        e1 = tk.Entry(self, width=10, textvariable=v1).grid(row=1, column=2)
        def comp_s():
            self.sum = math.sqrt(int(v1.get()))
            try:
                self.Label4.destroy()
                self.Label4 = tk.Label(self, text=str(self.sum))
                self.Label4.grid(row=3, column=2)
            except:
                self.Label4 = tk.Label(self, text=str(self.sum))
                self.Label4.grid(row=3, column=2)
        button0 = tk.Button(self, text="Calculate Answer", command=comp_s).grid(row=3, column=3)
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=4, column=2)




class PageSeven(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Quadratic Solver", font=LARGE_FONT)
        label.grid(row=0, column=2)
        def  quadadd(a, b, c):
            return((-1)* b + math.sqrt(b**2-4*a*c))/2*a
        def quadsubtract(a, b, c):
            return((-1)* b - math.sqrt(b**2-4*a*c))/2*a
        label1 = tk.Label(self, text="a").grid(row=1, column=1)
        Label2 = tk.Label(self, text="b").grid(row=2, column=1)
        Label3 = tk.Label(self, text="c").grid(row=3, column=1)
        Label4 = tk.Label(self, text="x: ").grid(row=4, column=1)
        Label5 = tk.Label(self, text="x: ").grid(row=5, column=1)
        v1 = tk.StringVar()
        v1.set('0')
        v2 = tk.StringVar()
        v2.set('0')
        v3 = tk.StringVar()
        v3.set('0')
        a = tk.Entry(self, width=10, textvariable=v1).grid(row=1, column=2)
        b = tk.Entry(self, width=10, textvariable=v2).grid(row=2, column=2)
        c = tk.Entry(self, width=10, textvariable=v3).grid(row=3, column=2)
        def comp_s():
            self.quadadd = quadadd(int(v1.get()), int(v2.get()), int(v3.get()))
            self.quadsubtract = quadsubtract(int(v1.get()), int(v2.get()), int(v3.get()))
            try:
                self.Label4.destroy()
                self.Label4 = tk.Label(self, text=str(self.quadadd))
                self.Label4.grid(row=4, column=2)
                self.Label5.destroy()
                self.Label5 = tk.Label(self, text=str(self.quadsubtract))
                self.Label5.grid(row=5, column=2)
            except:
                self.Label4 = tk.Label(self, text=str(self.quadadd))
                self.Label4.grid(row=4, column=2)
                self.Label5 = tk.Label(self, text=str(self.quadsubtract))
                self.Label5.grid(row=5, column=2)
        button0 = tk.Button(self, text="Find X values: ", command=comp_s).grid(row=4, column=3)
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=7, column=2)




class PageEight(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Sine Law Solver", font=LARGE_FONT)
        label.grid(row=0, column=2)
        def  sinelawangle(A, a, b):
            return math.degrees(math.asin((b * math.sin(math.radians(A))) / a))
        def sinelawside(A, a, b):
            return a * math.sin(math.radians(b)) / math.sin(math.radians(A))
        label1 = tk.Label(self, text="A").grid(row=1, column=1)
        Label2 = tk.Label(self, text="a").grid(row=2, column=1)
        Label3 = tk.Label(self, text="B/b").grid(row=3, column=1)
        Label4 = tk.Label(self, text="Angle: ").grid(row=4, column=1)
        Label5 = tk.Label(self, text="Side: ").grid(row=5, column=1)
        v1 = tk.StringVar()
        v1.set('0')
        v2 = tk.StringVar()
        v2.set('0')
        v3 = tk.StringVar()
        v3.set('0')
        A = tk.Entry(self, width=10, textvariable=v1).grid(row=1, column=2)
        a = tk.Entry(self, width=10, textvariable=v2).grid(row=2, column=2)
        x = tk.Entry(self, width=10, textvariable=v3).grid(row=3, column=2)
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=7, column=2)
        def comp_s():
            self.sinelawangle = sinelawangle(float(v1.get()), float(v2.get()), float(v3.get()))
            self.sinelawside = sinelawside(float(v1.get()), float(v2.get()), float(v3.get()))
            try:
                self.Label4.destroy()
                self.Label4 = tk.Label(self, text=str(self.sinelawangle))
                self.Label4.grid(row=4, column=2)
                self.Label5.destroy()
                self.Label5 = tk.Label(self, text=str(self.sinelawside))
                self.Label5.grid(row=5, column=2)
            except:
                self.Label4 = tk.Label(self, text=str(self.sinelawangle))
                self.Label4.grid(row=4, column=2)
                self.Label5 = tk.Label(self, text=str(self.sinelawside))

class PageNine(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Random Quadratic", font=LARGE_FONT)
        label.grid(row=0, column=2)
        def resetquadratic():
            Label0 = tk.Label(self, text="Plug numbers into the formula ax^2 + bx + c").grid(row=1, column=2)
            label1 = tk.Label(self, text="a").grid(row=2, column=1)
            Label2 = tk.Label(self, text="b").grid(row=2, column=2)
            Label3 = tk.Label(self, text="c").grid(row=2, column=3)
            a = tk.Label(self, text=random.randint(0, 100)).grid(row=3, column=1)
            b = tk.Label(self, text=random.randint(0, 100)).grid(row=3, column=2)
            c = tk.Label(self, text=random.randint(0, 100)).grid(row=3, column=3)
        resetquadratic()
        button2 = tk.Button(self, text="Generate another Quadratic", command=resetquadratic)
        button2.grid(row=4, column=2)
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=5, column=2)
        self.Label5.grid(row=5, column=2)
        button0 = tk.Button(self, text="Find Angle / Side: ", command=comp_s).grid(row=4, column=3)
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=7, column=2)




class PageNine(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Random Quadratic", font=LARGE_FONT)
        label.grid(row=0, column=2)
        def resetquadratic():
            Label0 = tk.Label(self, text="Plug numbers into the formula ax^2 + bx + c").grid(row=1, column=2)
            label1 = tk.Label(self, text="a").grid(row=2, column=1)
            Label2 = tk.Label(self, text="b").grid(row=2, column=2)
            Label3 = tk.Label(self, text="c").grid(row=2, column=3)
            a = tk.Label(self, text=random.randint(0, 100)).grid(row=3, column=1)
            b = tk.Label(self, text=random.randint(0, 100)).grid(row=3, column=2)
            c = tk.Label(self, text=random.randint(0, 100)).grid(row=3, column=3)
        resetquadratic()
        button2 = tk.Button(self, text="Generate another Quadratic", command=resetquadratic)
        button2.grid(row=4, column=2)
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=5, column=2)



class PageTen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Regression Calculator", font=LARGE_FONT)
        label.grid(row=0, column=2)
        Label0 = tk.Label(self, text="Insert X and Y values in their columns:").grid(row=1, column=2)
        label1 = tk.Label(self, text="X").grid(row=2, column=1)
        Label2 = tk.Label(self, text="Y").grid(row=2, column=2)
        Label3 = tk.Label(self, text="Answers").grid(row=2, column=3)
        Label1 = tk.Label(self, text="TempValue1").grid(row=3, column=3)                          
        Label2 = tk.Label(self, text="TempValue2").grid(row=4, column=3)
        Label3 = tk.Label(self, text="TempValue3").grid(row=5, column=3)
        v1 = tk.StringVar()
        v1.set('0')
        v2 = tk.StringVar()
        v2.set('0')
        v3 = tk.StringVar()
        v3.set('0')
        v4 = tk.StringVar()
        v4.set('0')
        v5 = tk.StringVar()
        v5.set('0')
        v6 = tk.StringVar()
        v6.set('0')
        x = tk.Entry(self, width=10, textvariable=v1).grid(row=3, column=1)
        xx = tk.Entry(self, width=10, textvariable=v2).grid(row=4, column=1)
        xxx = tk.Entry(self, width=10, textvariable=v3).grid(row=5, column=1)
        y = tk.Entry(self, width=10, textvariable=v4).grid(row=3, column=2)
        yy = tk.Entry(self, width=10, textvariable=v5).grid(row=4, column=2)
        yyy = tk.Entry(self, width=10, textvariable=v6).grid(row=5, column=2)
        
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=7, column=2)

class PageEleven(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Regression Calculator", font=LARGE_FONT)
        label.grid(row=0, column=2)
        Label0 = tk.Label(self, text="Insert X and Y values in their columns:").grid(row=1, column=2)
        label1 = tk.Label(self, text="X").grid(row=2, column=1)
        Label2 = tk.Label(self, text="Y").grid(row=2, column=2)
        Label3 = tk.Label(self, text="Answers").grid(row=2, column=3)
        Label1 = tk.Label(self, text="TempValue1").grid(row=3, column=3)                          
        Label2 = tk.Label(self, text="TempValue2").grid(row=4, column=3)
        Label3 = tk.Label(self, text="TempValue3").grid(row=5, column=3)
        v1 = tk.StringVar()
        v1.set('0')
        v2 = tk.StringVar()
        v2.set('0')
        v3 = tk.StringVar()
        v3.set('0')
        v4 = tk.StringVar()
        v4.set('0')
        v5 = tk.StringVar()
        v5.set('0')
        v6 = tk.StringVar()
        v6.set('0')
        x = tk.Entry(self, width=10, textvariable=v1).grid(row=3, column=1)
        xx = tk.Entry(self, width=10, textvariable=v2).grid(row=4, column=1)
        xxx = tk.Entry(self, width=10, textvariable=v3).grid(row=5, column=1)
        y = tk.Entry(self, width=10, textvariable=v4).grid(row=3, column=2)
        yy = tk.Entry(self, width=10, textvariable=v5).grid(row=4, column=2)
        yyy = tk.Entry(self, width=10, textvariable=v6).grid(row=5, column=2)
        
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=7, column=2)

       
        
app = SeaofBTCapp()
app.mainloop()
