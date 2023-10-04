import math

# Write your code below this line 👇
def prime_checker(number):
   is_prime=True
   for i in range(2,number):    
       if number%i==0:
           is_prime=False

   if is_prime:
     print("The Number is Prime")
   else:
           print("The number is not Prime")



# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Choose a Number :")) # Check this number
prime_checker(number=n)