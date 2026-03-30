#append vs extend
a = [1,2,3]
b = [4,5,6]
a.append(b)
a.extend(b)
a.insert(3, 4)
print(a)

numbers = [2, 7, 3, 8, 5]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == 10:
            print(f"{numbers[i]}, {numbers[j]}")
            
for i in range (4):
    for j in range (4):
        print(i * 4 + j + 1, end = " ")
        
  