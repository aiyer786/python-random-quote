import random
def primary():
  #print("Keep it logically awesome.")

  f = open("python-random-quote\quotes.txt","a")
  f.write("\nwillem DAFOE!")
  f.close()
  f = open("python-random-quote\quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 20
  rnd = random.randint(0, last)
  print(quotes[rnd],end='')
  rnd = random.randint(0, last)
  print(quotes[rnd])


if __name__== "__main__":
  primary()
