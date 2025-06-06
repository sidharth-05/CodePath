def main():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(most_honey(height))

    height = [1, 1]
    print(most_honey(height))


def most_honey(height):
    left = 0
    right = len(height) - 1
    max_honey = 0

    while left < right:
        minimum_height = min(height[left], height[right])
        w = right - left

        max_honey = max(max_honey, minimum_height * w)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_honey


if __name__ == '__main__':
    main()

