#lex_auth_01269438594930278448

def find_pairs_of_numbers(num_list,n):
    
    #Remove pass and write your logic here
    count=0
    for index,num in enumerate(num_list):
        for i in range(index+1,len(num_list)):
            if num+num_list[i]==n:
                count=count+1
    return count
num_list=[1, 2, 4, 5, 6]
n=6
print(find_pairs_of_numbers(num_list,n))
