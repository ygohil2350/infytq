#lex_auth_012693816331657216161

def encode(message):
    encode = message+"0"
    l=[]
    count = 1
    for index, value in enumerate(encode): 
        if value != "0":
            if value == encode[index+1]:
                count = count+1
            else:
                l.append(str(count))
                l.append(value)
                count=1    
    return "".join(l)
    
#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
