def insertion(nums):

    for i in range(1,len(nums)):
        val = nums[i]
        hole = i

        while(hole>0 and val<nums[hole-1]):
            nums[hole] = nums[hole-1]
            hole -= 1
        nums[hole] = val

    return nums

nums = [8,7,6,5,4,3]
print(insertion(nums))
        