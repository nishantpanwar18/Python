def count_substring(string,sub_string):

    return (len([i for i in range(len(string)) if string[i:i+len(sub_string)]==sub_string]))

if __name__ == '__main__':
    string = 'ABCDCDC'
    sub_string = 'CDC'

    count = count_substring(string, sub_string)
    print(count)