import random
def primary():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  str1 = " 'hello' "
  print(str1)

  str2 = " 'world' "
  print (str2)

  str3  = str1 + str2
  print(str3)

  last = 13
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  primary()