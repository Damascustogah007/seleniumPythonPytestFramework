#Numbers - Integer, Float, ComlplexNumber
print('###Interger###')
a = 10
print(a)
print(type(a))

print('###Float###')
b = 2.5
print(b)
print(type(b))

print('###ComplexNumbers###')
c = 12 + 3j
print(c)
print(type(c))

print('###Dictionary###')

dic = {
    1 : "Hello",
    2 : "Welcome"
}

print(dic.get(1))
print(dic[2])

print('###Boolean###')
x = True
y = False
print(x)
print(y)

print('###Set###')
s = {1,2,3,4,5,5,4,3}
print(s)

print('###String###')
#methods (len, lower, upper, concat(+), find, replace, split, join)

str1 = "This is the first code"
str2 = "This is the second code"
str3 = "This is the third code"

print(str1)
print(len(str1))
print(str1.lower())
print(str1.upper())
print(str1+str2)
print(str1.find("f"))
print(str1.replace('o', 'e'))
print(' '.join(str1))
print(str1.split()) #Convert string to array

print('###String###')
#methods (len, append, insert, index, remove, sort, reverse, pop, slice [starting : ending], extend)
lst1 = [1,2,3,4,5,6]
print(len(lst1))
lst1.append(2)
print(lst1)
lst1.insert(0, 0)
print(lst1)
lst1.remove(5)
print(lst1)
lst1.sort()
print(lst1)
lst1.reverse()
print(lst1)
lst1.pop()
print(lst1)
print(lst1[0 : 3])
lst1.extend([7,8,9])
print(lst1)
print(lst1.index(9))


print('###Tuple###')

tup = (1,2,3,4,5)
print(tup)