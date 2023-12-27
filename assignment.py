# ⁠write Pgm to find prime number or not

num = 4

for i in range(2,num):
  if num%i==1:

    print('Not Prime')
    break
else:
  print("Prime")


#Write a program to create a list of fruits and copy only 'e' letter fruits to the new list

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruitslist = []

for x in fruits:
  if "e" in x:
   fruitslist.append(x)

print(fruitslist)  
