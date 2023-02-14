def integral(f,a,b,n):
  deltaX = (b-a/n)
  sum = 0
  for i in range(1, n+1):
    sum+=f(a+(i-1)*deltaX)*deltaX
  return sum


equation = lambda x: eval(input("enter your equation in python code format: "))
print(integral(equation, 0,2,2))