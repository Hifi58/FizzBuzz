number = 0
while number < 100:
  number = number +1
  if number%15 == 0:
    print("Fizzbuzz")
  elif number%3 == 0:
    print("Fizz")
  elif number%5 == 0:
    print("buzz")
  else:
    print(number)
