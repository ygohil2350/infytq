#lex_auth_012693825794351104168

def find_common_characters(msg1,msg2):
    #Remove pass and write your logic here
    msg11=msg1.replace(" ","")
    msg21=msg2.replace(" ","")
    l=[]
    s=[]
    for i in msg11:
        if i in msg21:
            l.append(i)
    for x  in l:
        if x not in s:
            s.append(x)
    if len(s)>0:
        return "".join(s)
    else:
        return -1
#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
