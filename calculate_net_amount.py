#lex_auth_0127135929511936001157

def calculate_net_amount(trans_list):
    #start writing your code here
    W,D=0,0
    for i in trans_list:
        temp = i.split(":")
        if temp[0]=="D":
            D+=int(temp[1])
        else:
            W+=int(temp[1])
    return D-W

    
    return net_amount

trans_list=["D:300","D:200","W:200","D:100"]
print(calculate_net_amount(trans_list))
