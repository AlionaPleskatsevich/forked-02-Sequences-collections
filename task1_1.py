#Дан список целых чисел. Найти второе по величине число в списке.
numbers = [15, 7, 28, 10, 21]
numbers.sort() 
max_num = numbers[-1]
for num in range(len(numbers)-1,-1,-1):
    if numbers[num] < max_num:
        second_max_num = numbers[num]
        break
print(second_max_num)