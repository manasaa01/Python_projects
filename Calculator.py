
import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.config(bg="#1e1e1e")

# Input field
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Arial 20 bold", bd=10, relief="sunken", justify="right")
entry.pack(fill="x", padx=10, pady=10)

# Button frame
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

# Button labels
buttons = [
    ['7', '8', '9', '+'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '*'],
    ['C', '0', '=', '/']
]

# Create buttons
for row in buttons:
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font="Arial 18", width=5, height=2, bg="#333", fg="white")
        btn.grid(row=buttons.index(row), column=row.index(btn_text), padx=5, pady=5)
        btn.bind("<Button-1>", click)

root.mainloop()
