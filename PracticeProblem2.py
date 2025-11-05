print("Enter a number: ")
num = input()

numPro = 0
count = 1
while count <= 10:
    numPro = int(num) * int(count)
    print(num, " x ", count, " = ", numPro)
    count += 1
