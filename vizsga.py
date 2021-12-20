nap = (input('Jó napja van? '))
x = 'nem'
y = 'igen'
if nap == y :
    print('Az nagyszerű! ')
elif nap == x:
    print('Az nem jó! ')
else:
    print('Sajnos nem értem a válaszod! ')

szam = int(input('Adjon meg egy számot! '))
if szam%2:
    print('A szám páratlan')
else:
    print('A szám páros')
a = input('Nyomjon egy entert! ')

print('Gondoltam egy számra 1 és 5 között! ')
for i in range(1,6):
    print(i)
gondolt_szam = 3
tipp = int(input('Kérem adjon meg egy számot! '))
if gondolt_szam == tipp:
    print('A válszod helyes! ')
    print('Ügyes vagy! ')
elif gondolt_szam > tipp:
    print('A gonsdolt szám nagyobb! ')
    print('De majd legközelebb sikerülni fog! ')
else:
    print('A gondolt szám kisebb')
    print('Majd legközelebb sikerülni fog! ')