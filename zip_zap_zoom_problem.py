#lex_auth_01269363490743091290

def display(num):
    message=""
    #write your logic here
    if(num%3==0 and num%5==0):
        message="zoom"
    elif(num%5==0):
        message="zap"
    elif(num%3==0):
        message="zip"
    else:
        message="Invalid"
    return message
message=display(9)
print(message)
