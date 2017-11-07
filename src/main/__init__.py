from idlelib.idle_test.test_history import line2
print('helloworld')
print('The quick brown fox', 'jumps over'+'the lazy dog')
#name = input()
#print(name)
#address = input('please input your address: ')
#print(address)
print('''line1
line2
line3''')
age = 12
if age >= 18:
    print('adult')
else:
    print('teenager')

print(ord('A'))
print(chr(65))

l = ['python', 'java', ['asp', 'php'], 'scheme']

print(l)
print(l[2][1])

t = ('hello',('ha','he'),'fuck')

print(t)
print(t[1][1])

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
    
d = {'ha':'haha','he':'hehe'}
print(d)
print(d['ha'])

def getLast(x):
    temp = ''
    for index in x:
        temp = index
    return temp

print(getLast(d))

s = [('a','b','c')]
print(s)

from sample import getAbs

print (getAbs(-1))

print("test again")






    
    