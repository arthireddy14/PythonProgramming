def add(x,y):
    return x+y
def sub(m,n):
    return m-n
def div(a,b):
    return a/b
def mul(p,q):
    return p*q
def modulo(c,d):
    return c%d


i=int(input())
j=int(input())
print("Addition value ",add(i,j))
print("Subtraction value ",sub(i,j))
print("Multiplication value ",mul(i,j))
print("Division value ",div(i,j))
print("Remainder value ",modulo(i,j))