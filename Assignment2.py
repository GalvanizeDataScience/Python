#Q1
'''
str = input("Enter any String: ")
print(str)
final_str = str.lower()
print(final_str)
'''
#Q2 
'''''
import string
all_letters= string.ascii_letters
numbers = [n for n in range(len(all_letters))]    
dict1 = {}
key = 3
for i in range(len(all_letters)):
    dict1[all_letters[i]] = numbers[(i+key)%len(all_letters)]
   
plain_txt= "Nourh Manal"
cipher_txt=[]

for char in plain_txt:
    if char in all_letters:
        temp = dict1[char]
        cipher_txt.append(temp)
    else:
        temp=char
        cipher_txt.append(temp)

print("Cipher Text is: ",cipher_txt)
   

dict2 = {}     
for i in range(len(all_letters)):
    dict2[numbers[i]] = all_letters[(i-key)%(len(all_letters))]

decrypt_txt = []
  
for char in cipher_txt:
    if char in numbers:
        temp = dict2[char]
        decrypt_txt.append(temp)
    else:
        temp = char
        decrypt_txt.append(temp)

print("Recovered plain text :", decrypt_txt)
'''

#Q3 
'''
str = input("Please enter any string: ")
if str == 'x':
    exit();
else:
    newstr = str;
    vowels = ('a', 'e', 'i', 'o', 'u');
    for x in str.lower():
        if x in vowels:
            newstr = newstr.replace(x,"");
    print(newstr);
'''
#Q4
'''
str = input("Enter a string\n")

if str.isnumeric():
    print("string contains a number ")
elif str.replace(".","").isnumeric():
    print("string contains an float number ")
else: 
    print("string does not contain a number ")

'''
#Q5
'''
print("Enters numbers to calculate their sum (Input 0 to exit): ")
count = 0
sum = 0
number = 1
while number != 0:
	number = int(input(""))
	sum = sum + number
	count += 1
if count == 0:
	print("Input numbers please")
else:
    	print(" Sum of the above numbers are: ", sum)
'''
#Q6 

'''
num1 = input("Please enter any number : ")
num2 = input("Please enter other any number as last number: ")

assert num1.isnumeric() or num1.isnumeric(), "The two inputs entered should be numeric"
num1 = int(num1)
num2 = int(num2)
assert num1 != 0 , "The divider should be pos or neg number not zero"
assert num2 >= 0 , "The second should be greater than zero"

divisible_nums = []
for i in range(num2):
    if i%num1==0:
'''
#Q7
'''
num1 = int(input("Please enter a first number : "))
num2 = int(input("Please enter a second number : "))
if num2<num1:
    small = num1
    lar = num2
else:
    small = num2
    lar = num1
mult_list = []
for i in range(1, int(lar)):
    mult_res = i*int(small)
    if mult_res<=int(lar):
        mult_list.append(mult_res)
print(mult_list) 
'''

#Q8

 '''
num = int(input(""Please enter a number to check if a number is prime or not: "))
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")
   '''

#Q9
#I do not understand