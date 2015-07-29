# description
#There is an array of integers. Please write a piece of code to find 3 elements whose sum is zero.

# basic idea:
# 1. firstly sort this array
# 2. Then choose a integer(x) from index 0 to the last
#     a. use two pointers (a,b) starting from both sides to the mid (except x)
#     b. add num[a],nums[b] and x together and compare to 0
#         if bigger b--
#         if smaller b++
#         if equal store this output
# 3. do something corner case to accerlate this procedure
def sum2zero(nums):
    nums.sort()
    res = []
    size = len(nums)
    path = []
    i = 0
    while i<size:
        a = i+1
        b = size-1
        while a<b:
            tmp = nums[a]+nums[b]+nums[i]
            if tmp == 0:
                path.append(nums[i])
                path.append(nums[a])
                path.append(nums[b])
                res.append(path)
                while a<b and path[1] == nums[a]:
                    a += 1
                while a<b and path[2] == nums[b]:
                    b -= 1
                path = []
            else:
                if tmp < 0:
                    a += 1
                else:
                    b -= 1
        while i + 1 < size and nums[i+1] == nums[i]:
            i += 1
        i += 1
    return res

nums = [1,0,-1,-1,-1,-1,0,1,1,1]
print nums
res = sum2zero(nums)
for item in res:
    print item
