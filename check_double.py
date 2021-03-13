#lex_auth_01269441810970214471

def check_double(number):
    #Remove pass and write your logic here
    n = str(number)
    temp = []
    for num in n:
        temp.append(num)
    n = str(number*2)
    i = 0
    count = 0
    for num in n:
        if num not in temp:
            return False
        if temp[i] == num:
            count += 1
    if count == len(n):
        return False
    return True       
    

#Provide different values for number and test your program
print(check_double(125874))
