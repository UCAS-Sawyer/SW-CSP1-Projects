def sum_even_numbers(numbers):

     sum = 0
     numbers = str(numbers)
     for num in numbers:
          num = int(num)
          if num % 2 == 0:

               sum += num

          elif num % 2 !=0:
               #This is just doing nothing and moving on to the next number
               x = "fun"

     return sum
print(sum_even_numbers(1232696532414336547658989916325421133))