# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 16:06:40 2026

@author: DELL
"""

#ismlar = ['Islam', 'Ruslan', 'Maxmud', 'Baxit', 'Sultan']
#for n in ismlar:
#    print(f"Qalay {n} jora, orazalar qabil bolsin")
#print(f"Kod {len(ismlar)} marte takirarlandi")

#toq_sonlar = list(range(11,100,2))
#sonlar_kubi = []
#for son in toq_sonlar:
#    sonlar_kubi.append(son**3)
#print('Taqsanlar:',toq_sonlar)
#print('Usi sanlardin kublari:', sonlar_kubi)

#kino = []
#print('5 en jaqsi korgen kinonizdi kiritin:')
#for n in range(5):
#    kino.append(input(f"{n+1}-kinoni kiritin:"))
#print(kino)


s = int(input('Bugin neshe adam menen sawbetlestiniz:'))
dizim = []
for k in range(s):
    dizim.append(input(f"{k+1}-sawbetlesken adaminizdin ati kim: "))
print(dizim)