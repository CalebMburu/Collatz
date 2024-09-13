def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        result = 3 * number + 1
        print(result)
        return result
    
print('Enter number: ')
try:
    userNum = int(input())
    while userNum != 1:
        userNum = collatz(userNum)

except ValueError:
    print('You must enter an integer.')