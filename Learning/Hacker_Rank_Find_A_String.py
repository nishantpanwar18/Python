def count_substring(string, sub_string):
    cnt = 0
    for st in range(len(string)):
        for sub_st in sub_string:
            if sub_st == st:
                continue
            else:
                
                cnt+=1


        if sub_string:
                cnt+=1
    return
