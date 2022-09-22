# In this kata you have to create all permutations of a non empty input string and remove duplicates, if present.
#     This means, you have to shuffle all letters from the input in all possible orders.
def permutations(s):
    result = {s}
    if len(s) == 2:
        result.add(s[1] + s[0])
    elif len(s) > 2:
        for i, n in enumerate(s):
            for l in permutations(s[:i] + s[i + 1:]):
                result.add(n + l)
    return sorted(result)


print(permutations('12345678'))
