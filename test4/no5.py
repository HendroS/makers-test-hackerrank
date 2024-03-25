def isPangram(pangram):
    # Write your code here
    #97 sd 122
    # d=dict(
    string=''
    for el in pangram:
        d=dict()
        stat=True
        for ch in el:
            if ch!=" ":
                if ord(ch) not in d:
                    d[ord(ch)]=1
        for i in range(97,123):
            if i not in d:
                print(chr(i))
                stat=False
                break
        if stat==True:
            string+='1'
        else:
            string+='0'
    return string

s=['we promptly judged antique ivory buckles for the next prize']

print(isPangram(s))