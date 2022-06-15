def insertionSort(nums):
    i = 0
    while i<len(nums)-1:
        j = i+1

        while j>0:
            if nums[j]<nums[j-1]:
                nums[j],nums[j-1] = nums[j-1], nums[j]
                j-=1
            else:
                break
        i+=1
    return nums

def selectionSort(nums):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j]:
                nums[i],nums[j] = nums[j],nums[i]

def bubbleSort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

nums = [2,1,12,4,112,88]
bubbleSort(nums)
print(nums)


