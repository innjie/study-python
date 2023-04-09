# k번째 큰 수

numbers = [25, 25, 23, 23, 22, 20, 19]
numbers_set = ()

numbers_set = set(numbers)
reversed_numbers = list(numbers_set)
reversed_numbers.sort(reverse = True)

result = 0
for i in range (0, 3):
    result += reversed_numbers[i]

print(result)