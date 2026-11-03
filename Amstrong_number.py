n=int(input("Enter the value of n :"))
b=n
cal=0
while n>0:
    num=n%10
    cal=cal+(num**3)
    n=n//10
if b == cal:
    print("This is the Amstrong number")
else:
    print("This is the  not Amstrong number")