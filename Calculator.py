
print("Operations:")
print("To add - select 1")
print("To subtract - select 2")
print("To multiply - select 3")

choice = int(input()) # Input operation

print("Enter 1st number:")
number1 = int(input())

print("Enter 2nd number:")
number2 = int(input())

if(choice == 1):
    output = number1 + number2
elif(choice == 2):
    output = number1 - number2;
else:
    output = number1 * number2

print(output) # output operation

print("apple")
print(1)
