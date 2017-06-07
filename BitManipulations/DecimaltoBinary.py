def convertToBinary(num):
  """Function to print binary number
  for the input decimal"""
  binary = 0
  base = 1
  while num > 0:
    remainder = num % 2
    binary = binary + remainder * base
    num = num / 2
    base = base * 10

  print "The binary of the given number is ", binary, '.'

# decimal number
dec=1910

convertToBinary(dec)
