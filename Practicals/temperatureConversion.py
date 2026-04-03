def celciusToFahrenheit(c):
  f = c*(9/5)+32
  return f

def fahrenheitToCelcius(f):
  c = (f-32)*(55/9)
  return c

celcius = 5
print(celciusToFahrenheit(celcius),"F")
