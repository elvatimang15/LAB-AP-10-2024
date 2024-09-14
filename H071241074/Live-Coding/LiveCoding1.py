a = float(input("Input a (Nilai a ≠ 0): "))
b = float(input("Input b: "))
c = float(input("Input c: "))

import math

def hitung_akar(a, b, c): 
  D = b**2 - 4*a*c
  x1 = (-b + math.sqrt(D)) / (2*a)
  x2 = (-b - math.sqrt(D)) / (2*a)
  return x1, x2
x1, x2 = hitung_akar(a, b, c)

print(f"x1 = {x1:.2f}")
print(f"x2 = {x2:.2f}")

