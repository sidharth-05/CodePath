def main():
    items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
    target = 'hunny'
    print(linear_search(items, target))  # should print 3

    items = ['bed', 'blue jacket', 'red shirt', 'hunny']
    target = 'red balloon'
    print(linear_search(items, target))

def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return None

if __name__ == "__main__":
    main()  

