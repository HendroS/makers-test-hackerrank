import re

def testRegex(w):
    # patt=r"^(([a-z]([_]\d{0,4})?){1,6})\@hackerrank.com"
    patt=r"^((([a-z]){1,6}([_][0-9]{0,4})?))\@hackerrank.com"
    reg = re.compile(patt)
    if re.fullmatch(reg, w):
        return "Valid email"
    else:
        return 'not valid'
    


word=[
    'em_i_@hackerrank.com',
    'julia_0@hackerrank.com',
    'juliaaaaa_0@hackerrank.com',
    'julia0_@hackerrank.com',
    'julia_0123@hackerrank.com',
    'julia_a@hackerrank.com',
    'emi@',
    '089,']

for w in word:
    print(w,testRegex(w))
