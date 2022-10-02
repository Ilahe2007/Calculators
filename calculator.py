x=int(input())
a='1'
b=1
while a!=' ' and b!=' ':
  try:
    a,b=map(str,input().split())
    b=int(b)
    if a=='+':
      x=x+b
    elif a=='-':
      x=x-b
    elif a=='*':
      x=x*b
    elif a=='/':
      x=x/b
    else:
      x=x+0
    print(x)
  except:
      break
