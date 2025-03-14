# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 12:11:08 2025

@author: alexa
"""

import tkinter as tk

root = tk.Tk()


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
        
    def read(self): #Just Read file
        with open(self.path, 'r') as text_file:
            content = text_file.read()
            print(content)
            text_box.delete("1.0", tk.END)  # Clear previous content
            text_box.insert(tk.END, content)  # Display file content
        
        
#Unfinished....

    def append_content(self, new_line):
        with open(self.path, 'r+') as text_file:
            text_file.write(new_line)
        # Connected to read_write function
            
            
    def read_write(self):   # Enable Read and Write
        with open(self.path, 'r') as text_file:
            line_count = len(text_file.readlines())
        with open(self.path, 'a') as text_file:
            for i in line_count:
                text_file.append()
        print("---------------")
        # Unfinished # add ammend instead of read

#------------------------

# User input for file path, etc.
file_path = "C:/Users/alexa/OneDrive/Documents/Text Files/"
file_name = str(input('Enter File Name: '))
my_file = open_file(file_path, file_name)


# Setup for Popup
root.title(f"{file_name} File")
root.geometry("500x400")

# Create a Text widget to display file content
text_box = tk.Text(root, wrap="word", width=60, height=20)
text_box.pack(pady=10)

# Create a Button to open the file
button1 = tk.Button(root, text="Read File", command=my_file.read)
button1.pack(pady=0)
button2 = tk.Button(root, text="Create File", command=my_file.create_file)
button2.pack(pady=0)



print("\n-----------------------\n")




#Run popup
root.mainloop()