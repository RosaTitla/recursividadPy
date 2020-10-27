#https://infseg.com/informatica/recursividad-cuando-debo-utilizarla/

def factorial(n):
    result=1
    if n<=1:
        return result
    for i in range(2,n+1):
        result=result*i
    return result

n=int(input('número'))
print(factorial(n))
