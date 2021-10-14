def odd_nums(n):
    for num in range(1, n+1, 2):
        yield num


odd_to_15 = odd_nums(10)
print(list(odd_to_15))