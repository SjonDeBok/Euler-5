def euler_five(limit=20):
  """
  Calculates the smallest positive number that is evenly divisible by all of the numbers from 1 to limit value.
  Returns: int
  """
  prime = primeGen()
  num = next(prime) 
  result = 1
  while num <= limit:
    result *= highestPowerUpTo(num, limit)
    num = next(prime)
  return result


def primeGen():
  """
  Generator of prime numbers
  Returns: int
  """
  yield 2 # The smallest prime number
  primes = []
  nextprime = 3 # The smallest odd prime number
  while True:
    yield nextprime
    primes.append(nextprime)
    while True:
      nextprime += 2 # All other prime numbers are odd, even numbers need not be tested
      remainders = [nextprime%x for x in primes]
      if not 0 in remainders: break


def highestPowerUpTo(num, limit):
  """
  Calculates the highest power of num up to the limit value
  e.g. if num = 2 and limit = 20: it calculates 2**4 = 16 as the highest power of 2 up to 20 
  Returns: int
  """
  powered = num
  while powered <= limit: powered *= num
  return powered//num # num is multiplied one time too many, so divide again


print(euler_five())
