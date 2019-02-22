def sum(func,lb,up):
    total = 0
    while(lb <= up):
      total += func(lb)
      lb +=1
    return total

def id(i):
  return i 

def sqr(i):
  return i * i




