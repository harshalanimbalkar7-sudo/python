from bisect import bisect_left

def lengthOfLIS(nums):
    lis = []

    for num in nums:
        pos = bisect_left(lis, num)

        if pos == len(lis):
            lis.append(num)
        else:
            lis[pos] = num

    return len(lis)

nums = list(map(int, input("Enter numbers: ").split()))
print("Length of LIS:", lengthOfLIS(nums))