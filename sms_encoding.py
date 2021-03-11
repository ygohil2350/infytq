#lex_auth_01269444961482342489

def sms_encoding(data):
    #start writing your code here
    vowel = "aeiouAEIOU"
    list1 = data.split()
    list2 = []

    for i in list1:
        length=len(i)
        if length == 1:
            list2.append(i)
            list2.append(" ")#to add spaces between the words
        else:
            count=0
            for a in i:
                if a in vowel:
                    count+=1 
            if count==length: #to check if all the letters are vowels
                list2.append(i)
                list2.append(" ")
            for a in i:
                if a not in vowel:
                    list2.append(a)

            list2.append(" ")
    list2.pop() #to remove the extra space at the end of the whole sentence
    q="".join(list2)
    return q

data="I love Python"
print(sms_encoding(data))
