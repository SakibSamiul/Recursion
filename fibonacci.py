#fibonacci n number
def fibo(n):
    fibo0 = 0
    fibo1 = 1
    if n == 0:
        return fibo0
    elif  n == 1:
        return fibo1
    else:
        return fibo(n-1) + fibo(n-2)
    
print(fibo(9))


# fibonacci series sequence
def fibo(n):
   if n <= 1:
      return 1
   else:
      return fibo(n-1) + fibo(n-2)

n = int(input("enter a number: "))

if n <= 0:
   print("enter a positive number")
else:
   print("Fibonacci sequence")
   for i in range(n):
      print(fibo(i))