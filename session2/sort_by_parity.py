def main():
    nums = [3, 1, 2, 4]
    print(sort_by_parity(nums))

    nums = [0]
    print(sort_by_parity(nums))

def sort_by_parity(nums):
    """
    evens = []
    odds = []

    for num in nums:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    return evens + odds
    """

    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] % 2 > nums[right] % 2:
            nums[left], nums[right] = nums[right], nums[left]
        
        if nums[left] % 2 == 0:
            left += 1
        if nums[right] % 2 == 1:
            right -= 1
    
    return nums




if __name__ == '__main__':
    main()