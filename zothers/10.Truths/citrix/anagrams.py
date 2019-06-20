import os

def funWithAnagrams(s):
    # Write your code here
    i = 0
    a = len(s)
    while i < a:
        j = i + 1
        while j < a:
            Flag = False
            if sorted(s[i]) == sorted(s[j]):
                 s.remove(s[j])
                 Flag = True
            a = len(s)
            if Flag:
                j = i + 1
            else:
                j += 1
        i += 1
    s = sorted(s)
    return s


if __name__ == '__main__':
    s = ['poke', 'peok', 'poek', 'opek']
    result = funWithAnagrams(s)
    print(result)

