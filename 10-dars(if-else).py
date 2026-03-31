# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 10:32:54 2026

@author: DELL
"""

#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in cars:
#    if car == 'gm':
#        print(car.upper())
#    else:
#        print(car.title())
        
        
#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in cars:
#    if car != 'gm':
#        print(car.title())
#    else:
#        print(car.upper())



#login = (input('Loginingizni kiriting:\n'))
#if login.lower() == 'admin':
#    print('Xush kelibsiz, Admin.\nFoydalanuvchilar royxatini korasizmi?')
#else:
#    print(f"Xush kelibsiz {login.title()}!")
    



#x = float(input("Eki san kiritin'\nBirinshi san:"))
#y = float(input("Ekinshi san:"))
#if x == y:
#    print(f"Sanlar ten' {x} = {y}")



#son = float(input("Qalegen san kiritin':"))
#print("Son manfiy") if son<0 else print("Son musbat")


son = float(input("Qalegen san kiritin':"))
if son > 0:
    print(f"Bul sannin' koreni:{son**(1/2)}")
else:
    print("On' san kiritin'")
    