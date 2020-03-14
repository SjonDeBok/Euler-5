def primeGen():
  """
  Generator of prime numbers
  Returns: int
  """
  yield 2
  primes = []
  nextprime = 3
  while True:
    primes.append(nextprime)
    yield nextprime
    while True:
      nextprime += 2
      remainders = map(lambda x: nextprime%x, primes)
      if not 0 in remainders: 
        break


def highestPowerUpTo(num, limit):
  """
  Calculates the highest power of num up to the limit value
  e.g. if num = 2 and limit = 20: it calculates 2^4 = 16 as the highest power of 2 up to 20 
  Returns: int
  """
  powered = num
  while powered <= limit:
    powered *= num
  return int(powered/num)


limit = 20
prime = primeGen()
powers = []
num = next(prime) 
while num <= limit:
  powers.append(highestPowerUpTo(num, limit))
  num = next(prime) 
result = 1
for num in powers:
  result *= num
print(result)
