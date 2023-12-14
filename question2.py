def compress_string(s):
    cnt = 1
    res = ""
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            cnt +=1 
        else: 
            res += s[i-1]
            res += str(cnt)
            cnt = 1 
    res += s[-1]
    res += str(cnt)
    return res

s = input()
print(compress_string(s))
