import tkinter as tk
from tkinter import font


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Professional Calculator")
        self.root.geometry("380x560")
        self.root.resizable(False, False)
        self.root.configure(bg="#1f1f1f")

        self.expression = ""

        self.display_var = tk.StringVar()

        display_font = font.Font(size=24, weight="bold")

        display = tk.Entry(
            root,
            textvariable=self.display_var,
            font=display_font,
            justify="right",
            bd=0,
            bg="#2d2d2d",
            fg="white",
            insertbackground="white"
        )

        display.pack(fill="both", padx=10, pady=15, ipady=20)

        buttons = [
            ["C", "(", ")", "⌫"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "%", "+"],
            ["="]
        ]

        button_font = font.Font(size=16, weight="bold")

        frame = tk.Frame(root, bg="#1f1f1f")
        frame.pack(expand=True, fill="both")

        for row in buttons:
            row_frame = tk.Frame(frame, bg="#1f1f1f")
            row_frame.pack(expand=True, fill="both")

            for btn in row:
                color = "#3c3f41"
                fg = "white"

                if btn in ["+", "-", "*", "/", "="]:
                    color = "#ff9500"

                if btn == "C":
                    color = "#d32f2f"

                if btn == "⌫":
                    color = "#455a64"

                button = tk.Button(
                    row_frame,
                    text=btn,
                    font=button_font,
                    bg=color,
                    fg=fg,
                    bd=0,
                    activebackground="#666666",
                    activeforeground="white",
                    command=lambda b=btn: self.click(b)
                )

                if btn == "=":
                    button.pack(
                        side="left",
                        expand=True,
                        fill="both",
                        padx=5,
                        pady=5
                    )
                else:
                    button.pack(
                        side="left",
                        expand=True,
                        fill="both",
                        padx=5,
                        pady=5
                    )

        self.root.bind("<Return>", lambda event: self.calculate())
        self.root.bind("<BackSpace>", lambda event: self.backspace())
        self.root.bind("<Delete>", lambda event: self.clear())

        for key in "0123456789+-*/().%":
            self.root.bind(key, self.key_press)

    def key_press(self, event):
        self.expression += event.char
        self.display_var.set(self.expression)

    def click(self, value):
        if value == "=":
            self.calculate()

        elif value == "C":
            self.clear()

        elif value == "⌫":
            self.backspace()

        else:
            self.expression += value
            self.display_var.set(self.expression)

    def calculate(self):
        try:
            expression = self.expression.replace("%", "/100")
            result = str(eval(expression))
            self.display_var.set(result)
            self.expression = result

        except ZeroDivisionError:
            self.display_var.set("Cannot divide by zero")
            self.expression = ""

        except Exception:
            self.display_var.set("Invalid Expression")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.display_var.set("")

    def backspace(self):
        self.expression = self.expression[:-1]
        self.display_var.set(self.expression)


def main():
    root = tk.Tk()
    Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()