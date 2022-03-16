def fib(num1):
  if num1 == 1:
    return 0
  elif num1 == 2:
    return 1
  else:
    return fib(num1-1) + fib(num1-2)
    
print(fib(3))
