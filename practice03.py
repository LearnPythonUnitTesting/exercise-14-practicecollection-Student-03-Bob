def get_score(string):
    if len(string) != 10:
        return 0
    l = list(string)
    score = 0
    for s in l:
        if s.isdigit():
            score += 1
        elif s.isalpha():
            score += 5
        else:
            score += 10
    return score

# print(get_score())
# print(get_score())
# print(get_score())


