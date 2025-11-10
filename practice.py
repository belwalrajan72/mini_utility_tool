def odd_or_even(num):
    return "Even" if num%2 == 0 else "Odd"


def factorial(num):
    total = 1
    for i in range(1,num+1):
        total *= i
    return total 

def sum_all(num):
    total = 0 
    for i in range(1,num+1):
        total += i
    return total

def celcious_to_fahrenheit(n):
    f = (n*9/5)+32
    return f






while True :
    print('\nSmart Utility tool')
    print('1. Find Odd/even')
    print('2. Sum of n numbers')
    print('3.factorial upto n numbers')
    print('4. Multiplication table of a number')
    print('5. divisible by 5 upto n. ')
    print('6. Convert Celsius to fahrenheit.')
    print('7. Exit')

    choice =  input("Enter your choice :")
    
    if choice == "1":
        n = int(input('Enter a number :'))
        print(odd_or_even(n))
    
    elif choice == "2":
        n = int(input("Enter a number :"))
        print(sum_all(n))

    elif choice == "3":
        n = int(input("Enter a number:"))

        print(factorial(n))

    elif choice == "4":
        n = int(input('Enter a number:'))
        for i in range(1,11):
            print(f'{n} x {i} = {n*i}')
        
    
    elif choice == "5":
        n = int(input('Enter a number :'))
        for  i in range(1,n+1):
            if i % 5 == 0 :
             print(i)
    elif choice == "6":
        celcious = int(input("Enter the tempreture :"))
        print(celcious_to_fahrenheit(celcious))

    elif choice == "6": 
        print("Goodbye!")
        break
    elif choice == "quit":
        break
    else :
        print("Invalid Input.")

rajan = "belwal"