# : Write a program to print the sum of the digits in the number.
# Testcase1 : 101
# Output : 2
# Explanation : Sum of the digits in the number 1+0+1 = 2, Answer is 2.
# Testcase1 : 567
# Output : 18
# Explanation : Sum of the digits in the number 5+6+7 = 18, Answer is
# 18.


s = 121
sum = 0
while s!=0:
   num = s % 10
   s = s//10
   sum+=num
print(sum)


# multiply
s1 = 432
mul = 1
while s1!=0:
   num = s1 % 10
   s1 = s1//10
   mul = num * mul
print(mul)

#  Write a program to print reverse of the given number.
# Testcase1 : 721
# Output : 127
# Explanation : Reverse of the number 721 is 127.
# Testcase1 : 765
# Output : 567
# Explanation : Reverse of the number 765 is 567.
       
number = 721
rev = 0
while number!=0:
      num1 = number % 10
      number = number // 10
      rev = rev * 10 + num1
print(rev)

# palindrome

n1 = 121
paa = n1
pal=0
while n1!=0:
      n2 = n1 % 10
      n1 = n1//10
      pal = pal *10 + n2
print(pal)
if paa == pal:
 print("number is palindrome")
else:
 print("number is not palindrome")
 
 
#Armstrong number

arm = 153
l = arm
lengg = len(str(arm))
sum11 = 0
while arm!=0:
      arm1 = arm % 10
      arm = arm//10
      sum11 = sum11+(arm1**lengg)
if l ==sum11:
      print("num is armstrong")
else:
      print("num is not armstrogn")



      
      
      



    



      
      

        
        
        


   
   
   
