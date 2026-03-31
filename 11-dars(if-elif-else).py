# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:36:06 2026

@author: DELL
"""

#san = int(input("Jup san kiritin:"))
#if san % 2 == 0:
#    print("Raxmet")
#else:
#    print("Bul jup san emes")



#jas = int(input("Jasinizdi kiritin:"))
#if jas <= 4 or jas >= 60:
#    price = 0
#elif jas <= 18:
#    price = 10000
#else:
#    price = 20000
#print(f"Sizge kiriw {price} swm")    



#a = float(input("Birinshi sandi kiritin:"))
#b = float(input("Ekinshi sandi kiritin:"))
#if a > b:
#    print(f'{a} > {b}')
#elif a < b:
#    print(f'{a} < {b}')
#else:
#    print("Kiritilgen sanlar ten'")



#mahsulotlar = ['alma', 'juzim', 'erik', 'banan', 'shabdal', 'almurt', 'qareli', 'shiye', 'anar', 'ananas']
#savat = []
#for n in range(5):
#    savat.append(input(f' {n+1}-miyweni kiritin\':'))
#for onim in savat:
#    if onim in mahsulotlar:
#        print(f'Magazinimizde {onim} bar')
#    else:
#        print(f'Magazinimizde {onim} joq')



#mahsulotlar = ['alma', 'juzim', 'erik', 'banan', 'shabdal', 'almurt', 'qareli', 'shiye', 'anar', 'ananas']
#savat = []
#bor_mahsulotlar = []
#mavjud_emas = []
#for n in range(5):
#    savat.append(input(f' {n+1}-miyweni kiritin\':'))
#for onim in savat:
#    if onim in mahsulotlar:
#        bor_mahsulotlar.append(onim)
#    else:
#if mavjud_emas:
#    print('Tomendegi onimler magazinde joq:')
#    for onim in mavjud_emas:
#        print(onim)
#else:
#    print('Siz soragan barshe onimler bar')


#paydalaniwshilar = ['baxit', 'ali', 'aris', 'islam', 'nurik']
#login = input("Loginin'izdi kiritin':")
#if login.lower() in paydalaniwshilar:
#    print('Login band, yangi login kiritin')
#else:
#    print(f"Xosh kelipsiz, {login.title()}")


san = int(input("Qalegen putin san kiritin':"))
for n in range(2,11):
    if not (san % n):
        print(f'{san} sani {n} ge qaldiqsiz bolinedi')
