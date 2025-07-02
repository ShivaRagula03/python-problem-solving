# #prime numbeer to print from 1 to 100
# def prime_number(p_n):
#     if p_n<=1:
#         return False
#     for i in range(2,p_n):
#         if p_n % i==0:
#             return False
#     return True
# for num in range(1,100):
#     if prime_number(num):
#         print(num, end=' ' )


# #find next prime number 
# def prime_number(p_n1):
#     if p_n1<=1:
#         return False
#     for i in range(2,p_n1):
#          if p_n1 % i==0:
#             return False
#     return True
# def next_prime(num):
#     next_num = num + 1
#     while True:
#         if prime_number(next_num):
#             return next_num
#         next_num = next_num + 1
# n_n=int(input("Enter the number:"))
# nextprime = next_prime(n_n)
# print(f'the next prime is {nextprime}')

# #find previos prime
# def prime_number(p_n2):
#     if p_n2<=1:
#         return False
#     for i in range(2,p_n2):
#         if p_n2 % i == 0:
#             return False
#     return True
# def previous_prime(n):
#     previous_num = n - 1
#     while True:
#         if prime_number(previous_num):
#             return previous_num
#         previous_num = previous_num - 1
# Pn =int(input("Enter a Number :"))
# preprime = previous_prime(Pn)
# print(f'The previous Prime number is {preprime}')

#find amstrong number between 1 to 2000
for n in range(1,2001):
 k = n
 length = len(str(n))
 sum = 0
 while n !=0:
       s = n%10
       n = n//10
       sum = sum+(s**length)
    
 if k == sum:
    print(k,end=' ')

        



        
        
    
  


         
             
        




            
