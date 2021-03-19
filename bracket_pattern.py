#lex_auth_0127135773590405121141

def bracket_pattern(input_str):
    #Remove pass and write your code here
	return input_str.startswith('(') and (input_str.count('(')==input_str.count(')'))
input_str="(())("
print(bracket_pattern(input_str))
