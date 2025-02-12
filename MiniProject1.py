# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 13:10:05 2025

@author: hayeg
"""

def ListCourses():
    print("EECE2140(a)")
    print("EECE2150(b)")
    print("EECE2160(c)")
    print("EECE2170(d)")
    print("EECE2180(e)")
    print("EECE2190(f)")
    print("EECE2200(g)\n\n")

def ViewRegisteredCourses(Selected_Courses):
    if not Selected_Courses:
        print("\nYou have not registered for any courses yet.\n")
    else:
        print("\nYou have registered for the following courses:")
        for course in Selected_Courses:
            print(course)
        print()

def SelectCourses():
    ListCourses()
    Selected_Courses = []
    i = 0
    
    while(i < 3):
        UserInput = input("Choose a,b,c,d,e,f,g respectively to pick course.\n 'r' to view registered courses or 'exit' to exit: \n")
        
        if UserInput == 'a':
            for k in range(len(Selected_Courses)):
                if Selected_Courses[k] == "EECE2140":
                    print("You have chosen this course already. Please pick again\n")
                    break
            else:
                i += 1
                Selected_Courses.append("EECE2140")
                print("You have chosen EECE2140\n")
        
        elif UserInput == 'b':
            for k in range(len(Selected_Courses)):
                if Selected_Courses[k] == "EECE2150":
                    print("You have chosen this course already. Please pick again\n")
                    break
            else:
                i += 1
                Selected_Courses.append("EECE2150")
                print("You have chosen EECE2150\n")
        
        elif UserInput == 'c':
            for k in range(len(Selected_Courses)):
                if Selected_Courses[k] == "EECE2160":
                    print("You have chosen this course already. Please pick again\n")
                    break
            else:
                i += 1
                Selected_Courses.append("EECE2160")
                print("You have chosen EECE2160\n")
        
        elif UserInput == 'd':
            for k in range(len(Selected_Courses)):
                if Selected_Courses[k] == "EECE2170":
                    print("You have chosen this course already. Please pick again\n")
                    break
            else:
                i += 1
                Selected_Courses.append("EECE2170")
                print("You have chosen EECE2170\n")
        
        elif UserInput == 'e':
            for k in range(len(Selected_Courses)):
                if Selected_Courses[k] == "EECE2180":
                    print("You have chosen this course already. Please pick again\n")
                    break
            else:
                i += 1
                Selected_Courses.append("EECE2180")
                print("You have chosen EECE2180\n")
        
        elif UserInput == 'f':
            for k in range(len(Selected_Courses)):
                if Selected_Courses[k] == "EECE2190":
                    print("You have chosen this course already. Please pick again\n")
                    break
            else:
                i += 1
                Selected_Courses.append("EECE2190")
                print("You have chosen EECE2190\n")
        
        elif UserInput == 'g':
            for k in range(len(Selected_Courses)):
                if Selected_Courses[k] == "EECE2200":
                    print("You have chosen this course already. Please pick again\n")
                    break
            else:
                i += 1
                Selected_Courses.append("EECE2200")
                print("You have chosen EECE2200\n")
        
        elif UserInput == 'r':
            ViewRegisteredCourses(Selected_Courses)
        
        elif UserInput == 'exit':
            print("Exiting the Code\n")
            break
        
        else:
            print("Please enter a valid input\n")


def main():  # Main Function
    SelectCourses()

# Invoke the main function
if __name__ == "__main__":
    main()
