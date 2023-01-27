import tkinter as tk

def on_submit():
    # Get the values of the user and password fields
    username = user_var.get()
    password = pass_var.get()
    # Print the values for demonstration purposes
    print("Username:", username)
    print("Password:", password)

# Create the main window
root = tk.Tk()

# Set the window title and size
root.title("Inicio de sesión")
root.geometry("400x300")

# Create variables to store the user and password input
user_var = tk.StringVar()
pass_var = tk.StringVar()

# Create a label for the username field
user_label = tk.Label(root, text="Usuario:")
user_label.pack()

# Create an entry widget for the username field
user_entry = tk.Entry(root, textvariable=user_var)
user_entry.pack()

# Create a label for the password field
pass_label = tk.Label(root, text="Contraseña:")
pass_label.pack()

# Create an entry widget for the password field, with the show="*" option to mask the input
pass_entry = tk.Entry(root, textvariable=pass_var, show="*")
pass_entry.pack()

# Create a submit button
submit_button = tk.Button(root, text="Iniciar sesión", command=on_submit)
submit_button.pack()

# Run the main loop
root.mainloop()