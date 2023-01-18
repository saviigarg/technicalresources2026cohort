#ques9

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
def lcm(a,b):
    return (a*b)//gcd(a,b)
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print("LCM of", num1, "and", num2, "is: ", lcm(num1,num2))
print("GCD of", num1, "and", num2, "is: ", gcd(num1,num2))
