import tkinter as tk
def button_click():
    label.config(text="Hello")
root=tk.Tk()
root.title('Tkinter GUI')
label=tk.Label(root,text='Welcome')
label.pack()
button=tk.Button(root,text='Show',command=button_click())
button.pack
root.mainloop()


