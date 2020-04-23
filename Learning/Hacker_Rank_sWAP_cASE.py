new_string = []
def swap_case(s):
    for c in s:
        if c.isupper():
            new_string.append(c.lower())
        else:
            new_string.append(c.upper())
    return "".join(new_string)


if __name__ == '__main__':
    print(swap_case(input()))
