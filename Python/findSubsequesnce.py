'''
You are given two strings s and t consisting of only lowercase English letters.

Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
'''
def findSubsequence(s: str, t: str):
    lenS = len(s)
    lenT = len(t)
    
    if lenS == 1:
        if s[0] == t[0]:
            print(lenT-1)
            return
        print(lenT)
        
    if lenT == 1:
        for i in range(lenS):
            if s[i] == t[0]:
                print(lenT-1)
                return
        print(lenT)
        
    ptr1 = ptr2 = 0
    ctr = lenT
    
    while ptr1 < lenS and ptr2 < lenT:
        if s[ptr1] == t[ptr2]:
            ctr-=1
            ptr2+=1
        ptr1+=1
    
    print(ctr)

s= "coaching"
t= "coding"

print(sorted(s))

findSubsequence(s, t)