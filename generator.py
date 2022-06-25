def numbers(start=1, end=10):
    while start <= end:
        yield start
        start += 1


nums = numbers(10, 13)
print(nums)
print(next(nums))
print(next(nums))