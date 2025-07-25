import tkinter as tk
import customtkinter as ctk

app = ctk.CTk()
app.title("Calculator")
ctk.set_appearance_mode("dark")
app.geometry("400x600")

import re

def solve_with_ints(expr):
    print(expr)
    def to_int(match):
        return str(int(float(match.group())))

    expr_inted = re.sub(r'\d*\.\d+|\d+\.\d*|\d+', to_int, expr)
    textbox.delete("1.0", tk.END)
    result = eval(expr_inted)
    textbox.insert(tk.END, result)
    return 



textbox = ctk.CTkTextbox(app, width=400, height=100, font=("Arial", 76), )
textbox.pack(pady=20)

button1 = ctk.CTkButton(app, text="1", width=80, height=80, command=lambda: textbox.insert(tk.END, "1"), font=("Arial", 36), fg_color="#343634", hover_color="#2a2b2a")
button1.place(y=150, x=20)

button2 = ctk.CTkButton(app, text="2", width=80, height=80, command=lambda: textbox.insert(tk.END, "2"), font=("Arial", 36), fg_color="#343634", hover_color="#2a2b2a")
button2.place(y=150, x=120)

button3 = ctk.CTkButton(app, text="3", width=80, height=80, command=lambda: textbox.insert(tk.END, "3"), font=("Arial", 36), fg_color="#343634", hover_color="#2a2b2a")
button3.place(y=150, x=220)

button_plus = ctk.CTkButton(app, text="+", width=80, height=80, command=lambda: textbox.insert(tk.END, "+"), font=("Arial", 36), fg_color="#bf780d", hover_color="#945c09")
button_plus.place(y=150, x=320)

button4 = ctk.CTkButton(app, text="4", width=80, height=80, command=lambda: textbox.insert(tk.END, "4"), font=("Arial", 36), fg_color="#343634", hover_color="#2a2b2a")
button4.place(y=250, x=20)

button5 = ctk.CTkButton(app, text="5", width=80, height=80, command=lambda: textbox.insert(tk.END, "5"), font=("Arial", 36), fg_color="#343634", hover_color="#2a2b2a")
button5.place(y=250, x=120)

button6 = ctk.CTkButton(app, text="6", width=80, height=80, command=lambda: textbox.insert(tk.END, "6"), font=("Arial", 36), fg_color="#343634", hover_color="#2a2b2a")
button6.place(y=250, x=220)

button_minus = ctk.CTkButton(app, text="-", width=80, height=80, command=lambda: textbox.insert(tk.END, "-") , font=("Arial", 36), fg_color="#bf780d", hover_color="#945c09")
button_minus.place(y=250, x=320)

button7 = ctk.CTkButton(app, text="7", width=80, height=80, command=lambda: textbox.insert(tk.END, "7"), font=("Arial", 36), fg_color="#343634", hover_color="#252625")
button7.place(y=350, x=20)

button8 = ctk.CTkButton(app, text="8", width=80, height=80, command=lambda: textbox.insert(tk.END, "8"), font=("Arial", 36), fg_color="#343634", hover_color="#2a2b2a")
button8.place(y=350, x=120)

button9 = ctk.CTkButton(app, text="9", width=80, height=80, command=lambda: textbox.insert(tk.END, "9"), font=("Arial", 36), fg_color="#343634", hover_color="#2a2b2a")
button9.place(y=350, x=220)

button_times = ctk.CTkButton(app, text="*", width=80, height=80, command=lambda: textbox.insert(tk.END, "*") , font=("Arial", 36), fg_color="#bf780d", hover_color="#945c09")
button_times.place(y=350, x=320)

button0 = ctk.CTkButton(app, text="0", width=80, height=80, command=lambda: textbox.insert(tk.END, "0"), font=("Arial", 36), fg_color="#343634", hover_color="#2a2b2a")
button0.place(y=450, x=20)

button_clear = ctk.CTkButton(app, text="C", width=80, height=80, command=lambda: textbox.delete("1.0", tk.END), font=("Arial", 36), fg_color="#bf780d", hover_color="#945c09")
button_clear.place(y=450, x=120)

button_equals = ctk.CTkButton(app, text="=", width=80, height=80, command= lambda: solve_with_ints(textbox.get("1.0", tk.END).strip()), font=("Arial", 36), fg_color="#bf780d", hover_color="#945c09")
button_equals.place(y=450, x=220)

button_divide = ctk.CTkButton(app, text="/", width=80, height=80, command=lambda: textbox.insert(tk.END, "/") , font=("Arial", 36), fg_color="#bf780d", hover_color="#945c09")
button_divide.place(y=450, x=320)



app.mainloop()