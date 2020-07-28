def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))
#input from user
nTerms = int(input("Enter total number of terms you want to print in fibonacci series = "))
if nTerms <= 0:
    print("Invalid Input. Please Enter Positive number")
else:
    print("Fibonacci Series")
    for i in range(nTerms):
        print(recur_fibo(i))
