def palindrom(text):
    j1, j2, j = 0, 0, 0
    for i, t in enumerate(text):
        i1, i2 = 0, 0

        while not text[i + i1 + j1].isalpha():
            i1 += 1

        while not text[-i - 1 - i2 - j2].isalpha():
            i2 += 1

        j1 += i1
        j2 += i2

        i3 = j1 + j2

        if text[i + j1].lower() == text[-i - 1 - j2].lower():
            j += 1

        if i >= len(text) - i3 / 2:
            break

    print(j, i)
    if j == len(text) / 2 or j == len(text) / 2 + 1:
        return True
    return False
