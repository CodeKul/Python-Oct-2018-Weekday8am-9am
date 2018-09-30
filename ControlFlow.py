'''
if 

if 
else


if 
elif
'''

a = 10
b = 20

# if a < b:
#     print('a is less than b')

# if a > b:
#     print('a is greater than b')
# else:
#     print('b is greater than a')

# print('a == 10')

if a == 20:
    print('a == 20')
elif b == 20:
    print('a != 20 and b == 20')
else:
    pass


'''
Loops

while
for
'''

a = 0
while a < 10:
    print('value: %d'%a)
    a += 1


for item in "Codekul":
    print(item)

list1 = [1,2,3,4,5,6,7,8,9, 'Vaibhav']

for (index,num) in enumerate(list1):
    print('Index: {}\nData: {}\n'.format(index, num))

for num in list1:
    print(num)

t1 = (1,2,3,4,5)
for t in t1:
    print(t)