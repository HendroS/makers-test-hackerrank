def howMany(sentence):
    # Write your code here
    # new_sentence=""
    mark=['.',",","?","!","-"]
    # for el in sentence:
    #     if (ord(el)>=65 and ord(el)<=90) or (ord(el)>=97 and ord(el)<=122) or el==" " or (el in mark):
    #         new_sentence+=el
    # arr= new_sentence.split(" ")
    # arr2=[]
    # arr3=[]
    # for el in arr:
    #     if el !='':
    #         arr2.append(el)
    # print(arr2)
    # for el in arr2:
    arr= sentence.split(' ')
    arr1=[]
    for elm in arr:
        if elm !='':
            elm=elm.lower()
            stat=True
            for el in elm:
    
                if (ord(el)<65 or ord(el)>90) and (ord(el)<97 or ord(el)>122) and (el not in mark):
                    # new_sentence+=el
                    stat=False
                    break
            if stat==True:
                arr1.append(elm)
                    
                    # print(elm)
                    



    print(arr1)
    return len(arr1)

s="he is a good programmer, he won 865 competitions, but sometimes he dont. What do you think? All test-cases should pass. Done-done?"
s="jds dsaf lkdf kdsa fkldsf, adsbf ldka ads? asd bfdal ds bf[l. akf dhj ds 878  dwa WE DE 7475 dsfh ds  RAMU 748 dj."
print(howMany(s))