def test(x):
    x.append(100)
    print("関数内:", x)

nums = [1, 2, 3]
print("関数外:", nums)
test(nums)

