#lex_auth_012693816779112448160

def calculate(distance,no_of_passengers):
    #Remove pass and write your logic here
    cost=0
    cost=70*distance/10
    rest=0
    rest=no_of_passengers*80 
    if cost<=rest:
        return abs(cost - rest)
    else:
        return -1




#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))
