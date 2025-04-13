# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 15:19:56 2025

@author: alexa
"""
import tkinter as tk


class open_file:
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
        
    def getPath(self):
        return self.path
        
class To_do:
    def __init__(self, open_file):
        self.path = open_file.getPath()
        self.tasks = []  # List to hold tasks
        self.completed = []  # List to hold completion status of tasks
        self.load_tasks()  # Load tasks from the file when initializing
        
    def load_tasks(self):
        with open(self.path, 'r') as text_file:
            for line in text_file:
                strip = ['-', 'Pending', 'Completed']
                linewords = line.split()
                for status in linewords:
                    if status == 'Pending':
                        self.completed.append(False)
                    elif status == 'Completed':
                        self.completed.append(True)
                resultwords = [word for word in linewords if word not in strip]
                newline = ' '.join(resultwords)
                self.tasks.append(newline)
        print(self.tasks)
        print(self.completed)
            
    def save_tasks(self):
        """Save tasks and their completion status to the text file."""
        with open(self.path, 'w') as text_file:
            for task, status in zip(self.tasks, self.completed):
                status_str = "Completed" if status else "Pending"
                text_file.write(f"{task} - {status_str}\n")
        print(f"Tasks saved to {self.path}\n")
            
    def add_task(self, task_name):
        self.tasks.append(task_name)  # Add task to list
        self.completed.append(False)  # Mark the task as incomplete
        self.save_tasks()  # Save tasks after adding
    
    def view_tasks(self):
        if not self.tasks:  # Check if there are any tasks
            return "No tasks to display."
        else:
            task_list = ""
            for i in range(len(self.tasks)):  # Loop over the list of tasks
                status = "Completed" if self.completed[i] else "Pending"
                task_list += self.tasks[i] + " -  " + status + "\n"
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
    
# ----------------------------------------

# Constructor Initializing

file_path = "C:/Users/alexa/OneDrive/Documents/Text Files/"
file_name = "New Text"
fefe = open_file(file_path, file_name)
exp = To_do(fefe)


#------------------

# Setup for GUI

root = tk.Tk()
root.title(f"{file_name} Task Manager")
root.geometry("500x400")

# Create a Text widget to display task file content
text_box = tk.Text(root, wrap="word", width=60, height=15)
text_box.pack(pady=10)

# Function to update the Textbox with the task list
def update_textbox():
    task_list = exp.view_tasks()
    text_box.delete("1.0", tk.END)  # Clear previous content
    text_box.insert(tk.END, task_list)  # Display file content

# Button to add a task
def add_task_button():
    task = entry.get()  # Get task from the entry widget
    if task:
        exp.add_task(task)
        entry.delete(0, tk.END)  # Clear the entry widget
        update_textbox()  # Update the task list in the text box
        print(f"'{task}' added.\n")

# Button to complete a task
def complete_task_button():
    task_name = entry.get()  # Get task name from entry widget
    if task_name:
        result = exp.complete_task(task_name)
        entry.delete(0, tk.END)  # Clear the entry widget
        update_textbox()  # Update the task list in the text box
        print(result)

# Button to delete a task
def delete_task_button():
    task_name = entry.get()  # Get task name from entry widget
    if task_name:
        result = exp.delete_task(task_name)
        entry.delete(0, tk.END)  # Clear the entry widget
        update_textbox()  # Update the task list in the text box
        print(result)

# Button to read file content
def read_file_button():
    content = open_file.read()
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

