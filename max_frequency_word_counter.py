#lex_auth_0127382283825971201450

def max_frequency_word_counter(data):
    word=""
    frequency=0

    #start writing your code here
    data=data.lower()
    raw=data.split()
    temp=[]
    l=[]
    cnt=[]
    length=[]
    for val in raw:
        if val not in temp:
            temp.append(val)
    for i in temp:
        c=raw.count(i)
        s1=str(i)+" "+str(c) 
        cnt.append(c)
        l.append(s1)
    frequency=max(cnt)
    if cnt.count(frequency)>1:
        for i in range (0,len(cnt)):
            if cnt[i]==frequency:
                length.append(len(l[i]))
        m=max(length)
        i1=length.index(m)
        word=l[i1]
        print(word)
    else:
        num=str(frequency)
        for i in l:
            s=i.split()
            for val in s:
                if num in val:
                    word=s[0]
        print(word,frequency)
    #Populate the variables: word and frequency


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    #print(word,frequency)


#Provide different values for data and test your program.
data="Work like you do not need money, love like you have never been hurt, and dance like no one is watching"
max_frequency_word_counter(data)
