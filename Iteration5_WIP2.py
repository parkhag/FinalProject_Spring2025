# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 01:04:19 2025

@author: hayeg
"""

import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, file_path, file_name):
        self.file_path = file_path + file_name + ".txt"
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
            print(f"No existing task file found. Creating new one.")
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
file_path = "C:/Users/hayeg/Desktop/Northeastern!!/Classes"  # Default path to current directory
file_name = "New Text"  # Default file name
task_manager = TaskManager(file_path, file_name)  # Corrected initialization

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

def read_file_button():
    update_textbox()
    status_label.config(text="File content reloaded.", fg="black")

# ----------------------- GUI Integration with Tkinter ------------------------

root = tk.Tk()
root.title("Task Manager")
root.geometry("500x650")

# Removed file path entry and load button
text_box = tk.Text(root, wrap="word", width=60, height=15, state=tk.DISABLED)
text_box.pack(pady=10)

status_label = tk.Label(root, text="", fg="red")
status_label.pack(pady=5)

entry = tk.Entry(root, width=60)
entry.pack(pady=5)

list_box = tk.Listbox(root, height=5, width=60)
list_box.pack(pady=5)

read_btn = tk.Button(root, text="Read File", command=read_file_button)
read_btn.pack(pady=5)

add_task_btn = tk.Button(root, text="Add Task", command=add_task_button)
add_task_btn.pack(pady=5)

delete_task_btn = tk.Button(root, text="Delete Task", command=delete_task_button)
delete_task_btn.pack(pady=5)

complete_task_btn = tk.Button(root, text="Complete Task", command=complete_task_button)
complete_task_btn.pack(pady=5)

add_note_btn = tk.Button(root, text="Add Note", command=add_note_button)
add_note_btn.pack(pady=5)

edit_note_btn = tk.Button(root, text="Edit Note", command=edit_note_button)
edit_note_btn.pack(pady=5)

# Call update_textbox to load data when the program starts
update_textbox()

root.mainloop()
