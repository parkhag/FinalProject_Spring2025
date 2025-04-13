# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 11:57:58 2025

@author: alexa
"""
# REMEMBER TO CHANGE FILE DIRECTORY AT LINE 112 BEFORE RUNNING THE CODE!!!!

import tkinter as tk
from tkinter import ttk
import os


# Function to pull the names of each file in a folder
def get_folder_contents(folder_path):
  try:
    contents = os.listdir(folder_path)  #Using OS get the directory of all files as a list and store as content
    return contents
  except FileNotFoundError: #If the file is found return error
    return f"Error: Folder '{folder_path}' not found."
  except NotADirectoryError:    #If directory not found return error
      return f"Error: '{folder_path}' is not a directory."
  except Exception as e:    #Error of other exceptions
      return f"An error occurred: {e}"

class TaskManager:  #Task Class to handle the editing of to do list and notes
    def __init__(self, file_path, file_name):   #Create the constructor with file_path and file_name
        self.file_path = file_path + file_name  #Creates combined directory
        self.tasks = []                 #List that stores the pending tasks
        self.completed = []             #List that stores the completed tasks
        self.notes = []                 #List that stores the notes
        self.load_data()                #Calls the load_data function
    
    def load_data(self):    #function that loads the data from the .txt file
        try:    #closes .txt file after being read
            with open(self.file_path, 'r') as text_file:    #opens the file as read
                lines = text_file.readlines()
                reading_notes = False
                for line in lines:
                    line = line.strip()     #strips the each line to be filtered
                    if line == "":
                        continue  # Skip empty lines
                    if line.strip() == "# Notes Start": #filters out Notes Start
                        reading_notes = True
                        continue
                    if reading_notes:
                        self.notes.append(line)
                    else:
                        if ' - ' in line:        #if the to do status is marked as completed add to completed list   
                            task, status = line.split(' - ')
                            self.tasks.append(task)
                            self.completed.append(status == "Completed")
                        else:
                            print(f"Skipping invalid line: {line}")  # Optionally log invalid lines
        except FileNotFoundError:
            print("No existing task file found. Creating new one.")
            self.create_new_file()


    def create_new_file(self):  #Create new file
        if os.path.exists(self.file_path):  #if the file already exists don't allow the user to overwrite the file
            print(f"File already exists: {self.file_path}. Creation skipped.")
            return False
        else:
            with open(self.file_path, 'w') as text_file:
                text_file.write("# New File Created\n")
            print(f"New file created: {self.file_path}")
            return True

    def save_data(self):    #saves the new list data to the .txt file
        with open(self.file_path, 'w') as text_file:
            for task, status in zip(self.tasks, self.completed):
                text_file.write(f"{task} - {'Completed' if status else 'Pending'}\n")
            text_file.write("# Notes Start\n")
            for note in self.notes:
                text_file.write(f"{note}\n")
      
    def add_task(self, task):   #adds a new task to the list of tasks and saves
        self.tasks.append(task)
        self.completed.append(False)
        self.save_data()
    
    def delete_task(self, task_name):   #deletes task if it is found in the tasks list
        if task_name in self.tasks:
            index = self.tasks.index(task_name)
            del self.tasks[index]
            del self.completed[index]
            self.save_data()
            return True
        return False
    
    def complete_task(self, task_name): #if the task name is found in the tasks list it marks it as completed in its complementary position in the completed list
        if task_name in self.tasks:
            index = self.tasks.index(task_name)
            self.completed[index] = True
            self.save_data()
            return True
        return False
    
    def edit_note(self, index, new_note):   #Updates the note to knew note string
        if 0 <= index < len(self.notes):
            self.notes[index] = new_note
            self.save_data()
            return True
        return False
    
    

# ----------------------------------------

# Constructor Initializing
file_path = "C:/Users/alexa/OneDrive/Documents/Text Files/"  # Default path to current directory

def update_textbox():   #updates the text box with loaded data every time it is edited via a function button
    task_list = "\n".join([f"{task} - {'Completed' if status else 'Pending'}" for task, status in zip(task_manager.tasks, task_manager.completed)]) #prints the list of tasks with respective statuses
    notes_list = "\n".join(task_manager.notes)  #prints the notes list
    text_box.config(state=tk.NORMAL)
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, f"Tasks:\n{task_list}\n\n# Notes:\n{notes_list}")
    text_box.config(state=tk.DISABLED)
    list_box.delete(0, tk.END)
    for note in task_manager.notes:
        list_box.insert(tk.END, note)

def add_task_button():  #adds tasks as the string typed into the input bar
    task = entry.get()
    if task:
        task_manager.add_task(task)
        entry.delete(0, tk.END)
        update_textbox()
        status_label.config(text="Task added.", fg="green") #status statement

def delete_task_button():   #deletes tasks as the string typed into the input bar
    task_name = entry.get()
    if task_name:           #only does so if the task_name matches a corresponding task string stored in the tasks list
        success = task_manager.delete_task(task_name)
        if success:
            entry.delete(0, tk.END)
            update_textbox()
            status_label.config(text="Task deleted.", fg="red")
        else:
            status_label.config(text="Task not found.", fg="red")

def complete_task_button():     #marks as task as completed via its completed list
    task_name = entry.get()
    if task_name:
        success = task_manager.complete_task(task_name)
        if success:
            entry.delete(0, tk.END)
            update_textbox()
            status_label.config(text="Task completed.", fg="green")
        else:
            status_label.config(text="Task not found.", fg="red")

def add_note_button():      #adds a note to the note list
    note = entry.get()
    if note:
        task_manager.notes.append(note)
        task_manager.save_data()
        entry.delete(0, tk.END)
        update_textbox()
        status_label.config(text="Note added.", fg="blue")

def edit_note_button():     #update a note from the note list depending on the input from the input bar
    note = entry.get()
    selected_index = list_box.curselection()
    if note and selected_index:
        note_index = selected_index[0]
        success = task_manager.edit_note(note_index, note)
        if success:
            entry.delete(0, tk.END)
            update_textbox()
            status_label.config(text="Note edited.", fg="blue")
        else:
            status_label.config(text="Failed to edit note.", fg="red")
            
def delete_note_button():   #deletes the note
    selected_index = list_box.curselection()
    if selected_index:
        note_index = selected_index[0]
        del task_manager.notes[note_index]
        task_manager.save_data()
        update_textbox()
        status_label.config(text="Note deleted.", fg="red")
    else:
        status_label.config(text="No note selected.", fg="red")


# ----------------------- GUI Integration with Tkinter ------------------------

root = tk.Tk()      #initializing the root window
root.title("Task Manager")  #naming the root window
root.geometry("500x200")    #sizing for the root window


def open_first_window():    #function that stores the widgets for the note To Do List Editor
    global task_manager, text_box, entry, list_box, status_label
    first_window = tk.Toplevel()    #pushes the window to the top level
    first_window.title("To Do List Editor") #titles the window
    first_window.geometry("800x800")    #sizes the window
    file_name = selected_option.get()   #from the file name selected from the dropdown opens the corresponding file
    task_manager = TaskManager(file_path, file_name)    #creates a constructor with the Task Manager class
    text_box = tk.Text(first_window, wrap="word", width=60, height=15)  #sizing for text box
    text_box.pack(pady=10)  
    label = tk.Label(first_window, text="To Do List Editor")    #label for the window
    label.pack()
    entry = tk.Entry(first_window, width=60)
    entry.pack(pady=5)
    list_box = tk.Listbox(first_window, height=5, width=60) #input bar for the user to type in
    list_box.pack(pady=5)
    status_label = tk.Label(first_window, text="", fg="red")    #status label
    status_label.pack(pady=5)
    button_frame = tk.Frame(first_window)
    button_frame.pack(pady=20)  
    
    #To Do List Buttons
    add_button = tk.Button(first_window, text="Add Task", command=add_task_button)  #add button that adds tasks
    add_button.pack(side='left',expand=True, padx=10, anchor="center")
    complete_button = tk.Button(first_window, text="Complete Task", command=complete_task_button)   #complete button that completes tasks
    complete_button.pack(side='left', padx=10, anchor="center")
    delete_button = tk.Button(first_window, text="Delete Task", command=delete_task_button) #delete button that deletes tasks
    delete_button.pack(side='left',expand=True, padx=10, anchor="center")
    
    #Note Buttons
    add_note_btn = tk.Button(first_window, text="Add Note", command=add_note_button)    #add note button that adds note
    add_note_btn.pack(side='left', expand=True, padx=10, anchor="center")
    edit_note_btn = tk.Button(first_window, text="Edit Note", command=edit_note_button) #edit note button that edits note
    edit_note_btn.pack(side='left', expand=True, padx=10, anchor="center")
    delete_note_btn = tk.Button(first_window, text="Delete Note", command=delete_note_button)   #delete note button that deltes a note
    delete_note_btn.pack(side='left', expand=True, padx=10, anchor="center")
    
    # Other buttons
    close_button = tk.Button(first_window, text="Close", command=first_window.destroy)      #closes the To Do List editor window
    close_button.pack(side='bottom', padx=10, anchor="center")
    button_frame.pack(anchor="center")
    
    update_textbox() #updates the textbox
    
    
    
def create():   #function for creating new file
    file_name = createbox.get()
    task_manager = TaskManager(file_path, file_name)
    if task_manager.create_new_file() == True:  #calls create new file from 
        create_window.destroy()         #closes the window after the file is created
        RefreshFolder()                 #refreshes the file list dropdown
    else:
        status_labelc.config(text="File Already Exists", fg="red") #status statement

    
def open_create_window():   #Creation of the window for new file creation
    global createbox, create_window, status_labelc
    create_window = tk.Toplevel()
    create_window.title("Create File")
    create_window.geometry("500x200")
    createbox = tk.Entry(create_window, width=60)   #box used inputing file name
    createbox.pack(pady=10)
    create_frame = tk.Frame(create_window)  #used to group the buttons vertically
    create_frame.pack(pady=5)
    create_button = tk.Button(create_frame, text="Create", command=create)  #create button for creating a new file
    create_button.pack()
    status_labelc = tk.Label(create_frame, text="", fg="red")   # status that returns when error occurs
    status_labelc.pack()
    close_button = tk.Button(create_window, text="Close", command=create_window.destroy)    #close button to exit window
    close_button.pack(side='bottom', padx=10, anchor="center")
    

def RefreshFolder():    #function to refresh the folder
    new_options = get_folder_contents(file_path)    #pulls the new list of options from the get_folder_contents function
    dropdown['values'] = new_options   #sets the dropdown to refreshed list of options
    if new_options:     #If there are new options ser them
        selected_option.set(new_options[0])
    else:
        selected_option.set("") #if no option set set nothing
        
selected_option = tk.StringVar()    #get the option selected by the user from the dropdown menu
initial_options = get_folder_contents(file_path)    #get the initial options from the get_folder_contents function
dropdown = ttk.Combobox(root, textvariable=selected_option, values=initial_options) #create a dropdown menu in the root window
dropdown.pack(pady=10)

if initial_options: 
    selected_option.set(initial_options[0]) #sets the list of files from folder to dropdown menu
    
RefreshFolder()
dropdown.pack(pady=20)  #place the drowdown widget


def option_changed():  #function to change the option variable when a new dropdown is selected
    print("selected option:", selected_option.get())

dropdown.bind("<<ComboboxSelected>>", option_changed)   #if new option selected call option_changed function
open_button = tk.Button(root, text="Open", command=open_first_window)   #open button that 
open_button.pack(side='left', expand=True, padx=10, anchor="center")    #place button
create_window_button = tk.Button(root, text="Create New File", command=open_create_window)  #button for create new file
create_window_button.pack(side='left', expand=True, padx=10, anchor="center")   #place button


# Run the Tkinter event loop
root.mainloop() 
