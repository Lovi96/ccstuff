def bubble_sort(lst):
    nums = lst
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    print(nums)
bubble_sort([3,9,17,13,2,16,7])