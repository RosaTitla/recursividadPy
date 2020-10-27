
def is_palindrome(word):
    if len(word) < 2:
        # base case
        return True
    else:
        # recursive case
        if word[0] != word[-1]:
            return False
        else:
            return is_palindrome(word[1:-1])


#print (is_palindrome("a"))
#print (is_palindrome("silla"))
#print (is_palindrome("oso"))
print (is_palindrome("reconocer"))

