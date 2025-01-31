# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 12:06:53 2025

@author: hayeg
"""
import random



def Subtrac_Num():
    number1=random.randint(0, 9)
    number2=random.randint(0, 9)
    
    if number1<number2:
        number1,number2=number2,number1
        
    print("My numbers are ", number1," and ", number2,".", sep="")   
    
    
    Answer = eval(input("What is the answer of " + str(number1) + "-" + str(number2) +". "))
    
while(Answer != number1-number2):
    if number1 - number2 == Answer:
        print("Your answer is correct!")
        
    else:
        print("Your answer is incorrect.")
        Answer = eval(input("What is the answer of " + str(number1) + "-" + str(number2) +". "))
        
    

    
def main():
    Subtrac_Num()
    
#Invoke the main function
if __name__=="__main__":
    main()