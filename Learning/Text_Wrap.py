import textwrap

def wrap(string, max_width):
    a = 0
    b = max_width
    while a < len(string):
        print(string[a:b])
        a = b
        b = a + max_width
    return string[a:b]

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)