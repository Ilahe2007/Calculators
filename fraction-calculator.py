from fractions import Fraction
a=1
while a!=' ':
  try:
    a,c,b=map(str,input().split())
    a=a.replace('/',' ')
    a=a.split()
    a=list(map(int,a))
    a1=Fraction(a[0],a[1])
    b=b.replace('/',' ')
    b=b.split()
    b=list(map(int,b))
    b1=Fraction(b[0],b[1])
    if c=='*':
      if (a1*b1)//1!=(a1*b1):
        print(a1*b1)
      else:
        print(str(a1*b1)+'/'+'1')
    elif c=='+':
      if (a1+b1)//1!=(a1+b1):
        print(a1+b1)
      else:
        print(str(a1+b1)+'/'+'1')
    elif c=='-':
      if (a1-b1)//1!=(a1-b1):
        print(a1-b1)
      else:
        print(str(a1-b1)+'/'+'1')
    else:
      if (a1/b1)//1!=(a1/b1):
        print(a1/b1)
      else:
        print(str(a1/b1)+'/'+'1')
  except:
    break
