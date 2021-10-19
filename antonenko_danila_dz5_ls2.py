n = int(input('Введите ваше число: '))
odd_nums_gen = (num for num in range(1, n+1, 2))

print(list(odd_nums_gen))