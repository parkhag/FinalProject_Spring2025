# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 12:48:08 2025

@author: hayeg
"""
import tkinter as tk

class TaskManager:
    def __init__(self, file_path, file_name):
        self.file_path = file_path + file_name + ".txt"
        self.tasks = []  # List to hold tasks
        self.completed = []  # List to hold completion status of tasks
        self.load_tasks()  # Load tasks from the file when initializing
    
    def load_tasks(self):
        """Load tasks and completion status from the text file."""
        try:
            with open(self.file_path, 'r') as text_file:
                lines = text_file.readlines()
                for line in lines:
                    task, status = line.strip().split(' - ')
                    self.tasks.append(task)
                    self.completed.append(True if status == "Completed" else False)
        except FileNotFoundError:
            print(f"No existing task file found at {self.file_path}. Starting with an empty list.")
    
    def save_tasks(self):
        """Save tasks and their completion status to the text file."""
        with open(self.file_path, 'w') as text_file:
            for task, status in zip(self.tasks, self.completed):
                status_str = "Completed" if status else "Pending"
                text_file.write(f"{task} - {status_str}\n")
        print(f"Tasks saved to {self.file_path}\n")
    
    def add_task(self, task):
        self.tasks.append(task)  # Add task to list
        self.completed.append(False)  # Mark the task as incomplete
        self.save_tasks()  # Save tasks after adding
    
    def view_tasks(self):
        if not self.tasks:  # Check if there are any tasks
            return "No tasks to display."
        else:
            task_list = ""
            for i in range(len(self.tasks)):  # Loop over the list of tasks
                status = "Completed" if self.completed[i] else "Pending"
                task_list += f"{self.tasks[i]} - {status}\n"
            return task_list
    
    def complete_task(self, task_name):
        if task_name in self.tasks:  # If task name is in the list
            index = self.tasks.index(task_name)  # Get the index of the task
            self.completed[index] = True  # Mark it as completed
            self.save_tasks()  # Save tasks after completing
            return f"'{task_name}' is now complete."
        else:
            return "Task not found."
    
    def delete_task(self, task_name):
        if task_name in self.tasks:  # If task name is in the list
            index = self.tasks.index(task_name)  # Get the index of the task
            del self.tasks[index]  # Delete task
            del self.completed[index]  # Delete its completion status
            self.save_tasks()  # Save tasks after deletion
            return f"'{task_name}' has been deleted."
        else:
            return "Task not found."


class open_file():
    def __init__(self, file_path, file_name):
        self.path = file_path + file_name + ".txt"
        
    def create_file(self):
        try:
            with open(self.path, 'x') as text_file:
                text_file.write("") # content
            print(f"\n{self.path} \n Created Sucessfully\n")
        except FileExistsError:
            print("\n{self.path} ]n Already Exists\n")
        
    def read(self): # Just Read file
        try:
            with open(self.path, 'r') as text_file:
                content = text_file.read()
                return content
        except FileNotFoundError:
            return "File not found."


# ----------------------- GUI Integration with Tkinter ------------------------

# User input for file path and name
file_path = "C:/Users/alexa/OneDrive/Documents/Text Files/"
file_name = str(input('Enter File Name: '))
task_manager = TaskManager(file_path, file_name)
my_file = open_file(file_path, file_name)

# Setup for Popup
root = tk.Tk()
root.title(f"{file_name} Task Manager")
root.geometry("500x400")

# Create a Text widget to display task file content
text_box = tk.Text(root, wrap="word", width=60, height=15)
text_box.pack(pady=10)

# Function to update the Textbox with the task list
def update_textbox():
    task_list = task_manager.view_tasks()
    text_box.delete("1.0", tk.END)  # Clear previous content
    text_box.insert(tk.END, task_list)  # Display file content

# Button to add a task
def add_task_button():
    task = entry.get()  # Get task from the entry widget
    if task:
        task_manager.add_task(task)
        entry.delete(0, tk.END)  # Clear the entry widget
        update_textbox()  # Update the task list in the text box
        print(f"'{task}' added.\n")

# Button to complete a task
def complete_task_button():
    task_name = entry.get()  # Get task name from entry widget
    if task_name:
        result = task_manager.complete_task(task_name)
        entry.delete(0, tk.END)  # Clear the entry widget
        update_textbox()  # Update the task list in the text box
        print(result)

# Button to delete a task
def delete_task_button():
    task_name = entry.get()  # Get task name from entry widget
    if task_name:
        result = task_manager.delete_task(task_name)
        entry.delete(0, tk.END)  # Clear the entry widget
        update_textbox()  # Update the task list in the text box
        print(result)

# Button to read file content
def read_file_button():
    content = my_file.read()
    text_box.delete("1.0", tk.END)  # Clear previous content
    text_box.insert(tk.END, content)  # Display file content

# Create GUI elements
entry = tk.Entry(root, width=60)
entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task_button)
add_button.pack(pady=5)

complete_button = tk.Button(root, text="Complete Task", command=complete_task_button)
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task_button)
delete_button.pack(pady=5)

read_button = tk.Button(root, text="Read File", command=read_file_button)
read_button.pack(pady=5)

# Initially display the tasks in the text box
update_textbox()

# Run the Tkinter event loop
root.mainloop()
