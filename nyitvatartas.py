óra = int(input('Hány óra van most? '))
if (16>óra>8):
    print('A bolt nyitva van ')
    print('Még ennyi ideig van nyitva ',16-óra)
else:  
    print('A bolt zárva ')
    if óra>8:
        print('Ennyi idő múlva nyit ki a bolt: ',32-óra)
    else:
         print('Ennyi idő múlva nyit ki a bolt: ',8-óra)
        

