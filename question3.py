# def reverseInGroups( s,K):
#     # code here
#     if K > 1:
#         cnt = 0 
#         start = 0
#         res = ""
#         for i in range(len(s)):
#             if cnt != K:
#                 cnt += 1
#             if cnt == K:
#                 res  += s[start:i:-1][::-1]
#                 start = i + 1
#                 cnt = 0
#         res +=  s[start:len(s)-1][::-1]
#         print(res)
#         return res
#     return s

# s = input()
# k = int(input())
# ans = reverseInGroups(s,k)
# print(ans)

def reverse_groups(s, K):
    if K > 1:
        cnt = 0
        start = 0
        result = ""
        for i in range(len(s)):
            if cnt != K:
                cnt += 1
            if cnt == K:
                result += s[start:i+1][::-1]
                start = i + 1
                cnt = 0
        result += s[start:][::-1]
        return result
    return s

s = input()
k = int(input())
ans = reverse_groups(s, k)
print(ans)


