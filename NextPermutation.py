def nextPermutation(nums):
    n=len(nums)

    for i in range(n-1,0,-1):
        if nums[i]>nums[i-1]:
            nums[i:]=sorted(nums[i:])
            for j in range(i,n):
                if nums[j]>nums[i-1]:
                    nums[j],nums[i-1]=nums[i-1],nums[j]
                    print(*nums)
                    return
    else:
        nums.sort()
        print(*nums)
print("Enter array elements with space")
nums=list(map(int,input().split()))
nextPermutation(nums)