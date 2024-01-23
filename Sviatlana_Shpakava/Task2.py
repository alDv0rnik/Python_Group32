def odd_numbers(nums: int):
    for n in nums:
        if n % 2 != 0:
            yield n

o_nums = odd_numbers(range(1, 100))
print(list(o_nums))
print(next(o_nums))
print(next(o_nums))
print(next(o_nums))
