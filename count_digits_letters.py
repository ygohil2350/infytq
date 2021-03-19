#lex_auth_0127135838317445121147

def count_digits_letters(sentence):
    #start writing your code here
    return [sum(c.isalpha() for c in sentence),sum(c.isdigit() for c in sentence)]


sentence="Infosys Mysore 570027"
print(count_digits_letters(sentence))
