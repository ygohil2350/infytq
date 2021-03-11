#lex_auth_012693763253788672132

def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    #Write your logic here
    source=source[0:3]
    destination=destination[0:3]
    tickets=[]
    ot=[]
    for x in range (1,no_of_passengers+1):
        tickets.append(100+x)
        ot.append(airline+':'+source+':'+destination+':'+str(tickets[x-1]))
    if no_of_passengers>=5:
        ticket_number_list=ot[-5:-1]+ot[no_of_passengers-1:no_of_passengers]
    elif no_of_passengers<5:
        ticket_number_list=ot
    #Use the below return statement wherever applicable
    return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",7))
