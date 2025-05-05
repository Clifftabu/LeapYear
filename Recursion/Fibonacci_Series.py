n=int(input("What value do u want for your fibonacci series?: "))

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
for i in range(0,7):
    print(fibonacci(i))
    
print(fibonacci(5))
