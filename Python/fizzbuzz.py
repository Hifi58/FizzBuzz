number = 0
while number < 101:
  number = number +1
  if number%15 == 0:
    print("Fizzbuzz")
  elif number%3 == 0:
    print("Fizz")
  elif number%5 == 0:
    print("buzz")
  else:
    print(number)
