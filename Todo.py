from tkinter import *
import tkinter as tk            # importing the tkinter module as tk  
from tkinter import ttk         # importing the ttk module from the tkinter library  
from tkinter import messagebox 
import sqlite3 as sql

tasks=[]
def add_task():  
    # getting the string from the entry field  
    task_string = task_field.get()  
    # checking whether the string is empty or not  
    if len(task_string) == 0:  
        # displaying a message box with 'Empty Field' message  
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:  
        # adding the string to the tasks list  
        tasks.append(task_string)  
        # using the execute() method to execute a SQL statement  
        the_cursor.execute('insert into tasks values (?)', (task_string,))  
        # calling the function to update the list  
        list_update()  
        # deleting the entry in the entry field  
        task_field.delete(0, 'end')  


def list_update():  
    # calling the function to clear the list  
    clear_list()  
    # iterating through the strings in the list  
    for task in tasks:  
        # using the insert() method to insert the tasks in the list box  
        task_listbox.insert('end', task)  


def delete_task():  
    # using the try-except method  
    try:  
        # getting the selected entry from the list box  
        the_value = task_listbox.get(task_listbox.curselection())  
        # checking if the stored value is present in the tasks list  
        if the_value in tasks:  
            # removing the task from the list  
            tasks.remove(the_value)  
            # calling the function to update the list  
            list_update()  
            # using the execute() method to execute a SQL statement  
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:  
        # displaying the message box with 'No Item Selected' message for an exception  
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')  

def delete_all_tasks():  
    # displaying a message box to ask user for confirmation  
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    # if the value turns to be True  
    if message_box == True:  
        # using while loop to iterate through the tasks list until it's empty   
        while(len(tasks) != 0):  
            # using the pop() method to pop out the elements from the list  
            tasks.pop()  
        # using the execute() method to execute a SQL statement  
        the_cursor.execute('delete from tasks')  
        # calling the function to update the list  
        list_update()  


def clear_list():  
    # using the delete method to delete all entries from the list box  
    task_listbox.delete(0, 'end')  


def close():  
    # printing the elements from the tasks list  
    print(tasks)  
    # using the destroy() method to close the application  
    guiWindow.destroy() 

def retrieve_database():  
    # using the while loop to iterate through the elements in the tasks list  
    while(len(tasks) != 0):  
        # using the pop() method to pop out the elements from the list  
        tasks.pop()  
    # iterating through the rows in the database table  
    for row in the_cursor.execute('select title from tasks'):  
        # using the append() method to insert the titles from the table to the list  
        tasks.append(row[0])  



if __name__ == "__main__":  
    # creating an object of the Tk() class  
    guiWindow = tk.Tk()  
    # setting the title of the window  
    guiWindow.title("To-Do List")  
    # setting the geometry of the window  
    guiWindow.geometry("500x500+750+250")  
    # disabling the resizable option  
    guiWindow.resizable(0, 0)  
    # setting the background color   
    guiWindow.configure(bg = "#654321")  

    the_connection = sql.connect('listOfTasks.db')  
    # creating an object of the cursor class  
    the_cursor = the_connection.cursor()  
    # using the execute() method to execute a SQL statement  
    the_cursor.execute('create table if not exists tasks (title text)')  

    header_frame = tk.Frame(guiWindow, bg = "#654321")  
    functions_frame = tk.Frame(guiWindow, bg = "#654321")  
    listbox_frame = tk.Frame(guiWindow, bg = "#654321")  
  
    # using the pack() method to place the frames in the application  
    header_frame.pack(fill = "both")  
    functions_frame.pack(side = "left", expand = True, fill = "both")  
    listbox_frame.pack(side = "right", expand = True, fill = "both")  

    header_label = ttk.Label(  
        header_frame,  
        text = "The To-Do List",  
        font = ("Brush Script MT", "30"),  
        background = "#654321",  
        foreground = "#fff"  
    )  
    # using the pack() method to place the label in the application  
    header_label.pack(padx = 20, pady = 20)  
  
    # defining another label using the ttk.Label() widget  
task_label = ttk.Label(  
    functions_frame,  
    text = "Enter the Task:",  
    font = ("Consolas", "11", "bold"),  
    background = "#654321",  
    foreground = "#fff"  
)  
# using the place() method to place the label in the application  
task_label.place(x = 30, y = 40)  


task_field = ttk.Entry(  
    functions_frame,  
    font = ("Consolas", "12"),  
    width = 18,  
    background = "#FFF8DC",  
    foreground = "#A52A2A"  
)  
# using the place() method to place the entry field in the application  
task_field.place(x = 30, y = 80)  

add_button = ttk.Button(  
    functions_frame,  
    text = "Add Task",  
    width = 24,  
    command = add_task  
)  
del_button = ttk.Button(  
    functions_frame,  
    text = "Delete Task",  
    width = 24,  
    command = delete_task  
)  
del_all_button = ttk.Button(  
    functions_frame,  
    text = "Delete All Tasks",  
    width = 24,  
    command = delete_all_tasks  
)  
exit_button = ttk.Button(  
    functions_frame,  
    text = "Exit",  
    width = 24,  
    command = close  
)  
# using the place() method to set the position of the buttons in the application  
add_button.place(x = 30, y = 120)  
del_button.place(x = 30, y = 160)  
del_all_button.place(x = 30, y = 200)  
exit_button.place(x = 30, y = 240)  


task_listbox = tk.Listbox(  
    listbox_frame,  
    width = 26,  
    height = 13,  
    selectmode = 'SINGLE',  
    background = "#FFFFFF",  
    foreground = "#000000",  
    selectbackground = "#CD853F",  
    selectforeground = "#FFFFFF"  
)  
# using the place() method to place the list box in the application  
task_listbox.place(x = 10, y = 20)  

retrieve_database()  
list_update()  
# using the mainloop() method to run the application  
guiWindow.mainloop()  
# establishing the connection with database  
the_connection.commit()  
the_cursor.close()  