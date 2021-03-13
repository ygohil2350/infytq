#lex_auth_0127382164803993601239

#This verification is based on string match.

def sum_of_numbers(list_of_num,filter_func=None):
    #Remove pass and write the logic here    
    num_sum=0
    if filter_func!=None:
        num_sum=sum(filter_func(list_of_num))
    else:
        num_sum=sum(list_of_num)
    return num_sum

def even(data):
    #Remove pass and write the logic here
    eve=[]
    for num in data:
        if num%2==0:
            eve.append(num)
    return eve

def odd(data):
    #Remove pass and write the logic here
    od=[]
    for num in data:
        if num%2!=0:
            od.append(num)
    return od

sample_data = range(1,11)

print(sum_of_numbers(sample_data,None))
