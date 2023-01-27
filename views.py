import tkinter as tk

def on_button_click():
    print("Button was clicked!")

root = tk.Tk()
root.attributes("-fullscreen", True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# Create two entry widgets
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

# Create two buttons
button1 = tk.Button(root, text="Button 1")
button2 = tk.Button(root, text="Button 2")

# Position the widgets on the screen
entry1.pack()
entry2.pack()
button1.pack()
button2.pack()
label1 = tk.Label(root, text="Ingrese texto 1:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

#ASCII
art = " _____ ____  \n|_   _/ ___| \n  | || |     \n  | || |___  \n  |_| \____| "
label = tk.Label(root, text=art, font=("courier", 12))

# Create label
label = tk.Label(root, text=art, font=("courier", 12), bg="black", fg="white")

# Position label in the center
label.place(relx=0.5, rely=0.5, anchor="center")

#ASCII art


# Minimize button
minimize_button = tk.Button(root, text="-", command=root.iconify)
minimize_button.place(x=root.winfo_screenwidth()-50, y=0)
minimize_button.config(bg='blue',fg='white',bd=0)

# Close button
close_button = tk.Button(root, text="X", command=root.destroy)
close_button.place(x=root.winfo_screenwidth()-25, y=0)
close_button.config(bg='red',fg='white',bd=0)
root.mainloop()
