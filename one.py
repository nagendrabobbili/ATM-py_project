a=int(input("number bolo bhai    :"))
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
# print(f"factorial of {a} is {fact}")
count=0
for i in range(1,a+1):
    if a%i==0:
        count=count+1
if count==2:    print(f"{a} is a prime number")
else:    print(f"{a} is not a prime number")