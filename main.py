def isPrime(num):
  """ 
  Determines wheter num is a prime number
  Returns: bool
  """
  if num < 2:
    return False
  i = num-1
  while i > 1:
    if num%i == 0:
      return False
    else:
      i -= 1
  return True


def allPrimesUpTo(limit):
  """
  Collects all prime numbers up to limit value
  Returns: list
  """
  primes = []
  i = limit
  while i > 1:
    if isPrime(i):
      primes.append(i)
    i -= 1
  return primes

def highestPowerUpTo(num, limit):
  """
  Calculates the highest power of num up to the limit value
  e.g. if num = 2 and limit = 20: powered = 2^4 = 16 as the highest power of 2 up to 20 
  Returns: int
  """
  powered = num
  while powered <= limit:
    powered *= num
  return int(powered/num)

limit = 20
primes = allPrimesUpTo(limit)
powers = []
for num in primes:
  powers.append(highestPowerUpTo(num, limit))
result = 1
for num in powers:
  result *= num
print(result)
