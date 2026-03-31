# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 15:01:52 2026

@author: DELL
"""

#Davlatlar = ["Kanada", "Mexiko", "AQSH"]
#print(Davlatlar)
#print('Elementler sani:', len(Davlatlar))

#print("Taqlangan royxat:", sorted(Davlatlar))

#print("Teskari royxat",sorted(Davlatlar,reverse=True))

#print("Asl royxat:", Davlatlar)

#Davlatlar.reverse()
#print(Davlatlar)

#Davlatlar.sort()
#print("alfavit boyinsh taqlansa:",Davlatlar)

#Davlatlar.sort(reverse=True)
#print("alfavittin aqirinan baslap taqlansa:",Davlatlar)

#120dan 1200 ge shekemgi jup sanlardi shigariw
#sanlar = list(range(120,1200,2))
#print(sum(sanlar))
#print(max(sanlar)-min(sanlar))

#E_sani = len(sanlar)
#print("Elementler sani:",E_sani)

#print(sanlar[:20])
#print(sanlar[-20:])
#print(sanlar[530:550])


taomlar = ["Manti", "Palaw", "Teftel", "Golubci", "Bifshteks"]
#print(taomlar)

nonushta = taomlar[:]
nonushta.remove('Manti')
nonushta.remove('Palaw')
nonushta.remove('Bifshteks')
nonushta.append('tuxum')
nonushta.append('sosiska')
print("Taomlar:",taomlar)
print("nonushta:",nonushta)

nonushta = tuple(nonushta)
nonushta[0] = "qaymoq va non"