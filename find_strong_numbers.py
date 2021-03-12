#lex_auth_01269437118923571233
strong_num_list =[]
def factorial(number):
    fact=1
    if(number == 0 or number == 1):
        fact = 1
        
    else: 
        for i in range(1,number + 1):
            fact = fact*i
            
             
    return fact
    #remove pass and write your logic to find and return the factorial of given number


def find_strong_numbers(num_list):
    #remove pass and write your logic to find and return the list of strong numbers from the given list
     
    number=0
    for z in num_list: 
        temp = z
        sum = 0
        while(temp): 
            number = temp % 10
            sum =sum + factorial(number) 
            temp = temp // 10
        if(sum == z): 
            strong_num_list.append(z) 
        else: 
            pass  
              
    return strong_num_list 


num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
