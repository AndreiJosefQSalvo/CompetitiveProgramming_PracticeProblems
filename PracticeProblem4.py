print("Enter a range (starting number): ")
num1 = input()
print("Enter a range (ending number): ")
num2 = input()

count = int(num1)
div27 = []
div35 = []
while count <= int(num2):
   a = int(count) % 2
   b = int(count) % 7
   c = int(count) % 3
   d = int(count) % 5
   
   if a == 0:
       if b == 0:
           div27.append(count)
   if c == 0:
       if d == 0:
           div35.append(count)
   count += 1

print("Numbers divisible by 2 and 7: ", div27)
print("Numbers divisible by 3 and 5: ", div35)
