#lex_auth_01269446533799116898

def check_perfect_number(number):
    #start writing your code here
    num=[]
    for i in range(1,number):
        if number%i==0:
            num.append(i)
    total=sum(num)
    if number==total and number!=0:
        return True
    else:
        return False

def check_perfectno_from_list(no_list):
    #start writing your code here
    perfect=[]
    for i in no_list:
        result=check_perfect_number(i)
        if result:
            perfect.append(i)
    return perfect

perfectno_list=check_perfectno_from_list([18,6,4,2,1,28])
print(perfectno_list)
