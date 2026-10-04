numbers = [4, 6, 2, 11, 1, 11, 5]
numbers.sort() 
second_max_num = 0
max_num = numbers[-1]
for num in numbers[::-1]:
    if num != max_num:
        second_max_num = num
        break
print(second_max_num)