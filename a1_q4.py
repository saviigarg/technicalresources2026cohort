low=int(input("Enter the lowest range value: "))
high=int(input("Enter the highest range value: "))
print("The prime numbers in this range are: ")

for num in range(low,high+1):
    if num>1:
        for i in range(2,num):
            if (num%i==0):
                break
        else:
            print(num)
