import numpy as np
import pandas as pd

### #1 Multiple of 3 and 5 ###

# Slow, methodical method

def number1():
    num1 = 3
    num2 = 5
    maximum = 1000
    result = 0
    for i in range(maximum):
        if (i % num1 == 0) | (i % num2 == 0):
            result += i
    return result

# Much faster method

def number1alt():
    num1 = 3
    num2 = 5
    maximum = 1000
    num3 = num1 * num2
    maximum = maximum - 1
    n1 = num1 * (int(maximum / num1) * (int(maximum / num1) + 1)) / 2
    n2 = num2 * (int(maximum / num2) * (int(maximum / num2) + 1)) / 2
    n3 = num3 * (int(maximum / num3) * (int(maximum / num3) + 1)) / 2
    return int(n1 + n2 - n3)

### #2 Even Fibonacci numbers ###

def number2():
    n = 4000000
    fib = [1, 2]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    del fib[-1]
    a = 0
    for i in fib:
        if i % 2 == 0:
            a += i
    return a

#3 Largest prime factor

def is_prime(n):
    a = int(np.sqrt(n)) + 1
    nums = range(2,a)
    if all(n % num != 0 for num in nums):
        b = 1
    else:
        b = 0
    return b

def number3():
    n = 600851475143
    a = int(np.sqrt(n)) + 1
    for i in range(a):
        if n % (a-i) == 0:
            if is_prime(a - i) == 1:
                return (a - i)
                break

### #4 Largest Palindrome product ###

def number4():
    na = 100
    nb = 1000
    big_list = {}

    for a in range(na, nb):
        for b in range(na, nb):
            prod = a * b
            if str(prod)[0] == str(prod)[len(str(prod)) - 1]:
                if str(prod)[1] == str(prod)[len(str(prod)) - 2]:
                    if str(prod)[2] == str(prod)[len(str(prod)) - 3]:
                        big_list[(a,b)] = a * b
                    else:
                        big_list[(a,b)] = 0
                else:
                    big_list[(a,b)] = 0
            else:
                big_list[(a,b)] = 0

    maximum = max(big_list.values())
    return(maximum)

### #5 Smallest multiple ###

def number5():
    n = 20
    nums = range(1, n + 1)
    b = n
    c = 0
    while c == 0:
        if all(b % num == 0 for num in nums):
            c = 1
        b += n
    return b - n
    
### #6 Sum square difference ###

def number6():
    n = 100
    numbers = range(1, n + 1)
    a = sum(n**2 for n in numbers)
    b = (sum(n for n in numbers)) ** 2
    c = b - a
    return c

### #7 10001st prime ###
    
def number7():
    n = 10001
    primes = [2]
    attempt = 3
    while len(primes) < n:
        if all(attempt % prime != 0 for prime in primes):
            primes.append(attempt)
        attempt += 2
    return primes[-1]

### #8 Largest product in a series ###

def number8():
    n = 13
    big = []
    w1 = 731671765313306249192251196744265747423553491949349698352031277450632623957831801698480186947885184385861560789112949495459501737958331952853208805511
    w2 = 125406987471585238630507156932909632952274430435576689664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749
    w3 = 303589072962904915604407723907138105158593079608667017242712188399879790879227492190169972088809377665727333001053367881220235421809751254540594752243
    w4 = 525849077116705560136048395864467063244157221553975369781797784617406495514929086256932197846862248283972241375657056057490261407972968652414535100474
    w5 = 821663704844031998900088952434506585412275886668811642717147992444292823086346567481391912316282458617866458359124566529476545682848912883142607690042
    w6 = 2421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    what = str(w1) + str(w2) + str(w3) + str(w4) + str(w5) + str(w6)
    
    for i in range(1000 - n + 1):
        num = int(what[i:i+n])
        prod = 1
        while(num != 0):
            prod = prod * (num % 10)
            num = int(num/10)
        big.append(prod)
    big.sort()
    return big[-1]

    
### #9 Special Pythagorean triplet ###
    
def number9():
    n = 1000
    big = []
    for a in range(1,n):
        for b in range(1,n-a):
            c = n - a - b
            if (c**2 == a**2 + b**2) & (a+b+c == n):
                z = a*b*c
                big.append(z)
    return big

### #10 Summation of primes ###

def number10():
    n = 2000000
    primes = [2]
    a = int(np.sqrt(n)) + 1
    for i in range(2, a):
        if all(i % prime != 0 for prime in primes):
            primes.append(i)
    primes2 = primes.copy()
    for i in range(a,n):
        if all(i % prime != 0 for prime in primes2):
            primes.append(i)
    sum1 = sum(primes)
    return sum1
