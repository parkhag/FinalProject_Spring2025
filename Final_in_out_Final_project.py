# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 12:11:08 2025

@author: alexa
"""



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
            print(text_file.read())
        print("------------------")
        
        
        
        
        
        

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


    
        


        
     
file_path = "C:/Users/alexa/OneDrive/Documents/Text Files/"
file_name = str(input('Enter File Name: '))


# unused
path_2 = file_name + "/" + file_name + ".txt"



print("\n-----------------------\n")
my_file = open_file(file_path, file_name)
my_file.read()

#-----------Creation of files
