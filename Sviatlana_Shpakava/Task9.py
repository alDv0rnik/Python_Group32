# Task 9
def foo(nums: list[int]) -> list[int]:
    prlist = []
    for i in range(len(nums)):
        pr = 1
        for j in range(len(nums)):
            if j != i:
                pr = pr * nums[j]
        prlist.append(pr)
    return prlist


print(foo([1, 2, 3, 4, 5]))
