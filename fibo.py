array = [0, 1]
for i in range(1, 11):
    array.append(array[i-1] + array[i])
print array

