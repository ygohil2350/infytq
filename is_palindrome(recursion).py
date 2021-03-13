#lex_auth_01269442114344550475

def is_palindrome(word):
    #Remove pass and write your logic here
    word.lower()
    if word[::-1].lower() == word.lower():
        return 1
    else:
        return 0

#Provide different values for word and test your program
result=is_palindrome("MadAMa")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
