# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def Three_Numbers():
    number1=eval(input("Please enter three different numbers\nPlease enter your first number: "))
    number2=eval(input("Please enter your second number: "))
    number3=eval(input("Please enter your third number: "))
    
    #order for 1 highest
    if number1>number2 and number1>number3:
        number_Highest=number1
        if number2>number3:#number 2 is middle
            number_Middle=number2
            number_Low=number3
        else:
            number_Middle=number3#number 3 is middle
            number_Low=number2
            
    #order for 2 highest
    elif number2>number1 and number2>number3:
        number_Highest=number2
        if number1>number3:#number 1 is middle
            number_Middle=number1
            number_Low=number3
        else:                       #number 3 is middle
            number_Middle=number3
            number_Low=number1
            
    #order for 3 highest
    elif number3>number2 and number3>number1:
        number_Highest=number3
        if number2>number1:#number 2 is middle
            number_Middle=number2
            number_Low=number1
        else:
            number_Middle=number1#number 1 is middle
            number_Low=number2
    #print the order
    print("Your order is ", number_Highest,"(Highest), ",number_Middle,",and ",number_Low,"(Lowest).", sep="")
    


def Check_Pass():
    #input the password
    User_Pass=input("Please Enter a Password: ")
    print("Your Password is:", User_Pass)
    
    Pass_OK=len(User_Pass) >=8
    Has_digit=False
    Has_upper=False
    
    #For loop to check individual character in string
    for char in User_Pass:
        #Must have numbers
        if char.isdigit():
            Has_digit=True
            
        #Must be uppercase
        if char.isupper():
            Has_upper=True
    
    #Must be at least 8 characters long
    if Pass_OK and Has_digit and Has_upper:
        print("Your Password is valid")
    else:
         print("Your Password is not valid\nPlease enter a valid password")



def items_cost():
    print("Please enter the cost for your three items:")
    item1=eval(input("First item: "))
    item2=eval(input("Second item: "))
    item3=eval(input("Third item: "))
    
    #get the total
    total=item1+item2+item3
    #apply 10% discount if total is over 100
    if total>100:
        total=total*0.9
        
    print("Your total is:",total,)



def main():
    print("Question 1:")
    Three_Numbers()
    print("Question 2:")
    Check_Pass()
    print("Question 3:")
    items_cost()
    

    
#Invoke the main function
if __name__=="__main__":
    main()