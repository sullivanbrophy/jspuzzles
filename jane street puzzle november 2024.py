import random
import math
sqrt = math.sqrt

def log(s):
    if DEBUG:
        print(s)

DEBUG = False
iterations = 10 ** 10
hits = 0

for iteration in range(iterations):
    r2 = random.random()
    s1 = math.sqrt(random.random())

    blueX = .5 * s1
    blueY = blueX *(1.0 - r2)
    redX = random.random()
    redY = random.random()
    bluetozerozero = sqrt(blueX**2 + blueY**2)
    bluetoonezero = sqrt((1-blueX)**2 + blueY**2)
    redtozerozero = sqrt(redX**2 + redY**2)
    redtoonezero = sqrt((1-redX)**2 + redY**2)
    if bluetozerozero>=redtozerozero or bluetoonezero>=redtoonezero:
        hits += 1
print (hits/iterations)
