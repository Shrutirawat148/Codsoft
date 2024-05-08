import re
import secrets
import string
from tkinter import *
import tkinter as tk            # importing the tkinter module as tk  
from tkinter import ttk         # importing the ttk module from the tkinter library  
from tkinter import messagebox

def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password
def print_variable(label):
    # Retrieve the value of the variable
    variable_value = generate_password()
    # Update the label with the variable's value
    label.config(text=f"The generated password is: {variable_value}",font = ("Consolas", "11", "bold"))
def close():  
    # using the destroy() method to close the application  
    guiWindow.destroy()    
def main():
    pass
if __name__=='__main__':
        # creating an object of the Tk() class  
    guiWindow = tk.Tk()  
    # setting the title of the window  
    guiWindow.title("Password Generator")  
    # setting the geometry of the window  
    guiWindow.geometry("500x500+750+250")  
    # disabling the resizable option  
    guiWindow.resizable(0, 0)  
    # setting the background color   
    guiWindow.configure(bg = "#654321") 

    # print('Generated password:', new_password)
    header_frame = tk.Frame(guiWindow, bg = "#654321")  
    functions_frame = tk.Frame(guiWindow, bg = "#654321")  
    listbox_frame = tk.Frame(guiWindow, bg = "#654321") 
    # using the pack() method to place the frames in the application  
    header_frame.pack(fill = "both")  
    functions_frame.pack(side = "left", expand = True, fill = "both")  
    # listbox_frame.pack(side = "right", expand = True, fill = "both")  

    header_label = ttk.Label(  
        header_frame,  
        text = "Password Generator",  
        font = ("Brush Script MT", "30"),  
        background = "#654321",  
        foreground = "#fff"  
    )  
    # using the pack() method to place the label in the application  
    header_label.pack(padx = 20, pady = 20)  
  
    # defining another label using the ttk.Label() widget  
    task_label = ttk.Label(  
        functions_frame,  
        text = "Do you want to generate the password",  
        font = ("Consolas", "11", "bold"),  
        background = "#654321",  
        foreground = "#fff"  
    )  
    # using the place() method to place the label in the application  
    task_label.place(x = 20, y = 40)

    add_button = ttk.Button(  
    functions_frame,  
    text = "YES",  
    width = 24,  
    command =lambda:print_variable(password_label)
    ) 
    exit_button = ttk.Button(  
    functions_frame,  
    text = "Exit",  
    width = 24,  
    command = close  
    )
    # Create a Label to display the generated password
    password_label = ttk.Label(  
        functions_frame,  
        text = "",  # Initially empty
        font = ("Consolas", "11"),  
        background = "#654321",  
        foreground = "#fff"  
    )
    # using the place() method to place the label in the application  
    password_label.place(x = 20, y = 80)
    add_button.place(x = 30, y = 120) 
    exit_button.place(x = 250, y = 120)    
    guiWindow.mainloop()