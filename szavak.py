szo = input('Adj meg egy szót  ')
masikszo = input('Adj meg egy másik szót ')
szo_hossza = len (szo)
masikszo_hossza= len (masikszo)
if szo_hossza>masikszo_hossza:
    print('A hosszabb szó '+szo)
elif szo_hossza==masikszo_hossza:
    print('A két szó ugyan olyan hosszú ')
else: 
    print('A hosszabb szó ',masikszo)

