a = int(input('Adj meg egy számot '))
b = int(input('Adj meg egy számot '))
c = int(input('Adj meg egy számot '))
x = min ( a,b,c)
print('A legkisebb',x)

a = int(input('Adj meg egy számot '))
b = int(input('Adj meg egy számot '))
c = int(input('Adj meg egy számot '))
y = max ( a,b,c)
print('A legnagyobb',y)

x = int(input('A pontszámod '))
if x<50:
    print('1')
elif 50<=x<60:
    print('2')
elif  60<=x<70:
    print('3')
elif 70<=x<85:
    print('4')
elif x>=85:
    print('5')



