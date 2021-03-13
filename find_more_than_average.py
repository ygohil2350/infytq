#lex_auth_01269438947391897654

#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    #Remove pass and write your logic here
    sum=0
    count=0 
    for i in list_of_marks:
        sum+=i
    avg=sum/len(list_of_marks)
    for i in list_of_marks:
        if i>avg:
            count+=1
    per=(count*100)/len(list_of_marks)
    return per

def sort_marks():
   #Remove pass and write your logic here
    sorted_marks=sorted(list_of_marks)
    return sorted_marks

def generate_frequency():
    #Remove pass and write your logic here
    l=[]
    for i in range(0,26):
        l.append(list_of_marks.count(i))
    return l

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
