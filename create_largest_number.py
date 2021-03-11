#lex_auth_01269441913243238467

def create_largest_number(number_list):
   #remove pass and write your logic here
    number_list.sort(reverse = True)
    new_number_list=[]
    for index,value in enumerate(number_list):
        ele=number_list.pop(index)
        number_list.insert(index,str(ele))
    return int("".join(number_list))

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
