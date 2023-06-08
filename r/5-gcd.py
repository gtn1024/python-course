def gcd(x:int,y:int):
  return x if y==0 else gcd(y, x%y)

if __name__ == '__main__':
  print(f'gcd(10, 20)={gcd(10, 20)}')
