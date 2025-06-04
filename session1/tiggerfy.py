def main():
    word = "Trigger"
    print(tiggerfy(word))

    word = "eggplant"
    print(tiggerfy(word))

    word = "Choir"
    print(tiggerfy(word))


def tiggerfy(word):
    res = ""
    i = 0
    while i < len(word):
        if word[i] == 't' or word[i] == 'i':
            i += 1
        elif word[i] == 'g' and i + 1 < len(word) and word[i + 1] == 'g':
            i += 2
        elif word[i] == 'e' and i + 1 < len(word) and word[i + 1] == 'r':
            i += 2
        else:
            res += word[i]
            i += 1
    return res

        


if __name__ == "__main__":
    main()