n= int(input())
def fizz_buzz (n):
    for l in range (1,n+1):
        if l%5==0 and l%3==0:
            print ("FizzBuzz")
        elif l%5==0:
            print ("Buzz")
        elif l%3==0:
            print ("Fizz")
        else: 
            print (l)

fizz_buzz(n)