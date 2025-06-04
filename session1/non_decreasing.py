def main():
    nums = [4, 2, 3]
    print(non_decreasing(nums))

    nums = [4, 2, 1]
    print(non_decreasing(nums))

def non_decreasing(nums):
    count = 0

    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            count += 1
            if count > 1: 
                return False
            
            if i == 0 or nums[i - 1] <= nums[i + 1]:
                nums[i] = nums[i + 1]
            else:
                nums[i + 1] = nums[i]

    return True

if __name__ == "__main__":
    main()