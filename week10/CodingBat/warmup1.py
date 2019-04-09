def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile or not a_smile and not b_smile:
    return True
  else:
    return False

def sum_double(a, b):
  if a > b or a < b:
    return a+b
  else:
    return 2*(a+b)

def diff21(n):
  if n < 21:
    return 21 - n
  elif n > 21:
    return 2*(n -21)
  else:
    return 0

def parrot_trouble(talking, hour):
  if talking and (hour < 7 or hour > 20):
    return True
  else:
    return False

def makes10(a, b):
  if a == 10 or b == 10 or (a + b == 10):
    return True
  else:
    return False

def near_hundred(n):
  if n >= 90 and n <= 110 or n >= 190 and n <= 210:
    return True
  else:
    return False

def pos_neg(a, b, negative):
  if negative:
    return a < 0 and b < 0
  else:
    return (a > 0 and b < 0) or (a < 0 and b > 0)
    

    
def not_string(str):
  if len(str) >= 3 and str[:3] == 'not':
    return str
  else:
    return 'not ' + str

def missing_char(str, n):
  
def front_back(str):
  
def front3(str):