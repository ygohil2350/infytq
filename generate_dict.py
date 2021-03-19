#lex_auth_0127135904626688001159

def generate_dict(number):
    new_dict={}
    for x in range(1,number+1):
        new_dict[x]=x**2
    return new_dict

number=20
print(generate_dict(number))
