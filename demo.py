import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("计算器")

        self.display_var = tk.StringVar()
        self.display_var.set("")
        self.display = tk.Entry(master, textvariable=self.display_var, justify="right", font=("Arial", 16))
        self.display.grid(row=0, column=0, columnspan=4)

        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)
        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)
        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("C", 4, 2)
        self.create_button("+", 4, 3)
        self.create_button("=", 5, 0, 1, 4)

    def create_button(self, text, row, col, rowspan=1, columnspan=1):
        button = tk.Button(self.master, text=text, font=("Arial", 16), command=lambda: self.button_click(text))
        button.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan, sticky="nsew")

    def button_click(self, text):
        if text == "C":
            self.display_var.set("")
        elif text == "=":
            try:
                result = eval(self.display_var.get())
                self.display_var.set(result)
            except:
                self.display_var.set("Error")
        else:
            self.display_var.set(self.display_var.get() + text)


# root = tk.Tk()
# my_calculator = Calculator(root)
# root.mainloop()
t = '''
1+2
'''
eval(t)
