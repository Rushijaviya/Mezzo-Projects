import random

n= int(input("Enter the length of password : "))
string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

if n>73:            # As Maximum possible character is 73 whenever input is greater than 73 
    s=""            # we need to iterate over it 
    while n:
        n-=1
        s=s+str("".join(random.sample(string, 1)))
    password=s

else:
    password =  "".join(random.sample(string, n))

print("Random generated password : ", password)