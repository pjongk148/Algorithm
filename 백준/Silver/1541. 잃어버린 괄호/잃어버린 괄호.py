arr = input().split("-")
nums = []
for i in arr:
    tmp = sum(map(int,i.split("+")))
    nums.append(tmp)
print(nums[0] - sum(nums[1:]))