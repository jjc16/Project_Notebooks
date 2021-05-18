# Given a string of digits, generate all strings that could represent that number given the standard phone pad mapping.
# "23" -> ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
PHONE_PAD = {
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
}

def tmp(st2):
    # print(st2)
    out = []
    
    if len(st2) < 1:
        return []
    if len(st2) == 1:
        return PHONE_PAD[int(st2[0])]
    if len(st2) <= 2:
        out = [t1 + t2 for t1 in PHONE_PAD[int(st2[0])] for t2 in PHONE_PAD[int(st2[1])]]
        return out
    else:
        out2 = tmp(st2[:-1])
        out3 = [t1 + t2 for t1 in out2 for t2 in PHONE_PAD[int(st2[-1])]]
        return out3

def combos(st):
    out = []
    st2 = [st[ii] for ii in range(len(st))]
    out = tmp(st2)
    
    return out

print(combos(''))
    
    

        
