# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 01:04:19 2025

@author: hayeg
"""

import tkinter as tk
from tkinter import ttk
import os

def get_folder_contents(folder_path):
  """
  Retrieves the contents of a specified folder.

  Args:
      folder_path: The path to the folder.

  Returns:
      A list of strings, where each string is the name of a file or a subfolder 
      within the specified folder.
  """
  try:
    contents = os.listdir(folder_path)
    return contents
  except FileNotFoundError:
    return f"Error: Folder '{folder_path}' not found."
  except NotADirectoryError:
      return f"Error: '{folder_path}' is not a directory."
  except Exception as e:
      return f"An error occurred: {e}"

class TaskManager:
    def __init__(self, file_path, file_name):
        self.file_path = file_path + file_name
        self.tasks = []
        self.completed = []
        self.notes = []
        self.load_data()
    
    def load_data(self):
        try:
            with open(self.file_path, 'r') as text_file:
                lines = text_file.readlines()
                reading_notes = False
                for line in lines:
                    line = line.strip()
                    if line == "":
                        continue  # Skip empty lines
                    if line.strip() == "# Notes Start":
                        reading_notes = True
                        continue
                    if reading_notes:
                        self.notes.append(line)
                    else:
                    # Check if the line contains both task and status
                        if ' - ' in line:
                            task, status = line.split(' - ')
                            self.tasks.append(task)
                            self.completed.append(status == "Completed")
                        else:
                            print(f"Skipping invalid line: {line}")  # Optionally log invalid lines
        except FileNotFoundError:
            print("No existing task file found. Creating new one.")
            self.create_new_file()


    def create_new_file(self):
        with open(self.file_path, 'w') as text_file:
            text_file.write("# New File Created\n")
        print(f"New file created: {self.file_path}")

    def save_data(self):
        with open(self.file_path, 'w') as text_file:
            for task, status in zip(self.tasks, self.completed):
                text_file.write(f"{task} - {'Completed' if status else 'Pending'}\n")
            text_file.write("# Notes Start\n")
            for note in self.notes:
                text_file.write(f"{note}\n")
      
    def add_task(self, task):
        self.tasks.append(task)
        self.completed.append(False)
        self.save_data()
    
    def delete_task(self, task_name):
        if task_name in self.tasks:
            index = self.tasks.index(task_name)
            del self.tasks[index]
            del self.completed[index]
            self.save_data()
            return True
        return False
    
    def complete_task(self, task_name):
        if task_name in self.tasks:
            index = self.tasks.index(task_name)
            self.completed[index] = True
            self.save_data()
            return True
        return False
    
    def edit_note(self, index, new_note):
        if 0 <= index < len(self.notes):
            self.notes[index] = new_note
            self.save_data()
            return True
        return False

# ----------------------------------------

# Constructor Initializing
file_path = "C:/Users/alexa/OneDrive/Documents/Text Files/"  # Default path to current directory

def update_textbox():
    task_list = "\n".join([f"{task} - {'Completed' if status else 'Pending'}" for task, status in zip(task_manager.tasks, task_manager.completed)])
    notes_list = "\n".join(task_manager.notes)
    text_box.config(state=tk.NORMAL)
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, f"Tasks:\n{task_list}\n\n# Notes:\n{notes_list}")
    text_box.config(state=tk.DISABLED)
    list_box.delete(0, tk.END)
    for note in task_manager.notes:
        list_box.insert(tk.END, note)

def add_task_button():
    task = entry.get()
    if task:
        task_manager.add_task(task)
        entry.delete(0, tk.END)
        update_textbox()
        status_label.config(text="Task added.", fg="green")

def delete_task_button():
    task_name = entry.get()
    if task_name:
        success = task_manager.delete_task(task_name)
        if success:
            entry.delete(0, tk.END)
            update_textbox()
            status_label.config(text="Task deleted.", fg="red")
        else:
            status_label.config(text="Task not found.", fg="red")

def complete_task_button():
    task_name = entry.get()
    if task_name:
        success = task_manager.complete_task(task_name)
        if success:
            entry.delete(0, tk.END)
            update_textbox()
            status_label.config(text="Task completed.", fg="green")
        else:
            status_label.config(text="Task not found.", fg="red")

def add_note_button():
    note = entry.get()
    if note:
        task_manager.notes.append(note)
        task_manager.save_data()
        entry.delete(0, tk.END)
        update_textbox()
        status_label.config(text="Note added.", fg="blue")

def edit_note_button():
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


# ----------------------- GUI Integration with Tkinter ------------------------

root = tk.Tk()
root.title("Task Manager")
root.geometry("500x200")


#------------


def open_first_window():
    global task_manager, text_box, entry, list_box, status_label
    first_window = tk.Toplevel()
    first_window.title("To Do List Editor")
    first_window.geometry("800x800")
    file_name = selected_option.get()
    task_manager = TaskManager(file_path, file_name)
    text_box = tk.Text(first_window, wrap="word", width=60, height=15)
    text_box.pack(pady=10)
    label = tk.Label(first_window, text="To Do List Editor")
    label.pack()
    entry = tk.Entry(first_window, width=60)
    entry.pack(pady=5)
    list_box = tk.Listbox(first_window, height=5, width=60)
    list_box.pack(pady=5)
    status_label = tk.Label(first_window, text="", fg="red")
    status_label.pack(pady=5)
    button_frame = tk.Frame(first_window)
    button_frame.pack(pady=20)  
    
    add_button = tk.Button(first_window, text="Add Task", command=add_task_button)
    add_button.pack(side='left',expand=True, padx=10, anchor="center")
    complete_button = tk.Button(first_window, text="Complete Task", command=complete_task_button)
    complete_button.pack(side='left', padx=10, anchor="center")
    delete_button = tk.Button(first_window, text="Delete Task", command=delete_task_button)
    delete_button.pack(side='left',expand=True, padx=10, anchor="center")
    
    add_note_btn = tk.Button(first_window, text="Add Note", command=add_note_button)
    add_note_btn.pack(side='left', expand=True, padx=10, anchor="center")
    edit_note_btn = tk.Button(first_window, text="Edit Note", command=edit_note_button)
    edit_note_btn.pack(side='left', expand=True, padx=10, anchor="center")
    close_button = tk.Button(first_window, text="Close", command=first_window.destroy)
    close_button.pack(side='bottom', padx=10, anchor="center")
    button_frame.pack(anchor="center")
    
    update_textbox()
    
    
    
def create():
    file_name = createbox.get()
    task_manager = TaskManager(file_path, file_name)
    task_manager.create_new_file()
    create_window.destroy()
    RefreshFolder()
    
def open_create_window():
    global createbox, create_window
    create_window = tk.Toplevel()
    create_window.title("Create File")
    create_window.geometry("500x200")
    createbox = tk.Entry(create_window, width=60)
    createbox.pack(pady=10)
    create_button = tk.Button(create_window, text="Create", command=create)
    create_button.pack(side='lSeft', expand=True, padx=10, anchor="center")

    


def RefreshFolder():
    new_options = get_folder_contents(file_path)
    dropdown['values'] = new_options
    if new_options:
        selected_option.set(new_options[0])
    else:
        selected_option.set("")
        
selected_option = tk.StringVar()
initial_options = get_folder_contents(file_path)
dropdown = ttk.Combobox(root, textvariable=selected_option, values=initial_options)
dropdown.pack(pady=10)

if initial_options:
    selected_option.set(initial_options[0])

    
RefreshFolder()
dropdown.pack(pady=20)


def option_changed(event):
    print("selected option:", selected_option.get())

dropdown.bind("<<ComboboxSelected>>", option_changed)
open_button = tk.Button(root, text="Open", command=open_first_window)
open_button.pack(side='left', expand=True, padx=10, anchor="center")
create_window_button = tk.Button(root, text="Create New File", command=open_create_window)
create_window_button.pack(side='left', expand=True, padx=10, anchor="center")


# Run the Tkinter event loop
root.mainloop()