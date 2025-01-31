# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:18:17 2025

@author: hayeg
"""

Tasks=[] #initialize to hold tasks as lists
Completed=[] #initialize to hold completed status as lists

def addTask():
    Task=input("Your task: ")#input the task from user
    Tasks.append(Task)#Add Task to list
    Completed.append(False) #Mark the task as incomplete
    print(f"\n'{Task}' added.\n")
    
    
def viewTask():
    for i in range(len(Tasks)):#go over the length of the list
        if Completed[i]: #if task completed
            status = "Completed"#set status to completed
        else:#not completed
            status = "Pending"#print as pending
        print(f"\n{Tasks[i]} - {status}")
    print("\n")  # line break
    
    
def completeTask():
    viewTask()#reprint the current tasks
    TaskName = input("Enter the task name to mark as completed: ")
        # Get task name as input
    for i in range(len(Tasks)):  # Loop through the list
        if Tasks[i] == TaskName:  #if TaskName with name in list
            Completed[i] = True  #Switch from pending to completed
            print(f"\n'{TaskName}' is now complete.")
            break  # Exit the loop
    else:
        print("Invalid")#invalid when name not in list
    print("\n")  # Line break
    

def deleteTask():
    viewTask()#reprint the current task
    TaskName = input("\nEnter the task number to delete: ")
    #Get task name as input
    for i in range(len(Tasks)):  # Loop through the list
        if Tasks[i]==TaskName:# if Taskname with name in list
            del Tasks[i]#delete task
            del Completed[i]#delete completed/pending
            print(f"\n'{TaskName}' is deleted.\n")
            break#break out of loop
    else:#No correct input
        print("Invalid")




def main():
    
    Choice=''#initialize Choice as character-input
    
    while Choice != "end":
        Choice=input("Are you going to add(a), view(v), complete(c), or delete(d)? \n(end) to stop\n")
        #ask user, input choice
        if Choice == 'a':#if choice is add
            addTask()
            
        elif Choice == 'v':#if choice is view
            viewTask()
            
        elif Choice == 'c':#if choice is complete
            completeTask()
            
        elif Choice == 'd':#if choice is delete
            deleteTask()
            
        elif Choice == 'end':#if choice is end
            print("Ending the program")
            break#out of the loop
        
        else:#None of the above
            print("Invalid choice, please try again.")
        
        
#Invoke the main function
if __name__=="__main__":
    main()