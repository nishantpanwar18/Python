from functools import reduce

if __name__ == '__main__':
    score_list = []
    mark_sheet = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        mark_sheet.append([name, score])
        score_list.append(score)
mark_sheet.sort()
score_set = set(score_list)
sec  = sorted(score_set,reverse=False)[1]

for n, m in (mark_sheet):
    if m == sec:
        print(n)
    else:
        continue



