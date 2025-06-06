def main():
    clues = [0, 1, 3, 50, 75]
    lower = 0
    upper = 99
    print(find_missing_clues(clues, lower, upper))

    clues = [-1]
    lower = -1
    upper = -1
    print(find_missing_clues(clues, lower, upper))

def find_missing_clues(clues, lower, upper):
    # sentinel clues
    clues = sorted(clues)
    sentinel_clues = [lower - 1] + clues + [upper + 1]
    res = []

    for i in range(len(sentinel_clues) - 1):
        start = sentinel_clues[i] + 1
        end = sentinel_clues[i + 1] - 1
        
        if start <= end:
            res.append([start, end])

    return res





    #print(sentinel_clues)
    

if __name__ == '__main__':
    main()