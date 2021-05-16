import math
def f(x):
  return x * math.cos(x) * math.sin(30 * x)

a = 0
cyc = 0
error = 0.00000001
b = 2*math.pi 

h = b - a
t1 = h * (f(a) + f(b)) / 2
h = h / 2
n = 1
t2 = t1 / 2 + h * (f(a + h))
s1 = (4 * t2 - t1) / 3

h = h / 2
n = 2 * n
t4 = t2 / 2 + h * (f(a + h) + f(a + 3 * h))
s2 = (4 * t4 - t2) / 3
c1 = (16 * s2 - s1) / 15

h = h / 2
n = 2 * n
s = 0
for i in range(n):
  s = s + h * (f(a + (2 * (i+1) - 1) * h))
t8 = t4 / 2 + s
s4 = (4 * t8 - t4) / 3
c2 = (16 * s4 - s2) / 15
r1 = (64 * c2 - c1) / 63

while True:
    h = h / 2
    n = n * 2
    s = 0
    for i in range(n):
        s = s + h * (f(a + (2 * (i+1) - 1) * h))
    t2k = t8 / 2 + s
    s2k_1 = (4 * t2k - t8) / 3
    c2k_2 = (16 * s2k_1 - s4) / 15
    r2k_3 = (64 * c2k_2 - c2) / 63
    calc_error = abs(r2k_3 - r1)
    t8 = t2k
    s4 = s2k_1
    c2 = c2k_2
    r1 = r2k_3
    cyc = cyc + 1
    if calc_error<error:
        print(r1,cyc)
        break
