def main():
    items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
    print(remove_dupes(items))

    items = ["extract of malt", "haycorns", "honey", "thistle"]
    print(remove_dupes(items))

    """
    unique_list = items
    for i in range(len(items)):
        is_duplicate = False
        for j in range(len(unique_list)):
            if items[i] == unique_list[j]:
                is_duplicate = True
                break
            if not is_duplicate:
                unique_list.append(items[i])
    """

def remove_dupes(items):
    if not items:
        return 0

    write_index = 1  # Where the next unique item should go

    for read_index in range(1, len(items)):
        if items[read_index] != items[write_index - 1]:
            items[write_index] = items[read_index]
            write_index += 1

    return write_index

    




    





if __name__ == '__main__':
    main()