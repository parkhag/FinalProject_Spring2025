# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:18:17 2025

@author: hayeg
"""

Task1=input("*   ")

Choice=input("Are you going to add(a), view(v), complete(c), or delete(d)?  ")

if Choice=='a':
    Task1=input("*   ")

if Choice=='v':
    print(Task1)
    
if Choice=='c':
    print(Task1, "is completed")
    
if Choice == 'd':
    print(Task1, "is deleted")