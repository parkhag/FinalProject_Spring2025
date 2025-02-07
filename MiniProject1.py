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
    print("EECE2200(g)")
    
def SelectCourses():
    ListCourses()
    
    i=0
    
    while(i<3):
        UserInput=input("Choose a,b,c,d,e,or f respectively to pick course: ")
        if UserInput=='a':
            i +=1
        elif UserInput == 'b':
            i +=1
        elif UserInput == 'c':
            i +=1
        elif UserInput == 'd':
            i +=1
        elif UserInput == 'e':
            i +=1
        elif UserInput == 'f':
            i +=1
        elif UserInput == 'g':
            i +=1
            




def main():#Main Function
    SelectCourses()
    



#Invoke the main function
if __name__=="__main__":
    main()