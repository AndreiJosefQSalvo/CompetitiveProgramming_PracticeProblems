print("Enter a number: ")
num = input()

numSum = 0
count = 0
while count <= int(num):
    numSum += count
    count += 1
print("The sum from 1 to ", num, " is ", numSum)