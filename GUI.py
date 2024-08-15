import tkinter as tk
def get_text(text,on=False):
    if on:
        #text widget editing
        result_text.config(state="normal")
        #clear previous content
        result_text.delete("1.0",tk.END)
        #insert new text
        result_text.insert(tk.END,text)
        #disable text widget
        result_text.config(state="disabled")
def start():
    #retrieve text from input field
    text=length_entry.get()
    #retrieve state of checkbox
    on=checkbox_var.get()
    #calling get_text fun
    get_text(text,on)
#create main window
root=tk.Tk()
root.title("GUI EXAMPLE")
root.geometry("500x600")
#widgets
length_label=tk.Label(root,text="enter number")
length_label.pack()
#input field
length_entry=tk.Entry(root)
length_entry.pack()
#button
button=tk.Button(root,text="Getx text" ,command=start)
button.pack()
#check box
checkbox_var=tk.BooleanVar(value=True)
checkbox=tk.Checkbutton(root,text="true or false",variable=checkbox_var)
checkbox.pack()
#text widget
result_text=tk.Text(root,wrap="word",height=5,state="disabled")
result_text.pack()

#run the application
root.mainloop()
