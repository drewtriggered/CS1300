#append vs extend
a = [1,2,3]
b = [4,5,6]
a.append(b)
a.extend(b)
a.insert(3, 4)
print(a)