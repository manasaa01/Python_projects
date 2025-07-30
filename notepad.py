from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("600x600")
root.title("NOTEPAD")
root.configure(bg="lightblue")
root.resizable(False, False)

def save_file():
    file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if file is not None:
        text = entry.get("1.0", END)
        file.write(text)
        file.close()

def open_file_dialog():
    file = filedialog.askopenfile(mode='r', defaultextension='.txt')
    if file is not None:
        content = file.read()
        entry.delete("1.0", END)
        entry.insert(INSERT, content)
        file.close()

# Buttons
Button(root, width=20, height=2, bg='#fff', text="Save File", command=save_file).place(x=100, y=5)
Button(root, width=20, height=2, bg='#fff', text="Open File", command=open_file_dialog).place(x=300, y=5)

# Text area
entry = Text(root, height=33, width=72, wrap=WORD)
entry.place(x=10, y=60)

root.mainloop()
