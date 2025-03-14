# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 12:48:08 2025

@author: hayeg
"""
class TaskManager:
    def __init__(self):
        self.tasks = []  # List to hold tasks
        self.completed = []  # List to hold completion status of tasks
    
    def add_task(self):
        task = input("Your task: ")  # Input the task from user
        self.tasks.append(task)  # Add task to list
        self.completed.append(False)  # Mark the task as incomplete
        print(f"\n'{task}' added.\n")
    
    def view_tasks(self):
        if not self.tasks:  # Check if there are any tasks
            print("No tasks to display.\n")
        else:
            for i in range(len(self.tasks)):  # Loop over the list of tasks
                status = "Completed" if self.completed[i] else "Pending"
                print(f"\n{self.tasks[i]} - {status}")
            print("\n")  # Line break
    
    def complete_task(self):
        self.view_tasks()  # Reprint the current tasks
        task_name = input("Enter the task name to mark as completed: ")
        
        if task_name in self.tasks:  # If task name is in the list
            index = self.tasks.index(task_name)  # Get the index of the task
            self.completed[index] = True  # Mark it as completed
            print(f"\n'{task_name}' is now complete.\n")
        else:
            print("Task not found.\n")
    
    def delete_task(self):
        self.view_tasks()  # Reprint the current tasks
        task_name = input("\nEnter the task name to delete: ")
        
        if task_name in self.tasks:  # If task name is in the list
            index = self.tasks.index(task_name)  # Get the index of the task
            del self.tasks[index]  # Delete task
            del self.completed[index]  # Delete its completion status
            print(f"\n'{task_name}' has been deleted.\n")
        else:
            print("Task not found.\n")
    
    def MainEditingSpace(self):
        choice = ''
        while choice != "end":
            choice = input("Are you going to add(a), view(v), complete(c), or delete(d)? \nType 'end' to stop: ")
            if choice == 'a':  # If choice is add
                self.add_task()
            elif choice == 'v':  # If choice is view
                self.view_tasks()
            elif choice == 'c':  # If choice is complete
                self.complete_task()
            elif choice == 'd':  # If choice is delete
                self.delete_task()
            elif choice == 'end':  # If choice is end
                print("Ending the program")
                break  # Exit the loop
            else:  # Invalid input
                print("Invalid choice, please try again.")
        

if __name__ == "__main__":
    task_manager = TaskManager()  # Create an instance of TaskManager
    task_manager.MainEditingSpace()  # Run the main function
