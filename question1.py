def capital_first_last(s):
    newstring = s.split(" ")
    res = []
    for words in newstring:
        if (len(words) == 0):
            res.append(words)
        else:
            if ( len(words) == 1):
                res.append(words[0].upper())
            
            else:
                res.append( words[0].upper() + words[1:-1] + words[-1].upper())
    return " ".join(res)
s = input()
print(capital_first_last(s))