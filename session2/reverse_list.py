def main():
    lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
    print(reverse_list(lst))

def reverse_list(lst):
    beginning = 0
    last = len(lst) - 1
    result = []

    while last >= beginning:
        result.append(lst[last])
        last -= 1

    return result

if __name__ == '__main__':
    main()
