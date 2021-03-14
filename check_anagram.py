#lex_auth_0127382206342184961397

def check_anagram(data1,data2):
    #start writing your code here
    data2=data2.lower()
    data1=data1.lower()
    c=0
    l=[]
    s=""
    if(len(data2)==len(data1)):
        for i in range(0,len(data1)):
            for j in range(0,len(data2)):
                if(data2[j]==data1[i] and i!=j and not(j in l)):
                    l.append(j)
                    c+=1
                    break
    if(c==len(data2)):
        return True
    else:
        return False
print(check_anagram("eat","tea"))
