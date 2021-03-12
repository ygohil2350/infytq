strong_num_list =[]
def factorial(number):
    if number == 1:
        return (number)
    elif number == 0:
        return 1
    else:
        return (number * factorial(number-1))

    return fact
    #remove pass and write your logic to find and return the factorial of given number


def find_strong_numbers(num_list):
    #remove pass and write your logic to find and return the list of strong numbers from the given list
    result = []
    for num in num_list:
        temp = str(num)
        answer = 0
        for t in temp:
            answer = answer + factorial(int(t))
        if num == answer:
            result.append(num)
    return (result)
 
num_list=[145,375,100,2,10,40585,0]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
