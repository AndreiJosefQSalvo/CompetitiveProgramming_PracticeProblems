print("Enter a list: ")
num = input()
numList = num.split()

listLength = len(numList)

count = 0
even = 0
odd = 0
while count < listLength:
   a = numList[count]
   b = int(a) % 2
   
   if b == 0:
       even += 1
   else:
       odd += 1
   count += 1

print("Even numbers: ", even)
print("Odd numbers: ", odd)
